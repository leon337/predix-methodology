from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.scan_secrets import scan_paths, scan_text


class SecretScannerTests(unittest.TestCase):
    def test_safe_document_has_no_finding(self) -> None:
        text = "TOKEN=<REDACTED>\nOPENAI_API_KEY=${OPENAI_API_KEY}\npassword=changeme\n"
        self.assertEqual(scan_text(text, "safe.md"), [])

    def test_detects_github_token_without_exposing_value(self) -> None:
        value = "ghp_" + "A1b2" * 9
        findings = scan_text(f"credential={value}\n", "config.txt")
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].rule, "github-token")
        self.assertNotIn(value, findings[0].preview)

    def test_detects_high_entropy_generic_assignment(self) -> None:
        value = "qA7!zP9#mK2@vN8$xR4%tY6&"
        findings = scan_text("api_key=" + value, "settings.env")
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].rule, "generic-secret-assignment")

    def test_allow_marker_suppresses_intentional_fixture(self) -> None:
        value = "sk-" + "Z9y8X7w6V5u4T3s2R1q0"
        findings = scan_text("token=" + value + "  # secret-scan: allow", "fixture.txt")
        self.assertEqual(findings, [])

    def test_binary_file_is_skipped(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "image.bin").write_bytes(b"\x00" + b"ghp_" + b"A" * 36)
            self.assertEqual(scan_paths(["."], root=root), [])

    def test_directory_scan_reports_relative_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            value = "github_pat_" + "Ab1_" * 12
            (root / "bad.env").write_text("token=" + value, encoding="utf-8")
            findings = scan_paths(["."], root=root)
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].path, "bad.env")


if __name__ == "__main__":
    unittest.main()
