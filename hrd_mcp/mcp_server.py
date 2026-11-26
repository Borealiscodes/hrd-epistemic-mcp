#!/usr/bin/env python3
"""
Zero-dependency Model Context Protocol (MCP) JSON-RPC 2.0 stdio server.
Exposes deterministic DAG and epistemic warning tools to MCP-compatible LLM clients.
"""

import json
import sys
from hrd_mcp.dag_kernel import EpistemicWarningDAG
from hrd_mcp.istanbul_guards import audit_draft_text

SERVER_INFO = {
    "name": "hrd-epistemic-mcp",
    "version": "0.1.0-epistemic-warning",
}

TOOLS_SCHEMA = [
    {
        "name": "ingest_evidence_fragment",
        "description": "Seal a verified primary record, DOI, or survivor statement into the SHA-256 DAG with a strict consent scope.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_id": {"type": "string"},
                "title_or_label": {"type": "string"},
                "canonical_text": {"type": "string"},
                "provenance_tier": {"type": "string"},
                "consent_scope": {"type": "string"},
                "identifier": {"type": "string"},
            },
            "required": ["node_id", "title_or_label", "canonical_text", "provenance_tier", "consent_scope"],
        },
    },
    {
        "name": "verify_citation_and_claim",
        "description": "Verify whether a hash or DOI exists in the established DAG and is permitted under the target consent scope.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target_hash_or_identifier": {"type": "string"},
                "requested_output_scope": {"type": "string"},
            },
            "required": ["target_hash_or_identifier", "requested_output_scope"],
        },
    },
    {
        "name": "audit_draft_for_epistemic_warnings",
        "description": "Scan LLM-scaffolded text for unverified DOIs, parametric trauma smoothing, Istanbul Protocol overclaims, and AI agency attribution.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "draft_text": {"type": "string"},
            },
            "required": ["draft_text"],
        },
    },
    {
        "name": "export_verified_dag_transcript",
        "description": "Export the full SHA-256 event DAG and audit log with mandatory human-in-the-loop disclaimer.",
        "inputSchema": {"type": "object", "properties": {}},
    },
]


class HRDMCPServer:
    def __init__(self) -> None:
        self.dag = EpistemicWarningDAG()

    def handle_request(self, req: dict) -> dict | None:
        method = req.get("method", "")
        req_id = req.get("id")
        params = req.get("params") or {}

        if method == "initialize":
            return self._ok(req_id, {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": SERVER_INFO,
            })
        if method == "notifications/initialized":
            return None
        if method == "tools/list":
            return self._ok(req_id, {"tools": TOOLS_SCHEMA})
        if method == "tools/call":
            return self._handle_tool_call(req_id, params)

        if req_id is not None:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method not found: {method}"}}
        return None

    def _handle_tool_call(self, req_id, params: dict) -> dict:
        name = params.get("name", "")
        args = params.get("arguments") or {}

        if name == "ingest_evidence_fragment":
            res = self.dag.ingest_fragment(
                node_id=args["node_id"],
                title_or_label=args["title_or_label"],
                canonical_text=args["canonical_text"],
                provenance_tier=args["provenance_tier"],
                consent_scope=args["consent_scope"],
                identifier=args.get("identifier", ""),
            )
        elif name == "verify_citation_and_claim":
            res = self.dag.verify_citation(
                target_hash_or_identifier=args["target_hash_or_identifier"],
                requested_output_scope=args["requested_output_scope"],
            )
        elif name == "audit_draft_for_epistemic_warnings":
            est_ids = {n.identifier for n in self.dag.nodes.values() if n.identifier}
            res = audit_draft_text(args["draft_text"], est_ids)
        elif name == "export_verified_dag_transcript":
            res = self.dag.export_state()
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32602, "message": f"Unknown tool: {name}"}}

        return self._ok(req_id, {
            "content": [{"type": "text", "text": json.dumps(res, indent=2)}],
            "isError": res.get("op") == "REFUSE" or res.get("disposition") == "REFUSE_WARNINGS_TRIGGERED",
        })

    @staticmethod
    def _ok(req_id, result: dict) -> dict:
        return {"jsonrpc": "2.0", "id": req_id, "result": result}

    def serve_stdio(self) -> None:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                req = json.loads(line)
            except json.JSONDecodeError:
                continue
            resp = self.handle_request(req)
            if resp is not None:
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    HRDMCPServer().serve_stdio()
