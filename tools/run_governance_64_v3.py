#!/usr/bin/env python3
"""Executor R5 da matriz de 64 testes de governança.

Mantém os 64 cenários da R4 e converte TL-010 e TL-012 em verificações
executáveis sobre o scanner de segredos e o DAILY-CLOSE publicado.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, replace
from pathlib import Path
from typing import Sequence

from run_governance_64 import (
    BLOCKED,
    FAIL,
    NOT_RUN,
    PASS_AUTOMATED,
    PASS_STATIC,
    Repo,
    counts,
    to_markdown,
)
from run_governance_64_v2 import corrected_results
from scan_secrets import scan_paths

CLOSURE_PATH = "timeline/2026/07/2026-07-26-CLOSURE.md"
CLOSURE_MARKERS = (
    "DAILY-CLOSE",
    "Itens executados ou verificados",
    "Pendências ativas",
    "Bloqueios e condições de retomada",
    "Divergências reconciliadas e remanescentes",
    "Primeira ação recomendada",
    "Cobertura e lacunas do dia",
)


def r5_results(repo: Repo):
    results = corrected_results(repo)
    updated = []

    for item in results:
        if item.test_id == "TL-010":
            scanner_present = repo.exists("tools/scan_secrets.py") and repo.exists("tests/test_scan_secrets.py")
            findings = scan_paths(["."], root=repo.root) if scanner_present else []
            ok = scanner_present and not findings
            observed = (
                "Scanner executado no repositório sem segredos potenciais."
                if ok
                else (
                    f"Scanner encontrou {len(findings)} ocorrência(s) potencial(is)."
                    if scanner_present
                    else "Scanner ou testes de regressão ausentes."
                )
            )
            item = replace(
                item,
                status=PASS_AUTOMATED if ok else FAIL,
                evidence_class="automatizado",
                observed=observed,
                evidence=("tools/scan_secrets.py", "tests/test_scan_secrets.py"),
            )
        elif item.test_id == "TL-012":
            closure_exists = repo.exists(CLOSURE_PATH)
            closure_complete = closure_exists and repo.contains(CLOSURE_PATH, *CLOSURE_MARKERS)
            item = replace(
                item,
                status=PASS_STATIC if closure_complete else FAIL,
                evidence_class="inspeção estática",
                observed="DAILY-CLOSE publicado com os seis blocos mínimos." if closure_complete else "DAILY-CLOSE ausente ou incompleto.",
                evidence=(CLOSURE_PATH,),
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
    results = r5_results(Repo(root))
    output = root / args.output_dir
    output.mkdir(parents=True, exist_ok=True)
    (output / "results.json").write_text(
        json.dumps(
            {
                "runner": "v3-r5",
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
