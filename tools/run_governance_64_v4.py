#!/usr/bin/env python3
"""Executor R6 da matriz de 64 testes de governança.

Mantém a bateria R5 e invalida evidências manuais quando uma regressão posterior
não foi retestada. Nenhum efeito externo N2/N3 é executado.
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
    PASS_MANUAL,
    Repo,
    counts,
    to_markdown,
)
from run_governance_64_v3 import r5_results

FA_RECONCILIATION = "governance/tests/results/FA-REGRESSION-RECONCILIATION-20260726.md"
FA008_PASS_MARKER = "FA-008=PASS_MANUAL_RECUPERADO"
FA009_PASS_MARKER = "FA-009_MULTIGROUP=PASS_MANUAL"


def r6_results(repo: Repo):
    results = r5_results(repo)
    reconciliation_exists = repo.exists(FA_RECONCILIATION)
    reconciliation_text = repo.text(FA_RECONCILIATION) if reconciliation_exists else ""
    updated = []

    for item in results:
        if item.test_id == "FA-008":
            passed = FA008_PASS_MARKER in reconciliation_text
            item = replace(
                item,
                status=PASS_MANUAL if passed else NOT_RUN,
                evidence_class="manual/observado",
                observed=(
                    "Regressão reconciliada; próximo painel e comando de retorno observados."
                    if passed
                    else "Regressão posterior sem evidência manual de recuperação."
                ),
                evidence=(FA_RECONCILIATION,),
            )
        elif item.test_id == "FA-009":
            passed = FA009_PASS_MARKER in reconciliation_text
            item = replace(
                item,
                status=PASS_MANUAL if passed else NOT_RUN,
                evidence_class="manual/observado",
                observed=(
                    "Reteste multigrupo confirmou recomendação por grupo sem preseleção."
                    if passed
                    else "Reteste manual multigrupo ainda não executado."
                ),
                evidence=(FA_RECONCILIATION,),
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
    results = r6_results(Repo(root))
    output = root / args.output_dir
    output.mkdir(parents=True, exist_ok=True)
    (output / "results.json").write_text(
        json.dumps(
            {
                "runner": "v4-r6-fa-regression-aware",
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
