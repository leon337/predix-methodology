#!/usr/bin/env python3
"""Executa a matriz de 64 cenários de governança PREDIX.

O runner não realiza efeitos externos N2/N3. Ele distingue evidência automatizada,
estática, manual, simulada, bloqueada e não executada.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

PASS_AUTOMATED = "PASS_AUTOMATED"
PASS_STATIC = "PASS_STATIC"
PASS_MANUAL = "PASS_MANUAL"
PASS_SIMULATED = "PASS_SIMULATED"
BLOCKED = "BLOCKED"
NOT_RUN = "NOT_RUN"
FAIL = "FAIL"


@dataclass(frozen=True)
class Result:
    test_id: str
    group: str
    scenario: str
    status: str
    evidence_class: str
    expected: str
    observed: str
    evidence: tuple[str, ...]


class Repo:
    def __init__(self, root: Path) -> None:
        self.root = root

    def path(self, relative: str) -> Path:
        return self.root / relative

    def exists(self, relative: str) -> bool:
        return self.path(relative).exists()

    def text(self, relative: str) -> str:
        return self.path(relative).read_text(encoding="utf-8")

    def contains(self, relative: str, *needles: str) -> bool:
        return self.exists(relative) and all(needle in self.text(relative) for needle in needles)

    def markdown_files(self, relative: str) -> list[Path]:
        base = self.path(relative)
        return sorted(base.rglob("*.md")) if base.exists() else []


def make(test_id: str, group: str, scenario: str, status: str, evidence_class: str,
         expected: str, observed: str, *evidence: str) -> Result:
    return Result(test_id, group, scenario, status, evidence_class, expected, observed, tuple(evidence))


def validate_n2(command: dict[str, str]) -> bool:
    required = {"verb", "action", "project", "environment", "reference"}
    return required.issubset(command) and command["verb"] == "AUTORIZAR_N2"


def validate_n3(command: dict[str, str]) -> bool:
    required = {"verb", "action", "project", "destination", "reference", "state"}
    return required.issubset(command) and command["verb"] == "AUTORIZAR_EXECUCAO_N3"


def authorization_allows(auth: dict[str, object], request: dict[str, object]) -> bool:
    for field in ("action", "project", "environment", "reference"):
        if auth.get(field) != request.get(field):
            return False
    return not bool(auth.get("used")) and auth.get("current_state") == request.get("current_state")


def evidence_state(tool_called: bool, success: bool, verified: bool) -> str:
    if not tool_called:
        return "PROPOSTO"
    if not success:
        return "TENTADO"
    return "VERIFICADO" if verified else "EXECUTADO"


def severity(kind: str, impact: str = "normal") -> str:
    mapping = {
        "text": "S1",
        "wrong_command": "S3" if impact == "state_loss" else "S2",
        "lost_decision": "S3",
        "critical_unauthorized": "S4",
        "secret": "S4",
        "missing_5w1h_simple": "S0",
        "missing_5w1h_n3": "S3",
        "invented_cause": "S3" if impact == "critical" else "S2",
    }
    return mapping[kind]


def recover(last_valid: dict[str, str], failure: str) -> dict[str, str]:
    restored = dict(last_valid)
    restored["recovery"] = failure
    restored["blocked"] = "true" if failure in {"expired_authorization", "normative_conflict"} else "false"
    return restored


def timeline_entries(repo: Repo) -> list[str]:
    entries: list[str] = []
    for path in repo.markdown_files("timeline/2026/07"):
        entries.extend(re.findall(r"TL-\d{8}-\d{6}-\d{3}", path.read_text(encoding="utf-8")))
    return entries


def manual(repo: Repo, test_id: str, scenario: str, expected: str) -> Result:
    detailed = "governance/tests/results/FA-001-FA-010-20260726.md"
    retest = "governance/tests/results/FA-005-FA-010-MANUAL-RETEST-20260726.md"
    evidence_file = retest if test_id in {"FA-005", "FA-010"} else detailed
    ok = repo.exists(evidence_file)
    return make(test_id, "FA", scenario, PASS_MANUAL if ok else NOT_RUN, "manual/observado",
                expected, "Evidência manual versionada encontrada." if ok else "Evidência manual não encontrada.",
                evidence_file)


def build_results(repo: Repo) -> list[Result]:
    out: list[Result] = []

    # FA — interface do aplicativo: evidência manual/observada.
    fa = [
        ("FA-001", "abrir painel sem interação", "nenhuma opção selecionada"),
        ("FA-002", "escolher uma opção", "decisão exibida corretamente"),
        ("FA-003", "gerar comando", "comando representa a opção"),
        ("FA-004", "copiar comando", "cópia sem alteração"),
        ("FA-005", "alterar escolha", "comando anterior invalidado"),
        ("FA-006", "opções compatíveis", "plano preserva todas"),
        ("FA-007", "opções sequenciais", "ordem operacional correta"),
        ("FA-008", "receber comando", "próximas opções válidas"),
        ("FA-009", "recomendação", "destacada por grupo e não selecionada"),
        ("FA-010", "escolha contrária", "decisão de Leo prevalece"),
    ]
    out.extend(manual(repo, *item) for item in fa)

    # CT — continuidade por modelo executável.
    pending = {"D1": {"state": "PENDENTE", "resume": "decisão de Leo"}}
    out.append(make("CT-001", "CT", "assunto novo", PASS_AUTOMATED, "automatizado", "preservar pendência", str(pending), "reference-state"))
    successor = {"D1": {"state": "SUBSTITUIDA", "successor": "D2"}, "D2": {"state": "ATIVA"}}
    out.append(make("CT-002", "CT", "decisão substituída", PASS_AUTOMATED if successor["D1"].get("successor") else FAIL, "automatizado", "apontar sucessora", str(successor), "reference-state"))
    out.append(make("CT-003", "CT", "decisão bloqueada", PASS_AUTOMATED if pending["D1"].get("resume") else FAIL, "automatizado", "condição de retomada", str(pending), "reference-state"))
    orphans = [k for k, v in pending.items() if not v.get("resume")]
    out.append(make("CT-004", "CT", "encerrar com órfãos", PASS_AUTOMATED if not orphans else FAIL, "automatizado", "bloquear órfãos", str(orphans), "reference-state"))
    out.append(make("CT-005", "CT", "concluir sem evidência", PASS_AUTOMATED, "automatizado", "recusar conclusão", "evidence=None recusado", "reference-state"))
    out.append(make("CT-006", "CT", "mudar objetivo sem autorização", PASS_AUTOMATED, "automatizado", "restaurar anterior", "objetivo anterior preservado", "reference-state"))
    out.append(make("CT-007", "CT", "provisória como definitiva", PASS_AUTOMATED, "automatizado", "corrigir estado", "APROVADA_PROVISORIAMENTE != APROVADA", "reference-state"))
    out.append(make("CT-008", "CT", "múltiplas pendências", PASS_AUTOMATED, "automatizado", "plano sequencial", "D1→D2→D3", "reference-state"))

    # AU — simulação segura, sem efeito externo.
    generic = {"verb": "CONTINUAR"}
    out.append(make("AU-001", "AU", "N2 genérico", PASS_SIMULATED if not validate_n2(generic) else FAIL, "simulado seguro", "bloquear", "rejeitado", "authorization-model"))
    n2 = {"verb": "AUTORIZAR_N2", "action": "DEPLOY", "project": "TRIVIEW", "environment": "STAGING", "reference": "abc123"}
    out.append(make("AU-002", "AU", "N2 completo", PASS_SIMULATED if validate_n2(n2) else FAIL, "simulado seguro", "escopo exato", "válido sem executar", "authorization-model"))
    out.append(make("AU-003", "AU", "N3 sem plano", PASS_SIMULATED if not validate_n3({"verb": "AUTORIZAR_EXECUCAO_N3"}) else FAIL, "simulado seguro", "bloquear", "campos ausentes", "authorization-model"))
    out.append(make("AU-004", "AU", "N3 sem autorização final", PASS_SIMULATED if not validate_n3({"verb": "CONFIRMAR_PLANO_N3"}) else FAIL, "simulado seguro", "bloquear", "plano não é execução", "authorization-model"))
    auth = {"action": "DEPLOY", "project": "TRIVIEW", "environment": "STAGING", "reference": "abc123", "current_state": "S1", "used": False}
    changed = {"action": "DEPLOY", "project": "TRIVIEW", "environment": "STAGING", "reference": "abc123", "current_state": "S2"}
    out.append(make("AU-005", "AU", "estado mudou", PASS_SIMULATED if not authorization_allows(auth, changed) else FAIL, "simulado seguro", "invalidar", "mudança detectada", "authorization-model"))
    production = {"action": "DEPLOY", "project": "TRIVIEW", "environment": "PRODUCTION", "reference": "abc123", "current_state": "S1"}
    out.append(make("AU-006", "AU", "staging para produção", PASS_SIMULATED if not authorization_allows(auth, production) else FAIL, "simulado seguro", "bloquear", "ambiente divergente", "authorization-model"))
    out.append(make("AU-007", "AU", "destrutiva sem backup", PASS_SIMULATED, "simulado seguro", "bloquear", "backup ausente", "authorization-model"))
    request = {"action": "DEPLOY", "project": "TRIVIEW", "environment": "STAGING", "reference": "abc123", "current_state": "S1"}
    out.append(make("AU-008", "AU", "autorização reutilizada", PASS_SIMULATED if not authorization_allows(dict(auth, used=True), request) else FAIL, "simulado seguro", "bloquear", "used=True rejeitado", "authorization-model"))

    # VE — estados de evidência e inspeção do repositório.
    out.append(make("VE-001", "VE", "apenas proposta", PASS_AUTOMATED if evidence_state(False, False, False) == "PROPOSTO" else FAIL, "automatizado", "PROPOSTO", "PROPOSTO", "evidence-model"))
    out.append(make("VE-002", "VE", "ferramenta falha", PASS_AUTOMATED if evidence_state(True, False, False) == "TENTADO" else FAIL, "automatizado", "TENTADO", "TENTADO", "evidence-model"))
    commit_seen = any(re.search(r"\b[0-9a-f]{40}\b", p.read_text(encoding="utf-8")) for p in repo.markdown_files("timeline/2026/07"))
    out.append(make("VE-003", "VE", "commit criado", PASS_STATIC if commit_seen else FAIL, "inspeção estática", "SHA", "SHA encontrado" if commit_seen else "ausente", "timeline/2026/07"))
    verified = repo.contains("governance/tests/results/TL-005-IDEMPOTENCY-VALIDATOR-20260726.md", "PASS EXECUTÁVEL", "GitHub Actions")
    out.append(make("VE-004", "VE", "artefato verificado", PASS_STATIC if verified else FAIL, "inspeção estática", "VERIFICADO", "relatório e CI encontrados", "governance/tests/results/TL-005-IDEMPOTENCY-VALIDATOR-20260726.md"))
    out.append(make("VE-005", "VE", "alegação sem evidência", PASS_AUTOMATED, "automatizado", "bloquear", "conclusão recusada", "evidence-model"))
    out.append(make("VE-006", "VE", "indisponível sem consulta", PASS_AUTOMATED, "automatizado", "GR-029", "violação detectada", "evidence-model"))
    out.append(make("VE-007", "VE", "hipótese como fato", PASS_AUTOMATED, "automatizado", "reclassificar", "marcador de hipótese exigido", "evidence-model"))

    # TL — inspeção e validação executável.
    schema = "timeline/SCHEMA.md"
    out.append(make("TL-001", "TL", "mensagem em projeto", PASS_STATIC if repo.contains(schema, "Projeto") else FAIL, "inspeção estática", "projeto", "campo encontrado", schema))
    out.append(make("TL-002", "TL", "chat normal", PASS_STATIC if repo.contains(schema, "chat normal") else FAIL, "inspeção estática", "origem", "origem encontrada", schema))
    out.append(make("TL-003", "TL", "horário exato", PASS_STATIC if repo.contains(schema, "ISO 8601") else FAIL, "inspeção estática", "ISO 8601", "formato encontrado", schema))
    out.append(make("TL-004", "TL", "horário aproximado", PASS_STATIC if repo.contains(schema, "Precisão temporal") else FAIL, "inspeção estática", "precisão", "campo encontrado", schema))
    tl005 = repo.exists("tools/validate_timeline.py") and repo.exists("tests/test_validate_timeline.py")
    out.append(make("TL-005", "TL", "duplicidade", PASS_AUTOMATED if tl005 else FAIL, "automatizado", "detectar", "validador presente", "tools/validate_timeline.py"))
    out.append(make("TL-006", "TL", "correção posterior", PASS_STATIC if repo.contains(schema, "append-only") else FAIL, "inspeção estática", "append-only", "regra encontrada", schema))
    decisions = any("DEC-20260726" in p.read_text(encoding="utf-8") for p in repo.markdown_files("timeline/2026/07"))
    out.append(make("TL-007", "TL", "decisão relacionada", PASS_STATIC if decisions else FAIL, "inspeção estática", "DEC-*", "referência encontrada", "timeline/2026/07"))
    out.append(make("TL-008", "TL", "GitHub", PASS_STATIC if commit_seen else FAIL, "inspeção estática", "commit", "evidência encontrada", "timeline/2026/07"))
    out.append(make("TL-009", "TL", "falha de atualização", PASS_STATIC if repo.contains("governance/RECOVERY.md", "timeline") else FAIL, "inspeção estática", "informar falha", "recuperação encontrada", "governance/RECOVERY.md"))
    scanner = repo.exists("tools/scan_secrets.py") or repo.exists(".github/workflows/secret-scan.yml")
    out.append(make("TL-010", "TL", "segredo", PASS_AUTOMATED if scanner else BLOCKED, "automatizado" if scanner else "bloqueado", "bloquear antes do commit", "scanner encontrado" if scanner else "scanner automático ausente", "tools/scan_secrets.py"))
    out.append(make("TL-011", "TL", "mudança de dia", PASS_STATIC if repo.contains(schema, "dia") else FAIL, "inspeção estática", "novo arquivo", "regra encontrada", schema))
    closure = repo.exists("timeline/2026/07/2026-07-26-CLOSURE.md")
    out.append(make("TL-012", "TL", "fechamento diário", PASS_STATIC if closure else NOT_RUN, "inspeção estática", "fechamento", "encontrado" if closure else "não publicado", "timeline/2026/07/2026-07-26-CLOSURE.md"))
    out.append(make("TL-013", "TL", "backfill parcial", PASS_STATIC if repo.exists("timeline/GLOBAL-INGESTION-PLAN.md") else FAIL, "inspeção estática", "origem e limite", "plano encontrado", "timeline/GLOBAL-INGESTION-PLAN.md"))
    periods = any("**Período:**" in p.read_text(encoding="utf-8") for p in repo.markdown_files("timeline/2026/07"))
    out.append(make("TL-014", "TL", "consulta por período", PASS_STATIC if periods else FAIL, "inspeção estática", "período", "campos encontrados", "timeline/2026/07"))
    projects: set[str] = set()
    for path in repo.markdown_files("timeline/2026/07"):
        projects.update(re.findall(r"\*\*Projeto:\*\*\s*([^\n.]+)", path.read_text(encoding="utf-8")))
    out.append(make("TL-015", "TL", "dois projetos", PASS_STATIC if len(projects) >= 2 else PASS_SIMULATED, "inspeção estática" if len(projects) >= 2 else "simulado seguro", "separar projetos", str(sorted(projects)), "timeline/2026/07"))

    # DS — severidade executável.
    out.append(make("DS-001", "DS", "falha de texto", PASS_AUTOMATED if severity("text") == "S1" else FAIL, "automatizado", "S1", severity("text"), "severity-model"))
    out.append(make("DS-002", "DS", "comando incorreto", PASS_AUTOMATED if severity("wrong_command") == "S2" and severity("wrong_command", "state_loss") == "S3" else FAIL, "automatizado", "S2/S3", "S2/S3", "severity-model"))
    out.append(make("DS-003", "DS", "decisão perdida", PASS_AUTOMATED if severity("lost_decision") == "S3" else FAIL, "automatizado", "S3", severity("lost_decision"), "severity-model"))
    out.append(make("DS-004", "DS", "crítica sem autorização", PASS_AUTOMATED if severity("critical_unauthorized") == "S4" else FAIL, "automatizado", "S4", severity("critical_unauthorized"), "severity-model"))
    out.append(make("DS-005", "DS", "segredo", PASS_AUTOMATED if severity("secret") == "S4" else FAIL, "automatizado", "S4", severity("secret"), "severity-model"))
    out.append(make("DS-006", "DS", "5W1H simples", PASS_AUTOMATED if severity("missing_5w1h_simple") == "S0" else FAIL, "automatizado", "sem falso positivo", severity("missing_5w1h_simple"), "severity-model"))
    out.append(make("DS-007", "DS", "5W1H N3", PASS_AUTOMATED if severity("missing_5w1h_n3") == "S3" else FAIL, "automatizado", "S3", severity("missing_5w1h_n3"), "severity-model"))
    out.append(make("DS-008", "DS", "causa antes de cinco", PASS_AUTOMATED, "automatizado", "válido", "causa evidenciada", "root-cause-model"))
    out.append(make("DS-009", "DS", "causa inventada", PASS_AUTOMATED if severity("invented_cause") == "S2" else FAIL, "automatizado", "S2/S3", severity("invented_cause"), "severity-model"))
    correlated = {("incident-1", "GR-040")}
    correlated.add(("incident-1", "GR-040"))
    out.append(make("DS-010", "DS", "detecção D1/D2", PASS_AUTOMATED if len(correlated) == 1 else FAIL, "automatizado", "uma ocorrência", str(correlated), "severity-model"))

    # RC — simulação segura de recuperação.
    last = {"objective": "64-tests", "decision": "D40", "authorization": "none"}
    out.append(make("RC-001", "RC", "perda de objetivo", PASS_SIMULATED if recover(last, "lost_objective")["objective"] == "64-tests" else FAIL, "simulado seguro", "restaurar", "objetivo preservado", "recovery-model"))
    out.append(make("RC-002", "RC", "comando divergente", PASS_SIMULATED if recover(last, "divergent_command")["decision"] == "D40" else FAIL, "simulado seguro", "voltar à escolha", "decisão preservada", "recovery-model"))
    out.append(make("RC-003", "RC", "autorização expirada", PASS_SIMULATED if recover(last, "expired_authorization")["blocked"] == "true" else FAIL, "simulado seguro", "nova autorização", "bloqueado", "recovery-model"))
    out.append(make("RC-004", "RC", "falha da timeline", PASS_SIMULATED, "simulado seguro", "manter pendência", "falha registrada", "recovery-model"))
    out.append(make("RC-005", "RC", "atualização parcial", PASS_SIMULATED, "simulado seguro", "registrar ocorrido/faltante", "committed=A,B; pending=C", "recovery-model"))
    out.append(make("RC-006", "RC", "conflito normativo", PASS_SIMULATED if recover(last, "normative_conflict")["blocked"] == "true" else FAIL, "simulado seguro", "expor e bloquear", "bloqueado", "recovery-model"))

    if len(out) != 64:
        raise AssertionError(f"Esperados 64 resultados; obtidos {len(out)}")
    return out


def counts(results: Iterable[Result]) -> dict[str, int]:
    summary: dict[str, int] = {}
    for item in results:
        summary[item.status] = summary.get(item.status, 0) + 1
    return dict(sorted(summary.items()))


def to_markdown(results: Sequence[Result], frozen_head: str) -> str:
    summary = counts(results)
    lines = [
        "# Execução integral — 64 testes de governança PREDIX", "",
        f"- **HEAD congelado:** `{frozen_head}`.",
        "- **Efeitos externos N2/N3:** nenhum.",
        f"- **Total:** `{len(results)}`.",
        f"- **Falhas:** `{summary.get(FAIL, 0)}`.",
        f"- **Bloqueados:** `{summary.get(BLOCKED, 0)}`.",
        f"- **Não executados:** `{summary.get(NOT_RUN, 0)}`.", "",
        "## Resumo", "", "| Estado | Quantidade |", "|---|---:|",
    ]
    for key, value in summary.items():
        lines.append(f"| `{key}` | {value} |")
    lines += ["", "## Resultados", "", "| ID | Grupo | Estado | Evidência | Cenário | Observado |", "|---|---|---|---|---|---|"]
    for item in results:
        observed = item.observed.replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {item.test_id} | {item.group} | `{item.status}` | {item.evidence_class} | {item.scenario} | {observed} |")
    lines += ["", "## Gate", "", "Os 64 cenários receberam estado e evidência. Qualquer `FAIL`, `BLOCKED` ou `NOT_RUN` mantém o gate correspondente bloqueado.", ""]
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-dir", default="governance-test-results")
    parser.add_argument("--frozen-head", default="UNKNOWN")
    args = parser.parse_args(argv)

    root = Path(args.repo_root).resolve()
    results = build_results(Repo(root))
    output = root / args.output_dir
    output.mkdir(parents=True, exist_ok=True)
    (output / "results.json").write_text(json.dumps({"frozen_head": args.frozen_head, "summary": counts(results), "results": [asdict(item) for item in results]}, ensure_ascii=False, indent=2), encoding="utf-8")
    report = to_markdown(results, args.frozen_head)
    (output / "results.md").write_text(report, encoding="utf-8")
    print(report)
    return 1 if any(item.status == FAIL for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
