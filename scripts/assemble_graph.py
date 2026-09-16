#!/usr/bin/env python3
"""Assemble and validate The Ancestry of Stories data shards."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DIST = ROOT / "dist"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def assemble() -> dict:
    manifest = load_json(DATA / "manifest.json")
    meta = load_json(DATA / manifest["meta"])
    ontology = load_json(DATA / manifest["ontology"]) if manifest.get("ontology") else {}
    coverage = load_json(DATA / manifest["coverage"]) if manifest.get("coverage") else {}

    nodes = []
    for name in manifest["nodes"]:
        nodes.extend(load_json(DATA / name))

    edges = []
    for name in manifest["edges"]:
        edges.extend(load_json(DATA / name))

    return {
        "meta": meta,
        "ontology": ontology,
        "coverage": coverage,
        "nodes": nodes,
        "edges": edges,
        "manifest": manifest,
    }


def validate(graph: dict) -> list[str]:
    errors: list[str] = []
    nodes = graph["nodes"]
    edges = graph["edges"]
    manifest = graph["manifest"]
    ontology = graph.get("ontology", {})
    coverage = graph.get("coverage", {})

    ids = [n.get("id") for n in nodes]
    id_set = set(ids)

    if len(ids) != len(id_set):
        errors.append("Duplicate node IDs found")
    if len(nodes) != manifest["counts"]["nodes"]:
        errors.append(f"Node count mismatch: {len(nodes)} != {manifest['counts']['nodes']}")
    if len(edges) != manifest["counts"]["edges"]:
        errors.append(f"Edge count mismatch: {len(edges)} != {manifest['counts']['edges']}")

    allowed_types = {"work", "person", "tradition", "context", "medium"}
    allowed_layers = set(ontology.get("layers", {"world": {}, "person": {}, "work": {}}))
    allowed_scopes = set(ontology.get("context_scopes", {}))
    allowed_mechanisms = set(ontology.get("mechanisms", {}))
    allowed_status = {"verified", "review", "candidate", "contested"}

    for i, n in enumerate(nodes):
        nid = n.get("id")
        if n.get("type") not in allowed_types:
            errors.append(f"Node {i} ({nid}) has invalid type {n.get('type')!r}")
        if not n.get("label"):
            errors.append(f"Node {i} ({nid}) is missing a label")
        if n.get("layer") is not None and n.get("layer") not in allowed_layers:
            errors.append(f"Node {i} ({nid}) has invalid layer {n.get('layer')!r}")
        if n.get("scope") is not None and allowed_scopes and n.get("scope") not in allowed_scopes:
            errors.append(f"Node {i} ({nid}) has invalid scope {n.get('scope')!r}")
        if n.get("type") == "person":
            by, dy = n.get("birth_year"), n.get("death_year")
            if by is not None and dy is not None and dy < by:
                errors.append(f"Node {i} ({nid}) has death_year before birth_year")

    for i, e in enumerate(edges):
        s, t = e.get("source"), e.get("target")
        if s not in id_set:
            errors.append(f"Edge {i} references missing source {s!r}")
        if t not in id_set:
            errors.append(f"Edge {i} references missing target {t!r}")
        if e.get("status") not in allowed_status:
            errors.append(f"Edge {i} has invalid status {e.get('status')!r}")
        c = e.get("confidence")
        if not isinstance(c, int) or not 1 <= c <= 5:
            errors.append(f"Edge {i} has invalid confidence {c!r}")
        if not e.get("relation"):
            errors.append(f"Edge {i} is missing relation")
        if not e.get("note"):
            errors.append(f"Edge {i} is missing note")
        if e.get("mechanism") is not None and allowed_mechanisms and e.get("mechanism") not in allowed_mechanisms:
            errors.append(f"Edge {i} has invalid mechanism {e.get('mechanism')!r}")

    if coverage:
        allowed_coverage_status = set(coverage.get("status_values", {}))
        allowed_source_env = set(coverage.get("source_environment_values", {}))
        for nid, item in coverage.get("nodes", {}).items():
            if nid not in id_set:
                errors.append(f"Coverage metadata references missing node {nid!r}")
            if item.get("status") not in allowed_coverage_status:
                errors.append(f"Coverage metadata for {nid} has invalid status {item.get('status')!r}")
            if item.get("source_environment") not in allowed_source_env:
                errors.append(
                    f"Coverage metadata for {nid} has invalid source_environment "
                    f"{item.get('source_environment')!r}"
                )

    return errors


def write_outputs(graph: dict) -> None:
    DIST.mkdir(exist_ok=True)
    package = {
        k: graph[k]
        for k in ("meta", "ontology", "coverage", "nodes", "edges")
    }
    (DIST / "graph.json").write_text(
        json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    node_fields = [
        "id", "label", "type", "layer", "scope", "year", "birth_year",
        "death_year", "active_start", "active_end", "culture", "description",
        "tags", "personal_seed", "influence_score", "betweenness", "descendants",
    ]
    with (DIST / "nodes.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=node_fields)
        w.writeheader()
        for n in graph["nodes"]:
            m = n.get("metrics", {})
            w.writerow({
                "id": n.get("id", ""),
                "label": n.get("label", ""),
                "type": n.get("type", ""),
                "layer": n.get("layer", ""),
                "scope": n.get("scope", ""),
                "year": n.get("year", ""),
                "birth_year": n.get("birth_year", ""),
                "death_year": n.get("death_year", ""),
                "active_start": n.get("active_start", ""),
                "active_end": n.get("active_end", ""),
                "culture": n.get("culture", ""),
                "description": n.get("description", ""),
                "tags": "|".join(n.get("tags", [])),
                "personal_seed": n.get("personal_seed", False),
                "influence_score": m.get("influence_score", ""),
                "betweenness": m.get("betweenness", ""),
                "descendants": m.get("descendants", ""),
            })

    edge_fields = [
        "source", "target", "relation", "mechanism", "evidence_class",
        "confidence", "evidence", "note", "transformation_note",
        "source_url", "source_label", "status",
    ]
    with (DIST / "edges.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=edge_fields)
        w.writeheader()
        for e in graph["edges"]:
            w.writerow({k: e.get(k, "") for k in edge_fields})


def main() -> int:
    graph = assemble()
    errors = validate(graph)
    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    write_outputs(graph)
    print(
        f"Validated {len(graph['nodes'])} nodes and {len(graph['edges'])} edges. "
        f"Wrote outputs to {DIST}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
