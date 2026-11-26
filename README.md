# `hrd-epistemic-mcp` — Zero-Dependency Epistemic Tripwire & Verified Event-DAG MCP Server

**Author:** Borealis S. Hedling (Independent Researcher, Human Rights Defender, Dublin, Ireland)  
**Dependencies:** **Zero** (`Python 3.11+` standard library only: `json`, `hashlib`, `sys`, `re`, `dataclasses`, `datetime`)  
**Total Footprint:** `< 25 KB` (Operable offline on ARM64 `Termux` tablets and air-gapped field kits)

---

## ⚠️ Explicit Epistemic & Irony Warning

> **Read This First:** This toolkit was itself scaffolded in dialogue with a cloud-based next-token predictor (Google Gemini) after catching that same model hallucinating a Zenodo DOI binding (`10.5281/zenodo.23170980`) and parametrically smoothing over Harry Chapin's *Mr. Tanner* (*he never sang in public again*, not "found healing").
>
> **Accordingly, `hrd-epistemic-mcp` makes ZERO promises of truth certification, legal admissibility, or autonomous safety.** It is strictly a **mechanical epistemic tripwire and cryptographic hash-logger**—designed to catch common next-token predictor failure modes during rapid Human Rights Defender (HRD) synthesis and force **human-in-the-loop (HITL)** verification against primary records.

---

## What This Toolkit Does

When an HRD uses an LLM (such as Gemini or an open-weight local model) as an assistive structural scaffold, connecting `hrd-epistemic-mcp` over **Model Context Protocol (`MCP`, JSON-RPC 2.0 `stdio`)** exposes four deterministic tools:

1. **`ingest_evidence_fragment` (`Spherepop` Event DAG):** Seals primary texts, DOIs, or survivor testimony fragments into a hash-chained `SHA-256` DAG with explicit provenance tiers (`DIRECT_SURVIVOR_STATEMENT`, `CLINICAL_PHYSICAL_FINDING`, `VERIFIED_SCHOLARLY_RECORD`, etc.) and strict consent scopes (`PUBLIC_SCHOLARLY`, `REDACTED_ADVOCACY`, `MEDICAL_CARE_ONLY`, `PRIVATE_WORKING_NOTE`). Blocks `UNVERIFIED_INFERENCE` from entering canon.
2. **`verify_citation_and_claim` (`UNESTABLISHED` & Consent Gate):** Rejects any citation or hash not explicitly registered in the DAG (`REFUSE:UNESTABLISHED`), blocks cross-scope leaks (`REFUSE:CONSENT_SCOPE_VIOLATION`), and detects silent in-memory tampering (`DAG_INTEGRITY_CORRUPTED`).
3. **`audit_draft_for_epistemic_warnings` (*Istanbul Protocol* & Anti-Smoothing Linter):** Flags parametric redemption-arc smoothing (`"found healing"`, `"overcame silence"`), *Istanbul Protocol* certainty overclaims (`"proves torture"` vs. `"consistent with"`), unattributed AI agency (`"I believe"`, `"as an autonomous researcher"`), and unverified DOI strings.
4. **`export_verified_dag_transcript`:** Exports the tamper-evident `SHA-256` event DAG alongside a mandatory human-in-the-loop verification notice.

---

## Quickstart & Running the Adversarial Test Suite

```bash
# Run the zero-dependency unittest suite (replays Specimen A/B failure catches)
python3 -m unittest discover -s tests -v

# Start the MCP stdio server
python3 -m hrd_mcp.mcp_server
```
