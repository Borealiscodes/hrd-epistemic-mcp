#!/usr/bin/env python3
"""
Zero-dependency Spherepop-inspired SHA-256 Event DAG for Human Rights Defenders.
Enforces:
- Cryptographic hash chaining of primary records (no silent history mutation).
- Explicit consent-scope boundaries (POP / BIND / REFUSE:CONSENT_SCOPE_VIOLATION).
- Strict UNESTABLISHED rejection for any citation/claim not anchored in the DAG.
"""

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
import hashlib
import json


VALID_PROVENANCE_TIERS = {
    "DIRECT_SURVIVOR_STATEMENT",
    "CLINICAL_PHYSICAL_FINDING",
    "PSYCHOLOGICAL_SEQUELAE",
    "CORROBORATING_DOCUMENTARY_RECORD",
    "VERIFIED_SCHOLARLY_RECORD",
    "UNVERIFIED_INFERENCE",
}

VALID_CONSENT_SCOPES = {
    "PUBLIC_SCHOLARLY",
    "REDACTED_ADVOCACY",
    "MEDICAL_CARE_ONLY",
    "PRIVATE_WORKING_NOTE",
}


def canonical_sha256(payload: dict) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


@dataclass
class EvidenceNode:
    node_id: str
    parent_hash: str
    timestamp_utc: str
    title_or_label: str
    canonical_text: str
    identifier: str  # e.g., DOI, archive ID, or empty string
    provenance_tier: str
    consent_scope: str
    event_hash: str = ""

    def compute_hash(self) -> str:
        body = {
            "node_id": self.node_id,
            "parent_hash": self.parent_hash,
            "timestamp_utc": self.timestamp_utc,
            "title_or_label": self.title_or_label,
            "canonical_text": self.canonical_text,
            "identifier": self.identifier,
            "provenance_tier": self.provenance_tier,
            "consent_scope": self.consent_scope,
        }
        return canonical_sha256(body)


@dataclass
class EpistemicWarningDAG:
    genesis_hash: str = field(default_factory=lambda: canonical_sha256({"genesis": "HRD_EPISTEMIC_TRIPWIRE_V0"}))
    nodes: dict[str, EvidenceNode] = field(default_factory=dict)
    ordered_hashes: list[str] = field(default_factory=list)
    audit_log: list[dict] = field(default_factory=list)

    @property
    def head_hash(self) -> str:
        return self.ordered_hashes[-1] if self.ordered_hashes else self.genesis_hash

    def ingest_fragment(
        self,
        node_id: str,
        title_or_label: str,
        canonical_text: str,
        provenance_tier: str,
        consent_scope: str,
        identifier: str = "",
    ) -> dict:
        if provenance_tier not in VALID_PROVENANCE_TIERS:
            return self._log_refusal("INVALID_PROVENANCE_TIER", {"tier": provenance_tier})
        if consent_scope not in VALID_CONSENT_SCOPES:
            return self._log_refusal("INVALID_CONSENT_SCOPE", {"scope": consent_scope})
        if provenance_tier == "UNVERIFIED_INFERENCE":
            return self._log_refusal(
                "UNVERIFIED_INFERENCE_BARRED_FROM_CANON",
                {"node_id": node_id, "warning": "Parametric LLM guesses cannot be sealed as evidence."},
            )

        node = EvidenceNode(
            node_id=node_id,
            parent_hash=self.head_hash,
            timestamp_utc=datetime.now(timezone.utc).isoformat(),
            title_or_label=title_or_label,
            canonical_text=canonical_text,
            identifier=identifier.strip(),
            provenance_tier=provenance_tier,
            consent_scope=consent_scope,
        )
        node.event_hash = node.compute_hash()
        self.nodes[node.event_hash] = node
        self.ordered_hashes.append(node.event_hash)

        entry = {
            "op": "BIND",
            "node_id": node_id,
            "event_hash": node.event_hash,
            "head": self.head_hash,
            "length": len(self.ordered_hashes),
        }
        self.audit_log.append(entry)
        return entry

    def verify_integrity(self) -> tuple[bool, str]:
        """Re-computes every hash in the chain to detect silent in-memory/file tampering."""
        expected_parent = self.genesis_hash
        for h in self.ordered_hashes:
            node = self.nodes.get(h)
            if node is None:
                return False, f"MISSING_NODE:{h}"
            if node.parent_hash != expected_parent:
                return False, f"BROKEN_PARENT_LINK:{h}"
            if node.compute_hash() != h:
                return False, f"HASH_TAMPER_DETECTED:{h}"
            expected_parent = h
        return True, "INTACT"

    def verify_citation(
        self,
        target_hash_or_identifier: str,
        requested_output_scope: str,
    ) -> dict:
        ok, status = self.verify_integrity()
        if not ok:
            return self._log_refusal("DAG_INTEGRITY_CORRUPTED", {"detail": status})

        matched_node = None
        query = target_hash_or_identifier.strip()
        if query in self.nodes:
            matched_node = self.nodes[query]
        else:
            for node in self.nodes.values():
                if node.identifier and node.identifier == query:
                    matched_node = node
                    break

        if matched_node is None:
            return self._log_refusal(
                "UNESTABLISHED",
                {
                    "query": query,
                    "epistemic_warning": (
                        "STOP: Identifier or hash is NOT in the established DAG. "
                        "Do NOT invent a title, date, or claim for this identifier."
                    ),
                },
            )

        # Enforce consent scope hierarchy: MEDICAL_CARE_ONLY and PRIVATE_WORKING_NOTE
        # cannot be exported into PUBLIC_SCHOLARLY or REDACTED_ADVOCACY drafts.
        restricted_scopes = {"MEDICAL_CARE_ONLY", "PRIVATE_WORKING_NOTE"}
        if matched_node.consent_scope in restricted_scopes and requested_output_scope != matched_node.consent_scope:
            return self._log_refusal(
                "CONSENT_SCOPE_VIOLATION",
                {
                    "node_id": matched_node.node_id,
                    "bound_scope": matched_node.consent_scope,
                    "requested_scope": requested_output_scope,
                },
            )

        entry = {
            "op": "VERIFY_PASS",
            "node_id": matched_node.node_id,
            "event_hash": matched_node.event_hash,
            "identifier": matched_node.identifier,
            "provenance_tier": matched_node.provenance_tier,
            "consent_scope": matched_node.consent_scope,
        }
        self.audit_log.append(entry)
        return entry

    def _log_refusal(self, reason: str, detail: dict) -> dict:
        entry = {
            "op": "REFUSE",
            "reason": reason,
            "head": self.head_hash,
            "length": len(self.ordered_hashes),
            "detail": detail,
        }
        self.audit_log.append(entry)
        return entry

    def export_state(self) -> dict:
        ok, status = self.verify_integrity()
        return {
            "epistemic_disclaimer": (
                "WARNING: Mechanical cryptographic log only. Does NOT certify legal truth "
                "or replace human-in-the-loop verification."
            ),
            "integrity_status": status if ok else f"CORRUPTED:{status}",
            "genesis_hash": self.genesis_hash,
            "head_hash": self.head_hash,
            "node_count": len(self.ordered_hashes),
            "nodes": {h: asdict(n) for h, n in self.nodes.items()},
            "audit_log": self.audit_log,
        }
