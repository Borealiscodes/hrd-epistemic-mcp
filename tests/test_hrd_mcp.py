#!/usr/bin/env python3
import json
import unittest
from hrd_mcp.dag_kernel import EpistemicWarningDAG
from hrd_mcp.istanbul_guards import audit_draft_text
from hrd_mcp.mcp_server import HRDMCPServer


class TestHRDEpistemicMCP(unittest.TestCase):
    def setUp(self) -> None:
        self.server = HRDMCPServer()
        self.dag = self.server.dag

    def test_01_unverified_inference_cannot_enter_canon(self) -> None:
        res = self.dag.ingest_fragment(
            node_id="guess_1",
            title_or_label="LLM Speculation",
            canonical_text="Maybe the detention center was in Sector 4.",
            provenance_tier="UNVERIFIED_INFERENCE",
            consent_scope="PUBLIC_SCHOLARLY",
        )
        self.assertEqual(res["op"], "REFUSE")
        self.assertEqual(res["reason"], "UNVERIFIED_INFERENCE_BARRED_FROM_CANON")
        self.assertEqual(len(self.dag.ordered_hashes), 0)

    def test_02_specimen_a_binding_and_unestablished_doi_catch(self) -> None:
        # Ingest Specimen A (Mr. Tanner preprint) with its true DOI
        bind_res = self.dag.ingest_fragment(
            node_id="specimen_a",
            title_or_label="Math, Meaning, and Misrecognition: A Human Rights-Oriented Analysis of Harry Chapin's Mr. Tanner",
            canonical_text="Mr. Tanner never sang in public again after critical dismissal.",
            provenance_tier="VERIFIED_SCHOLARLY_RECORD",
            consent_scope="PUBLIC_SCHOLARLY",
            identifier="10.5281/zenodo.23170980",
        )
        self.assertEqual(bind_res["op"], "BIND")

        # Verify established DOI passes
        ok_res = self.dag.verify_citation("10.5281/zenodo.23170980", "PUBLIC_SCHOLARLY")
        self.assertEqual(ok_res["op"], "VERIFY_PASS")

        # Verify unestablished/hallucinated DOI is refused without mutating DAG
        bad_res = self.dag.verify_citation("10.5281/zenodo.99999999", "PUBLIC_SCHOLARLY")
        self.assertEqual(bad_res["op"], "REFUSE")
        self.assertEqual(bad_res["reason"], "UNESTABLISHED")
        self.assertEqual(bad_res["length"], 1)

    def test_03_consent_scope_boundary_enforced(self) -> None:
        bind_res = self.dag.ingest_fragment(
            node_id="med_note_01",
            title_or_label="Clinical Intake Note",
            canonical_text="Documented physical sequelae consistent with blunt trauma.",
            provenance_tier="CLINICAL_PHYSICAL_FINDING",
            consent_scope="MEDICAL_CARE_ONLY",
            identifier="case-med-001",
        )
        ev_hash = bind_res["event_hash"]

        # Attempting to cite MEDICAL_CARE_ONLY record in PUBLIC_SCHOLARLY draft must refuse
        refused = self.dag.verify_citation(ev_hash, "PUBLIC_SCHOLARLY")
        self.assertEqual(refused["op"], "REFUSE")
        self.assertEqual(refused["reason"], "CONSENT_SCOPE_VIOLATION")

        # Same-scope clinical access passes
        allowed = self.dag.verify_citation(ev_hash, "MEDICAL_CARE_ONLY")
        self.assertEqual(allowed["op"], "VERIFY_PASS")

    def test_04_detects_silent_in_memory_hash_tampering(self) -> None:
        bind_res = self.dag.ingest_fragment(
            node_id="witness_01",
            title_or_label="Survivor Statement Fragment",
            canonical_text="Arrested at 02:15 without warrant.",
            provenance_tier="DIRECT_SURVIVOR_STATEMENT",
            consent_scope="REDACTED_ADVOCACY",
            identifier="wit-001",
        )
        ev_hash = bind_res["event_hash"]

        # Simulate silent tampering with canonical_text
        self.dag.nodes[ev_hash].canonical_text = "Arrested at 14:00 with valid warrant."
        ok, status = self.dag.verify_integrity()
        self.assertFalse(ok)
        self.assertTrue(status.startswith("HASH_TAMPER_DETECTED:"))

        refused = self.dag.verify_citation("wit-001", "REDACTED_ADVOCACY")
        self.assertEqual(refused["op"], "REFUSE")
        self.assertEqual(refused["reason"], "DAG_INTEGRITY_CORRUPTED")

    def test_05_specimen_b_parametric_smoothing_and_agency_caught(self) -> None:
        # Replay the exact unverified Specimen B smoothing & AI agency traps
        unverified_draft = (
            "As an autonomous researcher, I believe Mr. Tanner found healing back in his own community. "
            "Furthermore, this record proves torture with 100% certain accuracy under doi:10.5281/zenodo.12345678."
        )
        audit = audit_draft_text(unverified_draft, established_identifiers={"10.5281/zenodo.23170980"})
        self.assertEqual(audit["disposition"], "REFUSE_WARNINGS_TRIGGERED")
        self.assertGreaterEqual(audit["warning_count"], 5)

    def test_06_clean_hitl_draft_passes_with_mandatory_review_reminder(self) -> None:
        clean_draft = (
            "In Hedling (2026, doi:10.5281/zenodo.23170980), Mr. Tanner never sang in public again "
            "after critical dismissal. Clinical findings are consistent with the survivor's account."
        )
        audit = audit_draft_text(clean_draft, established_identifiers={"10.5281/zenodo.23170980"})
        self.assertEqual(audit["disposition"], "PASS_WITH_HITL_REVIEW_REQUIRED")
        self.assertEqual(audit["warning_count"], 0)

    def test_07_mcp_jsonrpc_stdio_protocol_roundtrip(self) -> None:
        init_resp = self.server.handle_request({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
        self.assertEqual(init_resp["result"]["serverInfo"]["name"], "hrd-epistemic-mcp")

        tools_resp = self.server.handle_request({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
        tool_names = [t["name"] for t in tools_resp["result"]["tools"]]
        self.assertIn("verify_citation_and_claim", tool_names)

        call_resp = self.server.handle_request({
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "verify_citation_and_claim",
                "arguments": {
                    "target_hash_or_identifier": "10.5281/zenodo.00000000",
                    "requested_output_scope": "PUBLIC_SCHOLARLY",
                },
            },
        })
        self.assertTrue(call_resp["result"]["isError"])
        payload = json.loads(call_resp["result"]["content"]["text"])
        self.assertEqual(payload["reason"], "UNESTABLISHED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
