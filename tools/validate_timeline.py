#!/usr/bin/env python3
"""Validate PREDIX timeline identifiers and idempotency keys.

Policy:
- canonical structured events live under ``timeline/**/events/*.md``;
- each canonical event file must contain exactly one Markdown ``ID`` field and
  exactly one Markdown ``Chave de idempotência`` field;
- overview, index and historical files outside ``events`` are legacy/support
  documents and may omit those fields;
- YAML is not an accepted persisted event format in v0.3.

The validator is dependency-free so it can run locally and in GitHub Actions.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

ID_RE = re.compile(r"\bTL-(?P<date>\d{8})-(?P<time>\d{6})-(?P<seq>\d{3})\b")
KEY_RE = re.compile(r"\bIDEMP-(?P<date>\d{8})-(?P<body>[A-Z0-9][A-Z0-9-]{5,})\b")
FIELD_ID_RE = re.compile(r"^\s*-\s*\*\*ID:\*\*\s*`?(?P<value>TL-[^`\s.]+)`?\.?\s*$", re.MULTILINE)
FIELD_KEY_RE = re.compile(
    r"^\s*-\s*\*\*Chave de idempotência:\*\*\s*`?(?P<value>IDEMP-[^`\s.]+)`?\.?\s*$",
    re.MULTILINE,
)
HEADING_RE = re.compile(r"^###\s+", re.MULTILINE)


@dataclass(frozen=True)
class Occurrence:
    value: str
    path: str
    line: int
    entry_heading: str | None


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    message: str
    value: str | None
    occurrences: tuple[Occurrence, ...]


@dataclass(frozen=True)
class ValidationReport:
    files_scanned: int
    structured_event_files: int
    legacy_or_support_files: int
    ids_found: int
    idempotency_keys_found: int
    findings: tuple[Finding, ...]

    @property
    def error_count(self) -> int:
        return sum(1 for item in self.findings if item.severity == "error")

    @property
    def warning_count(self) -> int:
        return sum(1 for item in self.findings if item.severity == "warning")

    @property
    def ok(self) -> bool:
        return self.error_count == 0


def _line_number(text: str, start: int) -> int:
    return text.count("\n", 0, start) + 1


def _entry_heading(text: str, start: int) -> str | None:
    heading: str | None = None
    for match in HEADING_RE.finditer(text, 0, start + 1):
        line_end = text.find("\n", match.start())
        if line_end == -1:
            line_end = len(text)
        heading = text[match.start():line_end].lstrip("# ").strip()
    return heading


def _collect(pattern: re.Pattern[str], text: str, path: Path) -> list[Occurrence]:
    result: list[Occurrence] = []
    for match in pattern.finditer(text):
        value = match.group("value")
        result.append(
            Occurrence(
                value=value,
                path=path.as_posix(),
                line=_line_number(text, match.start()),
                entry_heading=_entry_heading(text, match.start()),
            )
        )
    return result


def _is_structured_event_file(path: Path) -> bool:
    """Return True only for canonical event records under an events directory."""
    return path.suffix.lower() == ".md" and "events" in path.parts


def _file_occurrence(path: Path) -> Occurrence:
    return Occurrence(value="", path=path.as_posix(), line=1, entry_heading=None)


def _required_field_findings(
    path: Path,
    file_ids: list[Occurrence],
    file_keys: list[Occurrence],
) -> list[Finding]:
    findings: list[Finding] = []
    if not file_ids:
        findings.append(
            Finding(
                code="TL005-MISSING-ID",
                severity="error",
                message="Entrada estruturada nova sem campo Markdown obrigatório de ID.",
                value=None,
                occurrences=(_file_occurrence(path),),
            )
        )
    elif len(file_ids) > 1:
        findings.append(
            Finding(
                code="TL005-MULTIPLE-ID",
                severity="error",
                message="Arquivo de evento deve conter exatamente um campo de ID.",
                value=None,
                occurrences=tuple(file_ids),
            )
        )

    if not file_keys:
        findings.append(
            Finding(
                code="TL005-MISSING-KEY",
                severity="error",
                message="Entrada estruturada nova sem chave de idempotência Markdown obrigatória.",
                value=None,
                occurrences=(_file_occurrence(path),),
            )
        )
    elif len(file_keys) > 1:
        findings.append(
            Finding(
                code="TL005-MULTIPLE-KEY",
                severity="error",
                message="Arquivo de evento deve conter exatamente uma chave de idempotência.",
                value=None,
                occurrences=tuple(file_keys),
            )
        )
    return findings


def _duplicates(items: Iterable[Occurrence], code: str, label: str) -> list[Finding]:
    grouped: dict[str, list[Occurrence]] = {}
    for item in items:
        grouped.setdefault(item.value, []).append(item)
    findings: list[Finding] = []
    for value, occurrences in sorted(grouped.items()):
        if len(occurrences) > 1:
            findings.append(
                Finding(
                    code=code,
                    severity="error",
                    message=f"{label} duplicado em {len(occurrences)} ocorrências.",
                    value=value,
                    occurrences=tuple(occurrences),
                )
            )
    return findings


def _format_findings(
    occurrences: Iterable[Occurrence], full_pattern: re.Pattern[str], code: str, label: str
) -> list[Finding]:
    findings: list[Finding] = []
    for item in occurrences:
        if full_pattern.fullmatch(item.value) is None:
            findings.append(
                Finding(
                    code=code,
                    severity="error",
                    message=f"{label} fora do formato canônico.",
                    value=item.value,
                    occurrences=(item,),
                )
            )
    return findings


def discover_files(paths: Sequence[Path]) -> list[Path]:
    files: set[Path] = set()
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md":
            files.add(path)
        elif path.is_dir():
            files.update(p for p in path.rglob("*.md") if p.is_file())
    return sorted(files)


def validate(paths: Sequence[Path]) -> ValidationReport:
    files = discover_files(paths)
    ids: list[Occurrence] = []
    keys: list[Occurrence] = []
    findings: list[Finding] = []
    structured_count = 0

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            findings.append(
                Finding(
                    code="TL005-IO",
                    severity="error",
                    message=f"Não foi possível ler o arquivo: {exc}",
                    value=None,
                    occurrences=(Occurrence("", path.as_posix(), 0, None),),
                )
            )
            continue

        file_ids = _collect(FIELD_ID_RE, text, path)
        file_keys = _collect(FIELD_KEY_RE, text, path)
        ids.extend(file_ids)
        keys.extend(file_keys)

        if _is_structured_event_file(path):
            structured_count += 1
            findings.extend(_required_field_findings(path, file_ids, file_keys))

    findings.extend(_duplicates(ids, "TL005-DUPLICATE-ID", "ID de timeline"))
    findings.extend(_duplicates(keys, "TL005-DUPLICATE-KEY", "Chave de idempotência"))
    findings.extend(_format_findings(ids, ID_RE, "TL005-INVALID-ID", "ID de timeline"))
    findings.extend(_format_findings(keys, KEY_RE, "TL005-INVALID-KEY", "Chave de idempotência"))

    return ValidationReport(
        files_scanned=len(files),
        structured_event_files=structured_count,
        legacy_or_support_files=len(files) - structured_count,
        ids_found=len(ids),
        idempotency_keys_found=len(keys),
        findings=tuple(findings),
    )


def _to_json(report: ValidationReport) -> str:
    return json.dumps(
        {
            "ok": report.ok,
            "files_scanned": report.files_scanned,
            "structured_event_files": report.structured_event_files,
            "legacy_or_support_files": report.legacy_or_support_files,
            "ids_found": report.ids_found,
            "idempotency_keys_found": report.idempotency_keys_found,
            "error_count": report.error_count,
            "warning_count": report.warning_count,
            "findings": [asdict(item) for item in report.findings],
        },
        ensure_ascii=False,
        indent=2,
    )


def _to_text(report: ValidationReport) -> str:
    lines = [
        "TL-005 — Validação de idempotência da timeline",
        f"Arquivos: {report.files_scanned}",
        f"Eventos estruturados: {report.structured_event_files}",
        f"Legados/suporte: {report.legacy_or_support_files}",
        f"IDs: {report.ids_found}",
        f"Chaves: {report.idempotency_keys_found}",
        f"Erros: {report.error_count}",
        f"Avisos: {report.warning_count}",
        f"Resultado: {'PASS' if report.ok else 'FAIL'}",
    ]
    for finding in report.findings:
        lines.append(f"\n[{finding.severity.upper()}] {finding.code}: {finding.message}")
        if finding.value:
            lines.append(f"Valor: {finding.value}")
        for item in finding.occurrences:
            location = f"{item.path}:{item.line}"
            suffix = f" — {item.entry_heading}" if item.entry_heading else ""
            lines.append(f"- {location}{suffix}")
    return "\n".join(lines)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        default=["timeline"],
        help="Arquivos ou diretórios Markdown. Padrão: timeline",
    )
    parser.add_argument("--format", choices=("text", "json"), default="text")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    paths = [Path(item) for item in args.paths]
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        print(f"Caminho inexistente: {', '.join(missing)}", file=sys.stderr)
        return 2

    report = validate(paths)
    print(_to_json(report) if args.format == "json" else _to_text(report))
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
