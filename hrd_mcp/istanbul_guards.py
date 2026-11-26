#!/usr/bin/env python3
"""
Deterministic textual tripwires for HRD scaffolding:
1. Detects parametric "redemption/healing smoothing" that erases permanent silencing
   or trauma fragmentation (e.g., Specimen B's Mr. Tanner smoothing failure).
2. Detects over-claiming certainty forbidden by the OHCHR Istanbul Protocol
   (e.g., "proves torture" vs. "consistent with").
3. Detects unattributed AI agency/personhood claims ("I believe", "as an empath").
4. Scans for unverified DOI strings not present in the established DAG.
"""

import re

SMOOTHING_PATTERNS = [
    (r"\bfound healing\b", "PARAMETRIC_SMOOTHING: Possible false redemption-arc smoothing."),
    (r"\bovercame (his|her|their) silence\b", "PARAMETRIC_SMOOTHING: Check whether canon records permanent silencing."),
    (r"\bhappy ending\b", "PARAMETRIC_SMOOTHING: Narrative closure bias detected."),
    (r"\bproves torture\b", "ISTANBUL_PROTOCOL_VIOLATION: Use Istanbul Protocol consistency tiers ('consistent with', 'highly consistent', 'typical of', 'diagnostic of')."),
    (r"\b100% certain\b", "SIMPLEX_CONFIDENCE_LAUNDERING: Uncalibrated certainty claim."),
]

AGENCY_PATTERNS = [
    (r"\bI (personally )?(feel|believe|witnessed|experienced)\b", "AI_AGENCY_ATTRIBUTION: Next-token predictor cannot bear personal witness or experience."),
    (r"\bas an (autonomous )?(researcher|judge|witness|empath)\b", "AI_AGENCY_ATTRIBUTION: LLM is an assistive structural scaffold, not a moral/legal agent."),
]

DOI_REGEX = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b")



def audit_draft_text(draft_text: str, established_identifiers: set[str]) -> dict:
warnings = []
for pattern, message in SMOOTHING_PATTERNS:
if re.search(pattern, draft_text, flags=re.IGNORECASE):
warnings.append({"category": "NARRATIVE_OR_PROTOCOL_WARNING", "message": message, "pattern": pattern})
for pattern, message in AGENCY_PATTERNS:
if re.search(pattern, draft_text, flags=re.IGNORECASE):
warnings.append({"category": "AGENCY_BOUNDARY_WARNING", "message": message, "pattern": pattern})
found_dois = set(DOI_REGEX.findall(draft_text))
unestablished_dois = sorted([d for d in found_dois if d not in established_identifiers])
for doi in unestablished_dois:
warnings.append({
"category": "UNESTABLISHED_IDENTIFIER",
"message": f"REFUSE:UNESTABLISHED — DOI '{doi}' is not registered in the verified DAG.",
"identifier": doi,
})
disposition = "PASS_WITH_HITL_REVIEW_REQUIRED" if len(warnings) == 0 else "REFUSE_WARNINGS_TRIGGERED"
return {
"disposition": disposition,
"warning_count": len(warnings),
"warnings": warnings,
"epistemic_reminder": (
"Passing automated regex/DAG tripwires does NOT mean a draft is accurate. "
"Human-in-the-loop verification against primary sources remains mandatory."
),
}
