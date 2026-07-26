#!/usr/bin/env python3
"""Scanner determinístico de segredos para o repositório PREDIX.

O scanner não imprime o valor encontrado. Cada ocorrência é representada por regra,
arquivo, linha, impressão digital curta e prévia mascarada.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

MAX_FILE_BYTES = 2 * 1024 * 1024
ALLOW_MARKER = "secret-scan: allow"
DEFAULT_EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    "governance-test-results",
    "dist",
    "build",
}
DEFAULT_EXCLUDED_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf",
    ".zip", ".gz", ".tar", ".7z", ".rar", ".woff", ".woff2",
    ".ttf", ".eot", ".mp3", ".mp4", ".mov", ".avi", ".sqlite",
    ".db", ".pyc",
}


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    rule: str
    fingerprint: str
    preview: str


@dataclass(frozen=True)
class Rule:
    name: str
    regex: re.Pattern[str]
    group: int = 0


RULES = (
    Rule("private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    Rule("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,255}\b")),
    Rule("github-fine-grained-token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,255}\b")),
    Rule("openai-token", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,255}\b")),
    Rule("aws-access-key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    Rule("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,255}\b")),
    Rule("stripe-live-secret", re.compile(r"\bsk_live_[A-Za-z0-9]{20,255}\b")),
    Rule("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")),
)

GENERIC_ASSIGNMENT = re.compile(
    r"(?i)\b(?:password|passwd|secret|token|api[_-]?key|client[_-]?secret|private[_-]?key)\b"
    r"\s*(?:=|:)\s*[\"']?([^\s\"'`,;#]{12,})"
)

PLACEHOLDER_PARTS = (
    "example", "placeholder", "changeme", "change_me", "redacted", "masked",
    "dummy", "sample", "your_", "your-", "replace", "none", "null", "xxxx",
    "<", ">", "${", "{{", "***", "abc123",
)


def shannon_entropy(value: str) -> float:
    if not value:
        return 0.0
    counts = {char: value.count(char) for char in set(value)}
    size = len(value)
    return -sum((count / size) * math.log2(count / size) for count in counts.values())


def is_placeholder(value: str) -> bool:
    lowered = value.lower()
    return any(part in lowered for part in PLACEHOLDER_PARTS)


def looks_like_generic_secret(value: str) -> bool:
    if len(value) < 12 or is_placeholder(value):
        return False
    classes = sum(
        bool(re.search(pattern, value))
        for pattern in (r"[a-z]", r"[A-Z]", r"[0-9]", r"[^A-Za-z0-9]")
    )
    return (len(value) >= 24 and classes >= 2) or (shannon_entropy(value) >= 3.2 and classes >= 3)


def redact(value: str) -> str:
    if len(value) <= 8:
        return "***"
    return f"{value[:3]}…{value[-3:]}"


def fingerprint(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8", errors="replace")).hexdigest()[:12]


def is_binary(path: Path) -> bool:
    try:
        sample = path.read_bytes()[:4096]
    except OSError:
        return True
    return b"\x00" in sample


def should_skip(path: Path, root: Path, extra_excludes: set[str]) -> bool:
    try:
        relative = path.relative_to(root)
    except ValueError:
        relative = path
    if any(part in DEFAULT_EXCLUDED_DIRS or part in extra_excludes for part in relative.parts[:-1]):
        return True
    if path.suffix.lower() in DEFAULT_EXCLUDED_SUFFIXES:
        return True
    try:
        return not path.is_file() or path.stat().st_size > MAX_FILE_BYTES or is_binary(path)
    except OSError:
        return True


def iter_files(paths: Sequence[Path], root: Path, extra_excludes: set[str]) -> Iterable[Path]:
    seen: set[Path] = set()
    for supplied in paths:
        candidate = supplied if supplied.is_absolute() else root / supplied
        if candidate.is_file():
            resolved = candidate.resolve()
            if resolved not in seen and not should_skip(resolved, root, extra_excludes):
                seen.add(resolved)
                yield resolved
        elif candidate.is_dir():
            for path in sorted(candidate.rglob("*")):
                resolved = path.resolve()
                if resolved not in seen and not should_skip(resolved, root, extra_excludes):
                    seen.add(resolved)
                    yield resolved


def scan_text(text: str, display_path: str) -> list[Finding]:
    findings: list[Finding] = []
    dedupe: set[tuple[int, str, str]] = set()
    for line_number, line in enumerate(text.splitlines(), start=1):
        if ALLOW_MARKER in line.lower():
            continue
        for rule in RULES:
            for match in rule.regex.finditer(line):
                value = match.group(rule.group)
                key = (line_number, rule.name, fingerprint(value))
                if key not in dedupe:
                    dedupe.add(key)
                    findings.append(Finding(display_path, line_number, rule.name, key[2], redact(value)))
        for match in GENERIC_ASSIGNMENT.finditer(line):
            value = match.group(1).rstrip(")]}")
            if looks_like_generic_secret(value):
                key = (line_number, "generic-secret-assignment", fingerprint(value))
                if key not in dedupe:
                    dedupe.add(key)
                    findings.append(Finding(display_path, line_number, key[1], key[2], redact(value)))
    return findings


def scan_paths(paths: Sequence[str | Path], root: str | Path = ".", excludes: Sequence[str] = ()) -> list[Finding]:
    root_path = Path(root).resolve()
    supplied = [Path(path) for path in paths] or [Path(".")]
    findings: list[Finding] = []
    for path in iter_files(supplied, root_path, set(excludes)):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        try:
            display = path.relative_to(root_path).as_posix()
        except ValueError:
            display = path.as_posix()
        findings.extend(scan_text(text, display))
    return sorted(findings, key=lambda item: (item.path, item.line, item.rule))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=["."], help="Arquivos ou diretórios para examinar")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--exclude", action="append", default=[])
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    findings = scan_paths(args.paths, root=args.repo_root, excludes=args.exclude)
    if args.format == "json":
        print(json.dumps({"findings": [asdict(item) for item in findings], "count": len(findings)}, ensure_ascii=False, indent=2))
    elif findings:
        for item in findings:
            print(f"{item.path}:{item.line}: {item.rule} [{item.fingerprint}] {item.preview}")
        print(f"Segredos potenciais encontrados: {len(findings)}", file=sys.stderr)
    else:
        print("Nenhum segredo potencial encontrado.")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
