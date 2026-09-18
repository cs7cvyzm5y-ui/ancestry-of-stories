# Methodology

## Core question

**What had to exist — stories, myths, languages, institutions, technologies, historical systems, lived experiences, artistic conventions, and other media — for a particular creator or work to become possible in the form we know?**

The Ancestry of Stories is a provenance and interpretation system for creative culture. It is not primarily a recommendation engine and it is not a biography database.

Version 0.2 formalizes a three-layer model:

```text
THE WORLD
history · institutions · place · language · religion · economy
technology · media · artistic traditions · social structures
                         ↓
THE PERSON
reading · education · profession · mentors · circles · travel
lived experience · beliefs · artistic practice · language
                         ↓
THE WORK
sources · allusions · structure · genre · characters · style
adaptation · rejection · publication history · recombination
```

Works then enter the world of later creators. Cultural transmission is therefore a loop, not a one-way family tree.

## Why a graph

Creative inheritance is many-to-many. A work may simultaneously quote an older text, reject a convention, inherit a genre form, respond to a war, transform a religious story, borrow game mechanics, and draw on an author's profession.

The graph stores these as separate claims so the same evidence can support different views: ancestry, descendants, author formation, work formation, timeline, pathfinding, and theme history.

## The three layers

### World / environment

This layer contains conditions larger than one creator:

- historical systems and events;
- institutions and professions;
- places and migration systems;
- languages and translation environments;
- religions and philosophies;
- oral and literary traditions;
- economic and labor structures;
- technologies and media;
- artistic movements and genre conventions.

World nodes are not automatically causes. They establish the environment in which transmission or formation may occur.

### Person / formation

A creator is a first-class node because stories often travel through human formation before entering a specific work.

Relevant evidence can include:

- documented reading;
- education and languages;
- profession;
- mentors, editors, teachers, and creative circles;
- religion or philosophy;
- travel and migration;
- military service and historical events personally experienced;
- family storytelling;
- artistic practice in other media;
- creator statements about formative experiences.

Biography should not be converted into psychological mind-reading. A documented experience can be represented without claiming that it caused a theme or personality trait.

### Work / expression

A work is where material becomes inspectable as expression.

Work-level claims include:

- direct influence;
- adaptation;
- quotation and allusion;
- title sources;
- research sources;
- formal or genre models;
- character or plot models;
- reaction against;
- explicit cross-media borrowing;
- publication and series lineage.

A circumstance that shaped the person does not automatically get a direct arrow to every work. Work-level edges require work-level evidence.

## Relationship mechanisms

Confidence answers **how well supported is this relationship?**

Mechanism answers **how does this relationship travel?**

Version 0.2 uses the controlled vocabulary in `data/ontology.json`.

### Textual / explicit transmission

The creator or work encounters, names, quotes, adapts, alludes to, reuses, or otherwise demonstrably receives material from an earlier source.

### Lived experience

A documented circumstance personally experienced by a creator.

Examples: wartime service, migration, a profession practiced, a specific family experience.

This records contact with the experience, not an inferred psychological consequence.

### Historical / social context

A system or condition relevant to a creator or work: colonial rule, slavery, industrial agriculture, economic crisis, legal structure, migration system, or historical setting.

### Intellectual / social formation

Education, profession, mentorship, creative circles, religion, philosophy, editorial environments, and institutions that shape practice.

### Formal / genre inheritance

Transmission of form: genre conventions, narrative structures, stylistic practice, performance forms, or compositional techniques.

### Authorship / publication lineage

Authorship, serialization, collection, series order, publication history, and same-author continuity.

These are lineage facts, not claims that a creator influenced themself.

### Reaction against

A creator is shaped by resisting, reversing, parodying, rebutting, or departing from an earlier source or convention.

Negative influence is still influence when documented.

### Context hierarchy

A broad process contains a narrower historical case.

Example:

```text
Resource-extraction frontier / boom economy
                    ↓
Nevada mining-boom frontier
                    ↓
Mark Twain
```

The first arrow is abstraction, not influence.

### Comparison

A useful resemblance without evidence of transmission.

Comparison edges are exploratory and must never be silently promoted to influence.

## Abstraction and context-node discipline

One of the easiest ways to corrupt the graph is to turn every interesting biographical fact into a green context bubble.

Version 0.2 assigns context scope where useful:

- **system** — large historical, institutional, economic, or cultural structure;
- **pattern** — recurring process seen in multiple places or creators;
- **tradition** — ongoing cultural, linguistic, religious, oral, artistic, or intellectual transmission;
- **event** — historically significant event that deserves independent representation;
- **case** — specific local manifestation of a broader system or pattern;
- **episode** — narrow one-person event retained only when it materially clarifies a documented claim.

### Promotion test

Prefer a first-class context node when at least one of these is true:

1. it recurs across multiple creators or works;
2. it represents a meaningful historical, cultural, institutional, or artistic process;
3. it is a specific event whose independent historical significance matters;
4. the specificity is necessary to explain a direct work-level relationship.

Otherwise keep the detail inside an evidence note or beneath a broader node.

**Label the world, not the biography.** A history/context node should be named for the external event, system, place-based process, or tradition itself. For example, use **Klondike Gold Rush**, not “Klondike Gold Rush / London’s Yukon journey.” London’s participation belongs on the relationship to London and in his person dossier. A one-person episode that lacks independent historical or cultural significance should normally not be a World node at all.

This preserves biography without allowing biography to become the ontology.

## Mediators matter

Creative transmission often does not run directly from old source to new creator.

Important intermediary nodes can include:

- translations;
- anthologies;
- teachers;
- editors;
- collectors;
- oral performers;
- religious institutions;
- schools;
- archives;
- film adaptations;
- games;
- criticism;
- fan communities.

When a mediator materially changes what later audiences receive, it should be represented rather than erased.

## Transformation, not just transmission

A future mature edge should be able to say not only that material traveled, but **what changed in transit**.

Examples include:

- a religious story becoming a secular family structure;
- medieval quest conventions becoming modern obsession or metafiction;
- a mythic figure becoming a science-fictional or superhero-like character;
- frontier history becoming frontier mythology.

Version 0.2 adds an optional `transformation_note` field for this purpose.

## Evidence classes

### Explicit

A creator, tradition-bearer, or other authoritative primary source directly identifies the influence, intention, reaction, or formative relationship.

### Direct textual

Quotation, adaptation, named allusion, title source, demonstrable reuse, or similarly close textual relation.

### Biographical

Letters, diaries, education, profession, travel, relationships, military service, interviews, or other documented life circumstances.

### Scholarly

Reputable scholarship argues the relationship. Interpretation should remain attributed where appropriate.

### Historical context

A documented circumstance relevant to formation, setting, or subject matter.

### Inferred

Chronology, access, and unusually specific similarities make a hypothesis plausible but not established.

### Comparison

Similarity only.

### Contested

Substantial competing accounts remain and should be preserved.

## Confidence rubric

Confidence measures support for the **relationship**, never literary importance.

- **5 — explicit/direct:** creator statement, direct adaptation, authorship, direct textual relation, or comparably direct evidence.
- **4 — strong:** well-established textual, historical, scholarly, or biographical evidence with relatively little uncertainty.
- **3 — contextual/likely lineage:** well-motivated relationship whose causal force is diffuse.
- **2 — inference:** plausible and worth investigating.
- **1 — comparison only:** useful similarity; not evidence of transmission.

`status=review` means the claim needs stronger sourcing or tighter formulation.

The schema also reserves `candidate` and `contested` for later contribution workflows.

## Research coverage is separate from cultural importance

The graph is vulnerable to a major representational error: mistaking **what is easy to research** for **what mattered most**.

A heavily studied English-language writer may have:

- digitized letters;
- searchable interviews;
- major biographies;
- university archives;
- established scholarly editions;
- decades of criticism.

A creator or tradition outside that archival environment may have oral transmission, undigitized material, scholarship in languages not yet reviewed, community-held knowledge, archival loss, or records produced mainly by outsiders.

A denser graph therefore does not imply richer ancestry or greater cultural importance.

`data/research-coverage.json` records the project's research state separately from graph metrics.

Coverage status is qualitative:

- `unassessed`;
- `seed`;
- `partial`;
- `substantial`.

Source environment is also qualitative:

- `digitally_rich`;
- `mixed`;
- `limited`;
- `unknown`;
- `not_applicable`.

These describe **our access and research**, not the culture or creator.

See `docs/bias-and-coverage.md`.

## Source bias and cultural responsibility

The project is currently being built through an English-speaking, U.S.-based research workflow. That creates predictable bias.

Expansion should actively check for:

- English-language search bias;
- digitization bias;
- archival survival bias;
- canon bias;
- gender and class bias in preserved correspondence;
- colonial and missionary collecting bias;
- catalog-description bias;
- underrepresentation of children's literature, comics, games, oral narrative, fan culture, and popular genre;
- traditions represented mainly through outsiders;
- translations disappearing from the transmission chain;
- Indigenous or community-held knowledge treated as freely extractable because it appears online.

### Oral and community-held traditions

A printed collection is not automatically equivalent to the living tradition from which material was gathered.

Where relevant:

- preserve specific communities and genres;
- model collectors, translators, and archives as mediators;
- prefer community-authored description and scholarship;
- respect cultural protocols and restrictions;
- do not reproduce sensitive or restricted material merely because an institution digitized it;
- identify when external archives are standing in for community voices;
- record uncertainty rather than filling source gaps with inference.

## Negative findings and missing edges

Absence of an edge means **not yet represented**, not “no relationship exists.”

A defensible negative finding must record the search scope: languages, archives, source types, and time period reviewed.

“No evidence found in currently reviewed English-language digital sources” is different from “there was no influence.”

## Dossier coverage standard

A mature author dossier should consider, where relevant:

- documented reading;
- childhood and family storytelling;
- languages and translations;
- education;
- religion and philosophy;
- profession;
- place and landscape;
- class and economic setting;
- war, migration, displacement, or other lived events;
- mentors and creative circles;
- other artistic media;
- historical systems;
- major works and work-specific sources;
- downstream influence;
- non-English scholarship;
- community-authored or oral sources;
- archival silences.

Not every category applies to every creator.

## Editorial red-team review

As the graph grows, expansion alone becomes dangerous. Periodic adversarial review should ask:

- Which edges are overclaimed?
- Which context nodes are too narrow?
- Which nodes are doing too much conceptual work?
- Which paths violate chronology?
- Which relationship types are used inconsistently?
- Which dense nodes are artifacts of archival privilege?
- Which traditions appear isolated because the project has not reviewed their languages or source environments?
- Which mediators are missing?
- Where has a specific case been mistaken for a universal category?
- Where has similarity been laundered into influence?

The graph should be able to criticize its own structure.

## Public views

### Combined ancestry

All supported upstream mechanisms under the current filters.

### Author formation

Focuses on the person: world, reading, profession, mentors, lived experience, and intellectual formation.

### Work formation

Focuses on the work: direct sources, formal inheritance, reaction, publication lineage, and authorship.

### Descendants

Where a work, person, tradition, or technique travels downstream.

### Timeline

Planned view that places the same claims on chronological lanes, preserving date ranges and elapsed time.

### Why this work?

Evidence-first dossier: strongest direct claims, formation, context, scholarship, inference.

### Path finder

The strongest explanatory path is not necessarily the shortest path. Future path scoring should consider evidence strength, relationship mechanism, path length, chronology, and interpretive usefulness.

### Theme river

Track an idea or motif through time while recording how its meaning changes.

## Website first; agent second

The public graph should remain inspectable. Readers need to see claims, evidence, uncertainty, research gaps, and source access.

A future natural-language agent can:

- translate questions into graph traversal;
- explain evidence-backed paths;
- identify missing context;
- propose candidate connections;
- search for contradictory evidence.

It must not verify its own generated claim.

## Long-term architecture

Version 0.2 remains static HTML plus JSON shards so the ontology stays easy to inspect and fork.

A later version may use:

- PostgreSQL for entities, claims, sources, contributors, revisions, and coverage;
- recursive SQL for graph traversal;
- full-text search over evidence;
- embeddings for discovery only, never truth assignment;
- human moderation;
- public API and bulk export;
- provenance-aware contribution workflow.

A graph database is unnecessary until traversal or path-scoring scale justifies it.

## Long-term analytic features

### The Obscure Shelf

Find upstream works or traditions that are structurally important to documented creator paths but less prominent in general readership.

### Idea mutation

Trace how a motif or structure changes meaning across generations rather than merely counting reuse.

### Research-bias audit

Compare graph density with coverage metadata to identify where the corpus may be reflecting source access instead of cultural history.

## Version 0.2 limitations

Version 0.2 is still a curated seed.

It remains:

- Western- and English-language-heavy;
- uneven in dossier depth;
- dependent on accessible digital research;
- incomplete in translations and intermediary transmission;
- incomplete in oral and community-authored sources;
- exploratory in its abstraction hierarchy;
- not a representative sample of world literature.

The prototype succeeds if it helps a reader ask a better question and understand why the graph believes a connection — while still making it easy to disagree.
