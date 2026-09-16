# The Ancestry of Stories — Version 0.2

A prototype **typed knowledge graph** for exploring how stories, authors, historical systems, lived experience, traditions, professions, institutions, and other media contribute to later creative work.

The project now asks:

> **What had to exist — in the world, in the creator's formation, and in earlier works — for this author or work to take the form it did?**

Version 0.2 is a major model revision built around three layers:

```text
WORLD / ENVIRONMENT
        ↓
PERSON / FORMATION
        ↓
WORK / EXPRESSION
        ↓
later creators and works
```

The arrows do not all mean the same thing. Version 0.2 separates **relationship mechanism** from **confidence**.

## Explore

`index.html` is a static interactive explorer with:

- search across works, people, traditions, contexts, and media;
- **Combined ancestry**;
- **Author formation**;
- **Work formation**;
- descendants;
- evidence-path finding;
- confidence thresholds;
- mechanism filters;
- world/person/work layer filters;
- context-detail filters for broad systems versus specific cases;
- evidence notes under **Why we think this**;
- source links;
- qualitative **research coverage** and **source environment** metadata.

The interface explicitly warns that **graph density is not cultural importance**.

## Version 0.2 model changes

### World → person → work

The graph now distinguishes:

- **world/environment** — history, institutions, language, religion, economics, technology, place, media, traditions;
- **person/formation** — reading, education, profession, mentors, travel, lived events, beliefs, creative circles;
- **work/expression** — textual sources, allusions, genre, structure, adaptation, reaction, publication history.

### Relationship mechanisms

The controlled vocabulary is in `data/ontology.json`:

- textual / explicit transmission;
- lived experience;
- historical / social context;
- intellectual / social formation;
- formal / genre inheritance;
- authorship / publication lineage;
- reaction against;
- context hierarchy;
- comparison only.

Confidence still measures the evidence supporting a claim. It does not measure importance.

### Context abstraction

Context nodes can be marked as:

- system;
- pattern;
- tradition;
- event;
- case;
- episode.

The goal is to avoid turning every biographical fact into a universal graph node while preserving specific events that genuinely matter.

Example:

```text
Resource-extraction frontier / boom economy
                ↓
Nevada mining-boom frontier
                ↓
Mark Twain
```

The first arrow means **specific case of**, not creative influence.

### Research coverage and source bias

`data/research-coverage.json` records the state of project research separately from the graph itself.

A dense English-language author dossier may partly reflect:

- rich surviving archives;
- extensive digitization;
- searchable interviews;
- English-language scholarship;
- decades of academic attention.

A sparse oral, Indigenous, colonized, working-class, non-English, children's, comics, game, or community-held tradition may reflect weaker source access rather than weaker cultural influence.

See [`docs/bias-and-coverage.md`](docs/bias-and-coverage.md).

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
│   ├── ontology.json
│   ├── research-coverage.json
│   ├── schema.json
│   ├── nodes-01.json ... nodes-12.json
│   └── edges-01.json ... edges-12.json
├── docs/
│   ├── methodology.md
│   ├── bias-and-coverage.md
│   ├── textual-reference-layer.md
│   ├── user-proposed-connections.md
│   └── version-1-roadmap.md
└── scripts/
    └── assemble_graph.py
```

The sharded JSON files remain the canonical editable data.

## Current corpus

Version 0.2 contains:

- **206 nodes**;
- **241 relationships**;
- literary works and authors;
- oral and literary traditions;
- historical events and systems;
- film, games, and media;
- professional and biographical formation;
- publication and series lineage;
- comparison-only hypotheses;
- explicit source-bias and coverage metadata.

The corpus is still a curated seed, not a representative sample of world literature.

## Evidence model

Confidence measures support for a relationship:

- **5 — explicit/direct**
- **4 — strong**
- **3 — contextual/likely lineage**
- **2 — inference**
- **1 — comparison only**

Core rule:

> **Similarity is not influence.**

The graph should preserve useful comparison without inventing transmission.

## Bias and representation

Version 0.2 adds explicit editorial constraints:

- sparse documentation is not weak cultural importance;
- non-English and community sources should be deliberately sought;
- oral variation is not treated as defective transmission;
- collectors, translators, teachers, editors, archives, and adaptations should be modeled when they mediate transmission;
- Indigenous and community-held knowledge should not be extracted merely because it is online;
- colonial or institutional archives should not silently stand in for community authority;
- archival privilege must not become a false measure of intellectual importance.

The goal is not equal node counts. The goal is to make **research attention and source access visible** and to change research priorities when the graph exposes bias.

## Data validation

Run:

```bash
python scripts/assemble_graph.py
```

The validator checks:

- manifest counts;
- duplicate IDs;
- source and target integrity;
- node types;
- optional layer and scope vocabulary;
- confidence and status;
- explicit mechanism values;
- research-coverage references and allowed values.

It also writes combined JSON/CSV exports to `dist/`.

## Website first; agent second

The website remains the inspectable public object.

A future agent can:

- translate natural-language questions into graph traversal;
- research missing claims;
- explain evidence-backed paths;
- propose candidate edges;
- identify contradictory evidence.

A model-generated claim must begin as candidate/inference and cannot verify itself.

## Planned next views

- Timeline with date ranges and elapsed time;
- expandable/collapsible context hierarchy;
- theme river / idea mutation;
- stronger path scoring;
- public proposal workflow;
- private Personal Lens over a reader's own shelf.

## Contributing

Contributions are **claims with provenance**, not attractive lines on a network.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/methodology.md`](docs/methodology.md).

## Licensing

- Code: MIT.
- Original graph metadata, summaries, annotations, and editorial notes: CC BY 4.0.
- Third-party sources remain under their original rights; the project links rather than reproduces substantial source material.

## Status

**Version 0.2.0** is an exploratory research prototype.

Its purpose is to make the model falsifiable and inspectable: test it, find where the ontology fails, expose source bias, improve the rules, and then expand the corpus under those rules.
