# The Ancestry of Stories — Version 0

A prototype **typed knowledge graph** for exploring why books and authors look the way they do: literary influence, reaction, adaptation, genre inheritance, biography, historical context, research, and cross-media influence.

The project asks a broader question than “what inspired this book?”:

> **What had to exist — texts, myths, ideas, media, institutions, historical events, and lived circumstances — for this author or work to take the form it did?**

## Why a graph instead of a family tree?

A family tree is a useful **view**, but a poor underlying data model. Creative inheritance is many-to-many. A novel may simultaneously inherit a mythic structure, reject a genre convention, borrow film grammar, respond to a war, and reflect an author’s education or profession.

The graph stores those claims separately so the same data can later support ancestry trees, descendant maps, timelines, author-formation dossiers, theme histories, and paths between apparently unrelated works.

## Explore Version 0

`index.html` is a static interactive explorer. It provides:

- search across works, people, traditions, contexts, and media;
- ancestry and descendant views with adjustable depth;
- confidence thresholds and the ability to hide review-stage claims;
- a path finder between two entities;
- evidence/source inspection for individual relationships;
- an **example reader shelf** showing how a personal reading history can become an entry point into the larger graph.

The page loads the graph from the JSON files in `data/`, so it should be served over HTTP rather than opened directly from the filesystem. GitHub Pages is sufficient for the prototype.

## Repository structure

```text
ancestry-of-stories/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── DATA_LICENSE.md
├── index.html
├── data/
│   ├── manifest.json
│   ├── meta.json
│   ├── nodes-01.json ... nodes-05.json
│   ├── edges-01.json ... edges-05.json
│   └── schema.json
├── docs/
│   └── methodology.md
└── scripts/
    └── assemble_graph.py
```

The **sharded JSON files are the editable source data**. `data/manifest.json` defines the current package and expected counts. Running `scripts/assemble_graph.py` validates the shards and generates convenient combined JSON/CSV exports in `dist/`.

```bash
python scripts/assemble_graph.py
```

The script uses only Python’s standard library.

## Evidence model

Confidence is **not literary importance**. It describes confidence in the claimed relationship.

- **5 — explicit / direct:** creator statement, direct adaptation, authorship, or comparably direct evidence.
- **4 — strong:** well-established textual, scholarly, or biographical evidence with relatively little uncertainty.
- **3 — contextual / likely lineage:** a well-motivated relationship whose causal strength may be diffuse.
- **2 — inference:** plausible and worth investigating, but not established.
- **1 — comparison only:** useful similarity; explicitly *not* evidence of transmission.

`status=review` marks a relationship that still needs a better source, more precise formulation, or editorial review before being treated as publication-grade.

### Core rule

**Never collapse similarity into influence.**

The graph should be able to preserve an interesting resemblance while also saying plainly that there is no evidence the later creator encountered the earlier source.

## Version 0 seed corpus

Version 0 contains:

- **122 nodes**;
- **128 typed relationships**;
- ancient epics, scripture, philosophy, drama, medieval traditions, the modern novel, modernism, dystopia, Westerns, fantasy, science fiction, film, games, MMORPG culture, and LitRPG;
- explicit creator statements alongside scholarly/contextual claims and deliberately labeled hypotheses.

It is a curated seed rather than a representative sample of world literature. It is Western- and English-language-heavy in places, and that bias should be corrected through subsequent expansion rather than hidden.

## What this could become

A larger graph could support questions such as:

- Which obscure works repeatedly appear upstream of major authors?
- Which works act as bridges between genres, cultures, or media?
- Which themes persist for centuries, and how does their meaning change?
- Where is an author deliberately **reacting against** an inherited convention rather than copying it?
- What biographical or historical circumstances repeatedly sit beside particular creative concerns?
- What is the strongest evidence-backed path between two apparently unrelated works?
- Which sources are unusually common among writers despite being relatively obscure among general readers?

The last question motivates a future feature described in the methodology as **The Obscure Shelf**.

## Website first; agent second

The public website should remain the inspectable object: readers need to see the claims, uncertainty, and sources themselves.

A future natural-language agent can sit on top of the graph to translate questions into traversal and retrieval operations, explain evidence-backed paths, and propose candidate connections. An AI-generated connection should begin as a hypothesis; it should never silently promote its own inference into a verified claim.

See [`docs/methodology.md`](docs/methodology.md) for the full editorial and technical direction.

## Contributing

Contributions should add **claims with provenance**, not merely attractive lines on a network diagram. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the evidence rubric and review rules.

Missing edges mean **not yet represented**, not “no relationship exists.” Competing interpretations should be preserved rather than flattened into one answer.

## Publishing the prototype

Because the repository already contains a root `index.html`, it can be hosted directly with GitHub Pages. In the repository’s GitHub settings, configure **Pages** to deploy from the `main` branch at the repository root.

## Licensing

- Software/code: [MIT License](LICENSE).
- Original graph metadata, summaries, relationship annotations, and editorial notes: [CC BY 4.0](DATA_LICENSE.md).
- Third-party works and source material retain their original rights; this project generally links to evidence rather than reproducing it.

## Status

**Version 0.1.0** is an exploratory research prototype. Its purpose is to make the model testable: ask questions of it, identify where it fails, improve the ontology and evidence, and expand outward from there.
