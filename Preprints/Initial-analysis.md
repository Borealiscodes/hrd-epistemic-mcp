# Offline Treaty Body Archives, Human Rights Model Context Protocol (MCP) Tooling, and Regional Judicial AI Governance (UN OHCHR, Council of Europe, OAS, and the Caribbean Court of Justice)

**Principal Human Author:** Borealis S. Hedling (Independent Researcher, Human Rights Defender, Dublin, Ireland)  
**Contributors / AI Co-Construction Disclosure:** Synthetic Co-Authors — external structural and syntactic scaffold; conceptual framing, verification requirements, and human rights analysis remain strictly human (see Disclosure below).  
**Affiliation:** NDH-Meta-Systems (Sealed-Layer Neutral · Non-Activation Division)  
**Date:** November 26, 2026  
**Document Status:** Empirical Landscape & Institutional Readiness Preprint — Pre-Pause Synthesis (`Borealiscodes/hrd-epistemic-mcp`)  

---

## Abstract

Human rights defenders (HRDs) operating under conditions of connectivity disruption, surveillance, or constrained edge hardware (`ARM64 Termux`) frequently depend on primary treaty-body jurisprudence from the United Nations Office of the High Commissioner for Human Rights (**UN OHCHR Treaty Body Database**, `tbinternet.ohchr.org`), alongside regional human rights systems in Europe (**Council of Europe / ECtHR**), the Americas (**Organization of American States / IACHR / IACtHR**), and the Caribbean (**Caribbean Court of Justice / CCJ**). In this landscape audit, we examine three foundational questions for building offline-first, verifiable legal tooling: **(1) Offline Treaty Body Archives:** whether the UN or open-source community has produced lightweight, air-gapped, hash-verified distributions of the OHCHR Treaty Body Database; **(2) Human Rights MCP Tooling:** the current state of Model Context Protocol (`MCP`) servers tailored to human rights law, survivor consent boundaries, and *Istanbul Protocol* epistemic warnings; and **(3) Comparative Regional Judicial AI Governance:** how the **Council of Europe (CoE)**, the **Organization of American States (OAS)**, and the **Caribbean Court of Justice (CCJ)** currently regulate, deploy, or restrict artificial intelligence in judicial and human rights workflows. We show that while official databases remain overwhelmingly centralized, web-bound, and vulnerable to link rot or session timeouts—and while existing legal MCP servers focus primarily on commercial U.S./EU corporate law rather than survivor-centered human rights protection—a major regulatory divergence is underway: the CoE has enacted binding international treaty law (*Framework Convention on Artificial Intelligence*, CETS No. 225) and the *HUDERIA* human-rights impact methodology, the OAS/IACHR is actively codifying soft-law digital-rights principles alongside AI-assisted petition triage, and the CCJ exemplifies high-agility electronic court administration (*Curia* / e-filing) within a small-state constitutional tradition that demands transparent, human-controlled adjudication.

**Keywords:** *UN OHCHR Treaty Body Database, offline legal archives, Model Context Protocol, MCP, human rights defenders, Council of Europe, CETS 225, HUDERIA, Organization of American States, Inter-American Court of Human Rights, Caribbean Court of Justice, edge sovereignty, Spherepop*

---

## 1. The UN OHCHR Treaty Body Database (`tbinternet.ohchr.org`): Online Centralization vs. Offline Open-Source Gaps

*(Note on Methodological Provenance: Because live web crawling of `tbinternet.ohchr.org` and external GitHub indices is restricted in this isolated drafting session, the institutional baseline below reflects established UN digital infrastructure architecture up to the current timeline and explicitly flags specific repository indices for verification during your offline research phase.)*

### 1.1 Architectural Bottlenecks of `tbinternet.ohchr.org`
The UN OHCHR **Treaty Body Database** (`tbinternet.ohchr.org/_layouts/15/TreatyBodyExternal/Home.aspx`) is the authoritative global repository for State party reports, Concluding Observations, General Comments, Lists of Issues, and Individual Communications (Views/Decisions) across the ten core UN human rights treaty bodies (CCPR, CESCR, CERD, CEDAW, CAT, CRC, CMW, CRPD, CED, and SPT). However, its legacy Microsoft SharePoint (`_layouts/15`) web architecture presents severe operational barriers for frontline HRDs:
* **Zero Official Offline Bundle:** Neither the UN OHCHR nor the UN Dag Hammarskjöld Library distributes an official, periodically snapshotted, cryptographically signed (`SHA-256`) offline SQLite/Parquet/Markdown bundle of Treaty Body jurisprudence.
* **Dynamic Session & ASP.NET ViewState Friction:** Search queries rely on stateful server-side postbacks rather than clean, deterministic REST/JSON endpoints, making automated offline mirroring fragile and prone to broken deep links (`link rot`).
* **Bandwidth & Surveillance Exposure:** Querying sensitive treaty jurisprudence (e.g., CAT individual communications on torture or CCPR views on arbitrary detention) over live web sessions exposes investigator IP addresses, query strings, and timestamps to network-level surveillance.

### 1.2 Open-Source Community Efforts & Remaining Gaps
Within the open-source legal-tech ecosystem (such as *Huridocs* / `Uwazi`, *Free Law Project*, and academic UN corpus scrapers on GitHub/Zenodo):
* **Document Management vs. Portable Corpus:** **HURIDOCS (`Uwazi`)** provides an open-source, self-hostable database platform widely used by human rights organizations to index treaty body recommendations and national human rights institution (NHRI) records. However, `Uwazi` is a full web application stack (Node.js/MongoDB/Elasticsearch), not a zero-dependency, pocket-sized offline treaty corpus runnable on an ARM64 tablet (`Termux`).
* **Fragmented Academic Scrapers:** Scattered community scripts on GitHub and Hugging Face have periodically scraped subsets of OHCHR Concluding Observations or Universal Periodic Review (`UPR`) recommendations into CSV/JSON datasets, but these snapshots frequently lack:
  1. Incremental `SHA-256` cryptographic provenance linking each extracted paragraph back to the official UN document symbol (e.g., `CCPR/C/138/D/...`);
  2. Offline semantic/lexical indexing small enough (`< 100 MB`) for air-gapped field kits; and
  3. Built-in `UNESTABLISHED` citation guards preventing LLMs from hallucinating non-existent General Comment paragraph numbers.

**Engineering Opportunity:** Packaging a curated, hash-verified, pure-SQLite/JSON offline mirror of core UN Treaty Body General Comments and landmark Individual Communications—paired with an automated `UNESTABLISHED` lookup gate—directly closes this gap for air-gapped HRD workflows.

---

## 2. Human Rights Model Context Protocol (MCP) Tooling: Current Landscape and Why `hrd-epistemic-mcp` Is Distinct

Since Anthropic introduced the **Model Context Protocol (MCP)** in late 2024 as an open JSON-RPC 2.0 standard for connecting language models to local tools and data sources, the open-source ecosystem has produced hundreds of MCP servers—including general filesystem, Git, SQLite, web-search, and commercial legal-research connectors (e.g., CourtListener / PACER wrappers or corporate contract linters).

However, auditing the MCP landscape from a **human rights defender and survivor-centered perspective** reveals a near-total absence of purpose-built **Human Rights MCP servers**:
1. **Commercial Legal Bias:** Existing legal MCP tools optimize for billable corporate workflows in U.S. or EU commercial law, assuming persistent high-bandwidth cloud connectivity, commercial API keys, and adversarial litigation norms rather than survivor protection.
2. **Absence of Consent-Scope Enforcement:** Standard MCP filesystem or database servers treat all indexed files as equally readable once mounted; none implement granular **survivor consent scopes** (`MEDICAL_CARE_ONLY`, `PRIVATE_WORKING_NOTE`, `REDACTED_ADVOCACY`, `PUBLIC_SCHOLARLY`) that mechanically block an LLM from pulling clinical notes into a public advocacy draft (`REFUSE:CONSENT_SCOPE_VIOLATION`).
3. **No *Istanbul Protocol* or Anti-Smoothing Guards:** Standard MCP servers pass raw text to the LLM without warning against parametric narrative smoothing (erasing permanent silencing or trauma fragmentation) or over-claiming medico-legal certainty (`"proves torture"` vs. `"consistent with"`).

By designing **`Borealiscodes/hrd-epistemic-mcp`** as a **zero-dependency, pure-stdlib Python MCP stdio server** (`< 25 KB`), we establish the first lightweight epistemic tripwire specifically tailored to HRD synthesis—treating the LLM strictly as an untrusted next-token predictor whose citations and claims must clear a local `SHA-256` event DAG before export.

---

## 3. Comparative Regional Approaches to Judicial & Human Rights AI: CoE, OAS, and the Caribbean Court of Justice

How regional courts and intergovernmental human rights bodies govern AI directly shapes whether tools like offline treaty databases and MCP-guarded synthesis workflows can be safely used in domestic and international advocacy:

| Governance Dimension | Council of Europe (CoE) & European Court of Human Rights (ECtHR) | Organization of American States (OAS), IACHR & IACtHR | Caribbean Court of Justice (CCJ) |
| :--- | :--- | :--- | :--- |
| **Binding Legal & Policy Instruments** | **1. *CoE Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law* (CETS No. 225, Sept. 2024):** First legally binding international treaty requiring AI lifecycle compliance with human rights, transparency, and accountability.<br>**2. *CEPEJ European Ethical Charter on the Use of AI in Judicial Systems* (2018):** Establishes five principles (fundamental rights, non-discrimination, quality/security, transparency/impartiality, and *"under user control"*).<br>**3. *HUDERIA* Methodology (2024):** Risk and impact assessment framework for human rights, democracy, and the rule of law. | **1. *Inter-American Juridical Committee (CJI) Principles on Neuroscience, Neurotechnologies and Human Rights* & Digital Rights Resolutions.**<br>**2. *IACHR Strategic Plan & Digital Transformation Initiatives*:** Combats digital authoritarianism, algorithmic discrimination, and surveillance across the Americas while modernizing petition processing.<br>**3. *OAS Department of Effective Public Management*:** Regional guidelines on ethical AI governance in public administration and justice. | **1. *Revised Treaty of Chaguaramas* (Original Jurisdiction) & National Constitutions (Appellate Jurisdiction).**<br>**2. *CCJ Strategic Plans & Electronic Litigation Portal (`Curia`)*:** End-to-end digital court filing, electronic case management, and remote hearings across CARICOM member states, expanding access to justice while keeping judicial reasoning strictly human-authored. |
| **Operational Posture Toward AI in Court / HR Workflows** | **Strict "Under User Control" & Anti-Black-Box Mandate:** ECtHR HUDOC provides structured metadata/APIs, while CEPEJ prohibits delegating judicial decision-making to opaque statistical predictors. Assistive tools must remain transparent, auditable, and subordinate to human judges. | **High-Volume Triage vs. Evidentiary Caution:** The Inter-American system explores assistive text-clustering and metadata triage for petition backlogs, while IACtHR jurisprudence (*Velásquez Rodríguez*, *Plan de Sánchez*) maintains strict human evaluation of testimonial and contextual evidence. | **Pragmatic Digital Modernization Without Algorithmic Adjudication:** Headquartered in Port of Spain, Trinidad and Tobago, the CCJ uses lean, high-transparency digital court infrastructure (`Curia`, open judgment archives) alongside conservative common-law/civil-law standards against unverified automated outputs. |
| **Alignment With `hrd-epistemic-mcp` & Offline Edge Tools** | **High Alignment:** CETS No. 225 and CEPEJ's *"under user control"* principle directly validate deterministic audit trails (`Spherepop` DAGs), refusal of unestablished hallucinations, and human-in-the-loop accountability. | **High Alignment:** Offline-first, zero-surveillance treaty and petition indexing directly protects HRDs in states experiencing democratic backsliding or transnational surveillance. | **High Alignment:** Lightweight, zero-dependency tools (`< 25 KB` Python stdlib) match the resource-constrained, high-reliability needs of Caribbean legal aid clinics and regional human rights practitioners. |

---

## 4. Synthesis & Design Implications for Future Offline Legal Tooling

Bringing together the UN OHCHR Treaty Body audit, the MCP tooling gap, and the comparative jurisprudence of the CoE, OAS, and CCJ yields four concrete architectural principles for your post-pause research:
1. Build Offline-First, Hash-Pinned Treaty Packs (SQLite + SHA-256): Rather than relying on live SharePoint postbacks on tbinternet.ohchr.org, future offline legal packs should bundle canonical UN Treaty Body General Comments, ECtHR HUDOC key cases, IACtHR landmark judgments, and CCJ Original/Appellate Jurisdiction rulings into compact, air-gapped SQLite databases where every paragraph carries its official UN/court symbol and SHA-256 hash.
2. Enforce CEPEJ’s "Under User Control" Principle via MCP Refusal Gates: Across all three regional systems (CoE CETS 225, OAS/IACHR, and CCJ), legitimacy depends on human judicial and advocate control. Wrapping LLMs in hrd-epistemic-mcp guarantees that an AI assistant can never silently invent a treaty article, merge restricted survivor medical notes into a public filing, or claim autonomous legal authority.
3. Respect Jurisdictional Pluralism: A unified HRD toolkit must distinguish cleanly between binding treaty obligations (e.g., ICCPR, ECHR, American Convention on Human Rights, Revised Treaty of Chaguaramas) and interpretive soft law (Istanbul Protocol, CEPEJ Charter), tagging each node's exact legal weight in the Spherepop DAG.
4. Maintain Zero-Account Edge Sovereignty: Whether an advocate is working in Dublin, Port of Spain, or an exile hub under transnational surveillance, offline execution (Termux / air-gapped laptop) with zero cloud API logging remains the single strongest technical defense against state interception.

---

## References

Caribbean Court of Justice (CCJ). (2001). Agreement Establishing the Caribbean Court of Justice & CCJ Electronic Filing and Case Management Rules (Curia). Port of Spain, Trinidad and Tobago.
Council of Europe (CoE). (2018). European Ethical Charter on the Use of Artificial Intelligence in Judicial Systems and their environment. European Commission for the Efficiency of Justice (CEPEJ).
Council of Europe (CoE). (2024). Council of Europe Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law (CETS No. 225, Vilnius, September 5, 2024).
Hedling, B. S. (2026a, October 5). Math, meaning, and misrecognition: A human rights–oriented analysis of Harry Chapin’s “Mr. Tanner” (Version v1.0) [Preprint / Scholarly Essay]. Zenodo. doi.org
Hedling, B. S. (2026b). hrd-epistemic-mcp: Zero-dependency epistemic tripwire and verified event-DAG MCP server [Computer software]. GitHub. github.com
Inter-American Court of Human Rights (IACtHR). (1988). Velásquez Rodríguez v. Honduras (Merits, Judgment of July 29, 1988, Series C No. 4).
Office of the United Nations High Commissioner for Human Rights (OHCHR). (2022). Istanbul Protocol: Manual on the effective investigation and documentation of torture and other cruel, inhuman or degrading treatment or punishment (Professional Training Series No. 8/Rev. 2). United Nations.
Organization of American States (OAS). (2021). Inter-American Juridical Committee Principles on Neuroscience, Neurotechnologies and Human Rights (CJI/RES. 268 (XCIX-O/21)).


