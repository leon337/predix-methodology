from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.validate_timeline import validate  # noqa: E402


ENTRY = """### 15:00:00 — Evento\n\n- **ID:** `{id}`.\n- **Chave de idempotência:** `{key}`.\n"""


class TimelineValidatorTests(unittest.TestCase):
    def write(self, root: Path, name: str, content: str) -> Path:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_unique_ids_and_keys_pass(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(
                root,
                "timeline/2026/07/2026-07-26.md",
                ENTRY.format(
                    id="TL-20260726-150000-001",
                    key="IDEMP-20260726-PROJETO-FABRICA-SOFTWARES-001-EVENTO",
                )
                + ENTRY.format(
                    id="TL-20260726-150001-002",
                    key="IDEMP-20260726-PROJETO-FABRICA-SOFTWARES-002-EVENTO",
                ),
            )
            report = validate([root / "timeline"])
            self.assertTrue(report.ok)
            self.assertEqual(report.ids_found, 2)
            self.assertEqual(report.idempotency_keys_found, 2)

    def test_duplicate_id_fails(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            repeated = "TL-20260726-150000-001"
            self.write(
                root,
                "timeline/a.md",
                ENTRY.format(id=repeated, key="IDEMP-20260726-PROJETO-A-001-EVENTO"),
            )
            self.write(
                root,
                "timeline/b.md",
                ENTRY.format(id=repeated, key="IDEMP-20260726-PROJETO-B-002-EVENTO"),
            )
            report = validate([root / "timeline"])
            self.assertFalse(report.ok)
            self.assertIn("TL005-DUPLICATE-ID", {item.code for item in report.findings})

    def test_duplicate_idempotency_key_fails(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            repeated = "IDEMP-20260726-PROJETO-FABRICA-SOFTWARES-001-EVENTO"
            self.write(
                root,
                "timeline/a.md",
                ENTRY.format(id="TL-20260726-150000-001", key=repeated),
            )
            self.write(
                root,
                "timeline/b.md",
                ENTRY.format(id="TL-20260726-150001-002", key=repeated),
            )
            report = validate([root / "timeline"])
            self.assertFalse(report.ok)
            self.assertIn("TL005-DUPLICATE-KEY", {item.code for item in report.findings})

    def test_legacy_entry_without_structured_fields_is_ignored(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "timeline/legacy.md", "### 13:03 — Entrada legada\n\n- **Estado:** histórico.\n")
            report = validate([root / "timeline"])
            self.assertTrue(report.ok)
            self.assertEqual(report.ids_found, 0)
            self.assertEqual(report.idempotency_keys_found, 0)

    def test_invalid_structured_values_fail(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(
                root,
                "timeline/invalid.md",
                "### Entrada\n\n- **ID:** `TL-20260726-1500-1`.\n"
                "- **Chave de idempotência:** `IDEMP-2026-X`.\n",
            )
            report = validate([root / "timeline"])
            self.assertFalse(report.ok)
            codes = {item.code for item in report.findings}
            self.assertIn("TL005-INVALID-ID", codes)
            self.assertIn("TL005-INVALID-KEY", codes)


if __name__ == "__main__":
    unittest.main()
