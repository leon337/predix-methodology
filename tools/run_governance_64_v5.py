#!/usr/bin/env python3
"""Executor R7 da matriz de 64 testes de governança.

A evidência manual do Fluxo Assistido é resolvida por eventos estruturados e
ordenados temporalmente. O evento mais recente do mesmo cenário prevalece:
PASS_MANUAL libera o cenário; REGRESSION força NOT_RUN até novo reteste.
O runner também valida o TL-005 atual e o esquema Markdown v0.3 diretamente.
Nenhum efeito externo N2/N3 é executado.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, replace
from datetime import datetime
from pathlib import Path
from typing import Iterable, Sequence

from run_governance_64 import (
    BLOCKED,
    FAIL,
    NOT_RUN,
    PASS_AUTOMATED,
    PASS_MANUAL,
    PASS_STATIC,
    Repo,
    counts,
    to_markdown,
)
from run_governance_64_v3 import r5_results
from validate_timeline import validate as validate_timeline

EVIDENCE_LOG = "governance/evidence/assisted-flow-events.jsonl"
SUPPORTED_OUTCOMES = {"PASS_MANUAL", "REGRESSION"}


@dataclass(frozen=True)
class EvidenceEvent:
    scenario_id: str
    timestamp: datetime
    outcome: str
    evidence: str
    note: str


def parse_event(payload: dict[str, object], line_number: int) -> EvidenceEvent:
    required = {"scenario_id", "timestamp", "outcome", "evidence", "note"}
    missing = sorted(required - payload.keys())
    if missing:
        raise ValueError(f"Linha {line_number}: campos ausentes: {', '.join(missing)}")

    outcome = str(payload["outcome"])
    if outcome not in SUPPORTED_OUTCOMES:
        raise ValueError(f"Linha {line_number}: outcome não suportado: {outcome}")

    timestamp = datetime.fromisoformat(str(payload["timestamp"]))
    if timestamp.tzinfo is None:
        raise ValueError(f"Linha {line_number}: timestamp deve incluir fuso horário")

    return EvidenceEvent(
        scenario_id=str(payload["scenario_id"]),
        timestamp=timestamp,
        outcome=outcome,
        evidence=str(payload["evidence"]),
        note=str(payload["note"]),
    )


def load_evidence_events(path: Path) -> list[EvidenceEvent]:
    events: list[EvidenceEvent] = []
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        payload = json.loads(line)
        if not isinstance(payload, dict):
            raise ValueError(f"Linha {line_number}: evento deve ser objeto JSON")
        events.append(parse_event(payload, line_number))
    return events


def latest_event(events: Iterable[EvidenceEvent], scenario_id: str) -> EvidenceEvent | None:
    matching = [event for event in events if event.scenario_id == scenario_id]
    return max(matching, key=lambda event: event.timestamp) if matching else None


def apply_chronological_evidence(item, events: list[EvidenceEvent], evidence_path: str):
    event = latest_event(events, item.test_id)
    passed = event is not None and event.outcome == "PASS_MANUAL"
    if event is None:
        observed = "Nenhuma evidência cronológica estruturada foi encontrada."
        evidence = (evidence_path,)
    else:
        observed = (
            f"Último evento cronológico: {event.outcome} em {event.timestamp.isoformat()}. {event.note}"
        )
        evidence = (evidence_path, event.evidence)

    return replace(
        item,
        status=PASS_MANUAL if passed else NOT_RUN,
        evidence_class="manual/observado",
        observed=observed,
        evidence=evidence,
    )


def r7_results(repo: Repo):
    results = r5_results(repo)
    evidence_path = repo.root / EVIDENCE_LOG
    events = load_evidence_events(evidence_path) if evidence_path.exists() else []
    schema_path = "timeline/SCHEMA.md"
    schema = repo.text(schema_path) if repo.exists(schema_path) else ""
    timeline_report = validate_timeline([repo.root / "timeline"])
    updated = []

    for item in results:
        if item.test_id in {"FA-008", "FA-009"}:
            item = apply_chronological_evidence(item, events, EVIDENCE_LOG)
        elif item.test_id == "TL-001":
            ok = "- **Projeto:**" in schema and "timeline/**/events/*.md" in schema
            item = replace(
                item,
                status=PASS_STATIC if ok else FAIL,
                evidence_class="inspeção estática",
                observed=(
                    "Esquema Markdown contém campo Projeto e limite canônico de eventos."
                    if ok
                    else "Esquema Markdown não contém campo Projeto ou limite canônico."
                ),
                evidence=(schema_path,),
            )
        elif item.test_id == "TL-005":
            item = replace(
                item,
                status=PASS_AUTOMATED if timeline_report.ok else FAIL,
                evidence_class="automatizado",
                observed=(
                    f"TL-005 executado: {timeline_report.structured_event_files} eventos estruturados, "
                    f"{timeline_report.error_count} erros."
                ),
                evidence=("tools/validate_timeline.py", "tests/test_validate_timeline.py"),
            )
        updated.append(item)

    if len(updated) != 64:
        raise AssertionError(f"Esperados 64 resultados; obtidos {len(updated)}")
    return updated


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-dir", default="governance-test-results")
    parser.add_argument("--frozen-head", default="UNKNOWN")
    args = parser.parse_args(argv)

    root = Path(args.repo_root).resolve()
    results = r7_results(Repo(root))
    output = root / args.output_dir
    output.mkdir(parents=True, exist_ok=True)
    (output / "results.json").write_text(
        json.dumps(
            {
                "runner": "v5-r7-chronological-evidence",
                "frozen_head": args.frozen_head,
                "summary": counts(results),
                "results": [asdict(item) for item in results],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    report = to_markdown(results, args.frozen_head)
    (output / "results.md").write_text(report, encoding="utf-8")
    print(report)

    gate_failures = {FAIL, BLOCKED, NOT_RUN}
    return 1 if any(item.status in gate_failures for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
