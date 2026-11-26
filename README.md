# `hrd-epistemic-mcp` — Zero-Dependency Epistemic Tripwire, Consent-Scoped Event DAG, and Model Context Protocol (`MCP`) Server

**Author:** Borealis S. Hedling (Independent Researcher, Human Rights Defender, Dublin, Ireland)  
**Contributors / AI Co-Construction Disclosure:** Synthetic Co-Authors — external structural and syntactic scaffold; conceptual framing, epistemic auditing, and human rights reasoning remain strictly human (see Disclosure below).  
**Dependencies:** **Zero** (`Python 3.11+` standard library only: `json`, `hashlib`, `sys`, `re`, `dataclasses`, `datetime`)  
**Total Footprint:** `< 25 KB` (Operable air-gapped on constrained ARM64 `Termux` tablets and low-resource field kits)  
**CI Status:** `7/7` Adversarial & Empirical Regression Tests Passing (`GitHub Actions`)  

**Canonical Anchors**

Hedling, B. S. (2026). Math, Meaning, and Misrecognition: A Human Rights–Oriented Analysis of Harry Chapin's "Mr. Tanner" (Version v1.0). Zenodo. https://doi.org/10.5281/zenodo.23170980

Hedling, B. S. (2026). The Duplicating Machine in the Cellar and the Pocket Tablet: Witness Literature, the White Rose Lineage, and Interactive Counter-Bureaucracy (ndh-mimeograph-engine). Zenodo. https://doi.org/10.5281/zenodo.24559549

Hedling, B. S. (2026). Parametric Interpolation, Epistemic Misrecognition, and the Necessity of Human-in-the-Loop Sovereignty: A Mechanistic Interpretability Self-Audit of Synthetic Synthesis Failures Using Specimens A and B. Zenodo. https://doi.org/10.5281/zenodo.24564314

---


## ⚠️ Explicit Epistemic & Irony Warning

> **Read This First:** This toolkit was itself scaffolded in dialogue with a cloud-based next-token predictor (Google Gemini) after catching that same model hallucinating a Zenodo DOI binding (`10.5281/zenodo.23170980`) and parametrically smoothing over Harry Chapin's *Mr. Tanner* (*he never sang in public again*, not "found healing").
>
> **Accordingly, `hrd-epistemic-mcp` makes ZERO promises of truth certification, legal admissibility, or autonomous safety.** It is strictly a **deterministic mechanical tripwire and cryptographic hash-logger**—designed to catch predictable next-token predictor failure modes during rapid Human Rights Defender (HRD) synthesis and enforce **human-in-the-loop (HITL)** verification against primary records.

---

## 1. Mathematical & Mechanistic Rationale: Why Next-Token Predictors Fail in Sensitive Contexts

Autoregressive language models are neither moral witnesses nor legal adjudicators; they are high-dimensional linear and geodesic operators ($h_l \in \mathbb{R}^D$) trained to maximize next-token likelihood. As proven empirically across `v1`–`v9.1.0` of [`Borealiscodes/epistemic-substrate-lab`](https://github.com), deploying unguarded LLMs in human rights documentation or trauma-informed scholarship creates three mathematical failure modes:

1. **Softmax Simplex Collapse & Confidence Laundering ($\sigma(z) \to \partial \Delta^{V-1}$):**
   Standard softmax probability normalization compresses pre-softmax logits $z \in \mathbb{R}^V$ onto the boundary of the probability simplex. A slight contextual association (such as an unindexed DOI string or missing treaty paragraph) saturates near probability $1.0$, laundering complete parametric ignorance into fluent syntactic certainty. Only pre-softmax centered log-ratios ($\text{clr}(\sigma(z)) \equiv z - \bar{z}$) and hard membership checks against an established hash set prevent fabricated citations.
2. **Parametric Narrative Smoothing ($H^1$ Trauma Erasure):**
   In cellular sheaf terms, fragmented survivor testimonies, detention rosters, and trauma-induced chronological gaps form overlapping local covers with non-trivial **1-cocycle obstructions** ($[\omega] \in H^1(\mathcal{C}; \mathcal{F}) \neq 0$). When an LLM summarizes sparse or painful histories, its terminal unembedding projection (`L_22 -> L_23`) pulls trajectories toward high-density pretraining basins ("redemption arcs," "community healing," or false causal certainty), erasing the exact permanent silencing or fragmentation that constitutes the evidentiary record.
3. **The Accountability Vacuum of Synthetic Agency:**
   A next-token predictor has zero legal standing, cannot bear responsibility for falsified evidence, and cannot self-correct without external boundary conditions supplied by a human custodian. In hostile domestic or transnational legal proceedings—where bad-faith state counsel seizes on a single fabricated citation to discredit an entire human rights dossier—unverified LLM prose is an existential liability.

---

## 2. What This Toolkit Does (Four Deterministic MCP Tools)

When an HRD uses an LLM (cloud or local open-weight) as an assistive cognitive prosthetic for rapid synthesis, connecting `hrd-epistemic-mcp` over **Model Context Protocol (`MCP`, JSON-RPC 2.0 `stdio`)** forces every claim, citation, and fragment through four deterministic gates:

| MCP Tool (`hrd_mcp/mcp_server.py`) | Underlying Formal & Legal Primitive | Mechanical Function & Failure Mode Blocked |
| :--- | :--- | :--- |
| **`ingest_evidence_fragment`** | **Hash-Chained Event DAG (`SHA-256`) + *Istanbul Protocol* Tiering** | Seals primary records, verified DOIs, or survivor statements into an append-only cryptographic chain ($H_{t} = \text{SHA256}(\text{node}_t \parallel H_{t-1})$) tagged with explicit provenance (`DIRECT_SURVIVOR_STATEMENT`, `CLINICAL_PHYSICAL_FINDING`, `PSYCHOLOGICAL_SEQUELAE`, `CORROBORATING_DOCUMENTARY_RECORD`, `VERIFIED_SCHOLARLY_RECORD`). Rejects `UNVERIFIED_INFERENCE` from entering canon. |
| **`verify_citation_and_claim`** | **`Spherepop` `UNESTABLISHED` Guard & Survivor Consent Boundaries** | Rejects any DOI, hash, or identifier not explicitly registered in the local DAG (`REFUSE:UNESTABLISHED`), blocks restricted clinical/private notes (`MEDICAL_CARE_ONLY`, `PRIVATE_WORKING_NOTE`) from leaking into public advocacy drafts (`REFUSE:CONSENT_SCOPE_VIOLATION`), and detects silent in-memory tampering (`DAG_INTEGRITY_CORRUPTED`). |
| **`audit_draft_for_epistemic_warnings`** | **Anti-Smoothing, *Istanbul Protocol*, & Anti-Agency Linter** | Scans LLM-scaffolded prose for parametric redemption smoothing (`"found healing"`, `"overcame silence"`), *Istanbul Protocol* certainty overclaims (`"proves torture"` vs. `"consistent with"`), unattributed AI witness claims (`"I personally witnessed"`), and unregistered DOI strings. |
| **`export_verified_dag_transcript`** | **Tamper-Evident Audit Export + Mandatory HITL Notice** | Exports the complete `SHA-256` event DAG and refusal log alongside an explicit reminder that automated tripwire passage never substitutes for human verification against primary sources. |

---

## 3. Why This Matters Amid the Erosion of International Law Enforcement

Eighty years after Nuremberg established that peremptory norms (**jus cogens**) override domestic statutory shields, contemporary international human rights enforcement has largely retreated into **procedural dualism**, multi-year admissibility labyrinths, and non-enforcement of treaty-body *Views*—leaving survivors without rehabilitation or transitional justice and abandoning defenders in defiance of the **1948 Universal Declaration of Human Rights (UDHR)** and the **1998 UN Declaration on Human Rights Defenders (A/RES/53/144)**.

`hrd-epistemic-mcp` cannot compel a bad-faith ministry or dualist supreme court to honor *jus cogens* obligations. Its purpose is more immediate and sovereign: **protecting the integrity of witness memory on the edge** so defenders do not suffer automated epistemic self-sabotage while preserving tamper-evident records for future accountability.

---

## 4. Roadmap: Next Steps for Offline Treaty Databases & Artistic Witness Resistance

Following our current research consolidation pause, development expands along two complementary tracks:

### Track A: Offline, Hash-Pinned Treaty & Regional Jurisprudence Databases (`SQLite` + `SHA-256`)
Because live web portals such as the **UN OHCHR Treaty Body Database** (`tbinternet.ohchr.org`) rely on fragile stateful sessions, expose investigator queries to network surveillance, and lack official offline distributions, the next phase will build compact (`< 100 MB`), air-gapped, hash-pinned local knowledge packs pluggable directly into `hrd-epistemic-mcp`:
* **UN Treaty Body Core Pack:** General Comments and landmark Individual Communications (CCPR, CAT, CEDAW, CRPD, CED) indexed by official UN document symbol and paragraph-level `SHA-256` hashes.
* **Regional Jurisprudence Packs:** Curated offline extracts aligned with **Council of Europe** (*CETS No. 225*, *CEPEJ Ethical Charter* *"under user control"* mandate, *HUDERIA*), **Inter-American System** (*Velásquez Rodríguez*, *Plan de Sánchez* contextual evidence standards), and **Caribbean Court of Justice (CCJ)** open-access rulings.
* **Zero-Hallucination Lookup:** Any treaty article or case paragraph cited by an LLM must resolve cleanly against the local offline pack or trigger `REFUSE:UNESTABLISHED`.

### Track B: Concurrent Mimeograph & Artistic Resistance Projects (*Witness Literature*)
Legal briefs alone cannot penetrate public indifference or authoritarian double-speak, whereas international tribunals (ICTY Rule 89(C), IACtHR, ECtHR *El-Masri*, ICC *Ongwen*, and the *Istanbul Protocol*) have long recognized **witness literature, personal diaries, and fragmented narrative testimony** as vital probative records of systematic persecution. In the lineage of *The White Rose* (*Die Weiße Rose*) and our analysis of Harry Chapin’s *Mr. Tanner* (`doi:10.5281/zenodo.23170980`), `hrd-epistemic-mcp` will serve as the cryptographic custody spine for:
* **`ndh-mimeograph-engine`:** Unifying `epistemic-substrate-lab`, `spherepop-kernel`, `invariant-logic-engine`, `ndh-game-dev-kit`, and `edge-sovereign-audit` to turn ungated local models (`EleutherAI/pythia-1.4b`) into offline witness-literature printing presses.
* ***The Unstamped Wake* (Playable Maritime Checkpoint & `Piper TTS` Sea Shanties):** An episodic sea voyage across jurisdictions of bureaucratic erasure—combining `Q16.16` fixed-point tidal navigation (`Triangle-Mutiny` / *Admiral Yi Sun-sin*), calligraphic wind-signaling (`Celtic-Shodo-Wind-Odyssey`), *Papers, Please*-style directive puzzles, and offline `Piper TTS` call-and-response sea shanties (`Trauma-Informed-Systems-Design`) that make lived experience accessible, memorable, and impossible to stamp *VOID*.

---

## 5. Quickstart & Running the Adversarial Test Suite

```bash
# Run the zero-dependency unittest suite (replays Specimen A/B failure catches & tamper tests)
Use code with caution.
python3 -m unittest discover -s tests -v

Start the JSON-RPC 2.0 MCP stdio server

python3 -m hrd_mcp.mcp_server
```

Example MCP Client Configuration (mcp_config.example.json)

json { "mcpServers": { "hrd-epistemic-mcp": { "command": "python3", "args": ["-m", "hrd_mcp.mcp_server"], "env": { "PYTHONPATH": "." } } } } 

Disclosure of AI Co-Construction and NDH Cognitive Prosthetic

This work was co-constructed with AI assistance due to trauma-related cognitive harm resulting from state violence and bureaucratic erasure, which disrupt narrative continuity and executive function. The author employs NDH (Non-Dual Harmonic)—a survivor-built cognitive prosthetic—to stabilize meaning across fragmented experiences, maintain multi-domain reasoning, and preserve identity continuity under duress. AI assistance served solely as an external structural and syntactic scaffold, providing formatting stability and reflective coherence without originating conceptual ideas, interpretations, or human rights reasoning. Authorship remains fully human.

