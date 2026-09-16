#!/usr/bin/env python3
"""Assemble and validate The Ancestry of Stories Version 0 data shards."""

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
    nodes = []
    for name in manifest["nodes"]:
        nodes.extend(load_json(DATA / name))
    edges = []
    for name in manifest["edges"]:
        edges.extend(load_json(DATA / name))
    return {"meta": meta, "nodes": nodes, "edges": edges, "manifest": manifest}


def validate(graph: dict) -> list[str]:
    errors: list[str] = []
    nodes = graph["nodes"]
    edges = graph["edges"]
    manifest = graph["manifest"]

    ids = [n.get("id") for n in nodes]
    id_set = set(ids)

    if len(ids) != len(id_set):
        errors.append("Duplicate node IDs found")
    if len(nodes) != manifest["counts"]["nodes"]:
        errors.append(f"Node count mismatch: {len(nodes)} != {manifest['counts']['nodes']}")
    if len(edges) != manifest["counts"]["edges"]:
        errors.append(f"Edge count mismatch: {len(edges)} != {manifest['counts']['edges']}")

    allowed_types = {"work", "person", "tradition", "context", "medium"}
    for i, n in enumerate(nodes):
        if n.get("type") not in allowed_types:
            errors.append(f"Node {i} ({n.get('id')}) has invalid type {n.get('type')!r}")
        if not n.get("label"):
            errors.append(f"Node {i} ({n.get('id')}) is missing a label")

    for i, e in enumerate(edges):
        s, t = e.get("source"), e.get("target")
        if s not in id_set:
            errors.append(f"Edge {i} references missing source {s!r}")
        if t not in id_set:
            errors.append(f"Edge {i} references missing target {t!r}")
        if e.get("status") not in {"verified", "review"}:
            errors.append(f"Edge {i} has invalid status {e.get('status')!r}")
        c = e.get("confidence")
        if not isinstance(c, int) or not 1 <= c <= 5:
            errors.append(f"Edge {i} has invalid confidence {c!r}")
        if not e.get("relation"):
            errors.append(f"Edge {i} is missing relation")
        if not e.get("note"):
            errors.append(f"Edge {i} is missing note")

    return errors


def write_outputs(graph: dict) -> None:
    DIST.mkdir(exist_ok=True)
    package = {k: graph[k] for k in ("meta", "nodes", "edges")}
    (DIST / "graph.json").write_text(
        json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    node_fields = [
        "id", "label", "type", "year", "culture", "description", "tags",
        "personal_seed", "influence_score", "betweenness", "descendants",
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
                "year": n.get("year", ""),
                "culture": n.get("culture", ""),
                "description": n.get("description", ""),
                "tags": "|".join(n.get("tags", [])),
                "personal_seed": n.get("personal_seed", False),
                "influence_score": m.get("influence_score", ""),
                "betweenness": m.get("betweenness", ""),
                "descendants": m.get("descendants", ""),
            })

    edge_fields = [
        "source", "target", "relation", "confidence", "evidence", "note",
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
