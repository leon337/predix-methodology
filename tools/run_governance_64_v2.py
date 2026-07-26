#!/usr/bin/env python3
"""Executor R2 da matriz de 64 testes.

Corrige falsos negativos do primeiro runner sem alterar os cenários:
- TL-001 aceita o campo YAML `projeto:`;
- TL-002 aceita a taxonomia `chat-normal`;
- TL-003 valida um timestamp ISO 8601 real, sem exigir a frase literal;
- VE-004 usa a evidência TL-005 sincronizada na branch integrada.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, replace
from pathlib import Path
from typing import Sequence

from run_governance_64 import (
    FAIL,
    PASS_STATIC,
    Repo,
    build_results,
    counts,
    to_markdown,
)


def corrected_results(repo: Repo):
    results = build_results(repo)
    schema = repo.text("timeline/SCHEMA.md") if repo.exists("timeline/SCHEMA.md") else ""
    report = "governance/tests/results/TL-005-IDEMPOTENCY-VALIDATOR-20260726.md"
    corrected = []

    for item in results:
        if item.test_id == "TL-001":
            ok = bool(re.search(r"(?mi)^\s*projeto:\s*", schema))
            item = replace(
                item,
                status=PASS_STATIC if ok else FAIL,
                observed="Campo YAML `projeto:` encontrado." if ok else "Campo de projeto ausente.",
                evidence=("timeline/SCHEMA.md",),
            )
        elif item.test_id == "TL-002":
            ok = "chat-normal" in schema or "chat normal" in schema.lower()
            item = replace(
                item,
                status=PASS_STATIC if ok else FAIL,
                observed="Taxonomia de origem `chat-normal` encontrada." if ok else "Origem de chat normal ausente.",
                evidence=("timeline/SCHEMA.md",),
            )
        elif item.test_id == "TL-003":
            ok = bool(re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}", schema))
            item = replace(
                item,
                status=PASS_STATIC if ok else FAIL,
                observed="Exemplo de timestamp ISO 8601 com fuso encontrado." if ok else "Timestamp ISO 8601 ausente.",
                evidence=("timeline/SCHEMA.md",),
            )
        elif item.test_id == "VE-004":
            ok = repo.contains(report, "PASS EXECUTÁVEL", "success")
            item = replace(
                item,
                status=PASS_STATIC if ok else FAIL,
                observed="Relatório TL-005 e conclusão de CI encontrados." if ok else "Evidência TL-005 incompleta.",
                evidence=(report,),
            )
        corrected.append(item)

    if len(corrected) != 64:
        raise AssertionError(f"Esperados 64 resultados; obtidos {len(corrected)}")
    return corrected


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-dir", default="governance-test-results")
    parser.add_argument("--frozen-head", default="UNKNOWN")
    args = parser.parse_args(argv)

    root = Path(args.repo_root).resolve()
    results = corrected_results(Repo(root))
    output = root / args.output_dir
    output.mkdir(parents=True, exist_ok=True)
    (output / "results.json").write_text(
        json.dumps(
            {
                "runner": "v2",
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
    return 1 if any(item.status == FAIL for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
