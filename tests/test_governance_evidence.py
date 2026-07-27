from datetime import datetime
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

from run_governance_64 import NOT_RUN, PASS_MANUAL, Result  # noqa: E402
from run_governance_64_v5 import EvidenceEvent, apply_chronological_evidence, latest_event  # noqa: E402


class GovernanceEvidenceChronologyTests(unittest.TestCase):
    def base_result(self) -> Result:
        return Result(
            test_id="FA-009",
            group="FA",
            scenario="Recomendação por grupo",
            status=PASS_MANUAL,
            evidence_class="manual/observado",
            expected="Recomendação por grupo sem preseleção.",
            observed="Evidência anterior.",
            evidence=("old.md",),
        )

    def event(self, timestamp: str, outcome: str) -> EvidenceEvent:
        return EvidenceEvent(
            scenario_id="FA-009",
            timestamp=datetime.fromisoformat(timestamp),
            outcome=outcome,
            evidence="evidence.md",
            note=f"Evento {outcome}",
        )

    def test_latest_pass_keeps_manual_pass(self) -> None:
        events = [
            self.event("2026-07-26T17:40:53-03:00", "REGRESSION"),
            self.event("2026-07-26T20:12:10-03:00", "PASS_MANUAL"),
        ]
        updated = apply_chronological_evidence(self.base_result(), events, "events.jsonl")
        self.assertEqual(updated.status, PASS_MANUAL)
        self.assertIn("PASS_MANUAL", updated.observed)

    def test_regression_after_pass_forces_not_run(self) -> None:
        events = [
            self.event("2026-07-26T20:12:10-03:00", "PASS_MANUAL"),
            self.event("2026-07-26T21:00:00-03:00", "REGRESSION"),
        ]
        updated = apply_chronological_evidence(self.base_result(), events, "events.jsonl")
        self.assertEqual(updated.status, NOT_RUN)
        self.assertIn("REGRESSION", updated.observed)

    def test_latest_event_is_resolved_per_scenario(self) -> None:
        other = EvidenceEvent(
            scenario_id="FA-008",
            timestamp=datetime.fromisoformat("2026-07-26T22:00:00-03:00"),
            outcome="REGRESSION",
            evidence="other.md",
            note="Outro cenário",
        )
        selected = latest_event(
            [self.event("2026-07-26T20:12:10-03:00", "PASS_MANUAL"), other],
            "FA-009",
        )
        self.assertIsNotNone(selected)
        self.assertEqual(selected.outcome, "PASS_MANUAL")


if __name__ == "__main__":
    unittest.main()
