# The Ancestry of Stories — Version 0

A prototype **typed knowledge graph** for exploring why books and authors look the way they do: literary influence, reaction, adaptation, genre inheritance, biography, historical context, research, and cross-media influence.

## Why a graph instead of a family tree?

A tree forces every work to have one parent and a single ancestry. Creative influence is many-to-many. A novel may simultaneously inherit a mythic structure, reject a genre convention, borrow a film grammar, respond to a war, and reflect an author’s profession. The graph stores those relationships separately and lets the interface generate tree-like views when that view is useful.

## Repository structure

- `index.html` — Version 0 interactive explorer.
- `data/graph.json` — canonical Version 0 graph package.
- `data/nodes.csv` and `data/edges.csv` — audit/edit exports.
- `data/schema.json` — JSON schema for the graph package.
- `scripts/build_v0.py` — reproducible seed-corpus builder and validator.
- `scripts/make_html.py` — prototype page generator.
- `docs/methodology.md` — evidence model, product concept, and technical direction.
- `CONTRIBUTING.md` — rules for adding and reviewing claims.

## Evidence model

Confidence is **not literary importance**. It is confidence in the claimed relationship.

- **5 — explicit / direct**: creator statement, direct adaptation, authorship, or otherwise unusually strong evidence.
- **4 — strong**: well-established scholarship, direct textual relationship, or biographical documentation.
- **3 — contextual / likely lineage**: strong interpretive or genre-historical relationship, but causal strength may be diffuse.
- **2 — inference**: plausible contextual or curatorial connection requiring caution.
- **1 — comparison only**: useful similarity; explicitly *not* evidence of transmission.

`status=review` means the edge should receive a better source or more precise formulation before an authoritative public release.

## Design rule

**Never collapse similarity into influence.** The graph must be able to retain a provocative connection while saying that we do not know whether one creator encountered the other source.

## Seed corpus

Version 0 contains 122 nodes and 128 typed relationships spanning ancient epics and scripture through modernism, dystopia, Westerns, fantasy, science fiction, games, and LitRPG. It is intentionally incomplete and Western-/English-language-heavy in places.

## Long-term direction

The website should remain the inspectable public object. A future natural-language agent can query the graph, explain evidence-backed paths, and propose candidate relationships, but it should not silently create or promote claims. See `docs/methodology.md` for the fuller project brief.

## Licensing

Code is released under the MIT License. Original graph metadata, summaries, and relationship annotations are released under CC BY 4.0. Third-party source material remains under its original copyright and is linked rather than reproduced.

## Status

This is a seed corpus, not a canonical literary history. Missing edges mean **not yet represented**, not “no relationship exists.”
