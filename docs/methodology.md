# Methodology

## Core question

**What had to exist — books, myths, ideas, institutions, technologies, historical events, personal experiences, artistic conventions, and other media — for a particular author or work to become possible in the form we know?**

The Ancestry of Stories is not primarily a recommendation engine. It is a provenance and interpretation system for creative culture.

## Why the database is a graph

A family tree is a useful *view* but a poor *data model*. Creative inheritance is many-to-many. A novel may simultaneously adapt an older work, reject a genre convention, borrow film grammar, inherit a mythic structure indirectly, respond to a war, and reflect an author’s education or profession.

Those relationships must remain distinct edges. The interface can then render a tree, constellation, timeline, path, dossier, or thematic flow depending on the question.

## The project should answer five families of questions

1. **Ancestry** — What sources stand behind this work or author?
2. **Descendants** — Where did this work, style, or idea travel next?
3. **Bridges** — What connects two apparently unrelated works, movements, or media?
4. **Persistence** — Which themes, narrative structures, anxieties, and metaphors recur across centuries, and how do their meanings change?
5. **Hidden infrastructure** — Which obscure books, academic disciplines, translations, games, films, religious traditions, or subcultures repeatedly appear behind famous works?

## The unit of knowledge is a claim

Every non-trivial edge should eventually contain:

- source entity;
- target entity;
- relationship type;
- concise claim text;
- evidence class;
- confidence;
- supporting source or sources;
- relevant locator or excerpt where licensing permits;
- contributor;
- review state;
- creation/revision timestamps;
- optional counterevidence or competing interpretation.

Version 0 does not yet contain all of these fields, but its schema is designed to evolve in this direction.

## Evidence classes

### Explicit
A creator directly identifies an influence, intention, source, reaction, or formative experience.

### Direct textual
Adaptation, quotation, named allusion, demonstrable reuse, or another close textual relationship.

### Biographical
Letters, diaries, education, library/reading records, profession, travel, relationships, wartime service, or other documented circumstances.

### Scholarly
Reputable scholarship argues the relationship. The project should retain attribution rather than presenting interpretation as self-evident fact.

### Historical context
A documented circumstance relevant to formation or subject matter. Context must not be converted automatically into psychological causation.

### Inferred
Chronology, access, and unusually specific similarities make a hypothesis plausible. These edges are useful precisely because they are labeled as hypotheses.

### Comparison only
A useful resemblance with no transmission claim. This category is essential for exploratory questions without laundering similarity into influence.

### Contested
Substantial competing accounts are preserved rather than collapsed into a single authoritative line.

## Confidence rubric

Confidence measures support for the **relationship**, not the importance of the source or target.

- **5 — explicit/direct:** creator statement, direct adaptation, authorship, or comparably direct evidence.
- **4 — strong:** well-established textual, scholarly, or biographical evidence with relatively little uncertainty.
- **3 — contextual/likely lineage:** a well-motivated relationship whose causal strength is diffuse.
- **2 — inference:** plausible and worth investigating, but not established.
- **1 — comparison only:** useful similarity; never evidence of transmission by itself.

`status=review` means the claim needs a stronger source, more exact formulation, or explicit editorial review before it should be treated as publication-grade.

## Editorial guardrails

1. **Similarity is not influence.**
2. Chronology is necessary but not sufficient evidence.
3. “The culture influenced the author” is too vague; encode a concrete circumstance or omit it.
4. Do not psychologize a creator from biography. Record documented experiences and interpretations separately.
5. Preserve contradictory scholarship and creator accounts.
6. Separate work-level influence from author-level influence.
7. Translations and intermediary adaptations deserve nodes when they materially mediate transmission.
8. Absence of an edge means “not yet represented,” not “no relationship exists.”
9. Centrality metrics describe the sampled graph, not objective literary importance.
10. Every substantive public claim should ultimately expose its provenance in one click.

## Public views

### Constellation
Free network exploration for clusters, bridge nodes, and unexpected media/cultural connections.

### Ancestry
Incoming paths to a selected node, with user-controlled depth and evidence threshold.

### Descendants
The reverse view: where a work, author, technique, or tradition travels downstream.

### Timeline
Chronology helps prevent impossible influence claims and reveals bursts of reuse after translation, adaptation, war, or technological change.

### Why this work?
A readable evidence dossier: strongest explicit sources first, then biography/context, then scholarship, then inference.

### Path finder
“Connect *The Odyssey* to *Dungeon Crawler Carl*.” The best path is not necessarily the mathematically shortest. A future scorer should combine evidence strength, path length, relationship diversity, and temporal plausibility.

### Theme river
Track motifs such as descent, apocalypse, doubles, forbidden knowledge, frontier, memory, artificial persons, or reluctant heroism through time, while distinguishing persistence from independent reinvention.

### Author formation
For a person rather than a work: childhood reading, schooling, languages, profession, wars, places, intellectual circles, religious/philosophical formation, artistic media, and stated influences.

## Website first; agent second

The public website should remain the inspectable object because users need to see and audit claims. A natural-language agent can later translate questions into graph and retrieval operations, explain evidence-backed paths, and propose candidate edges.

A model-generated connection must begin life as **candidate/inferred**. Language generation cannot upgrade its own claim to verified status.

## Long-term architecture

Version 0 is static HTML plus JSON shards. This keeps the concept easy to inspect and fork.

A later public version can use:

- PostgreSQL for entities, claims, sources, contributors, and revision history;
- recursive SQL for graph traversal initially;
- full-text search over claims and evidence notes;
- embeddings over source excerpts for discovery, never truth assignment;
- a web graph library such as Cytoscape.js, Sigma.js, D3, or Vis Network;
- a read-only public API and bulk exports;
- human moderation and citation review for contributed claims.

A dedicated graph database should be added only if traversal scale or path scoring warrants the operational complexity.

## Discovery sources

Candidate edges can be discovered through Wikidata, OpenAlex, library catalogs, authority files, archival finding aids, biographies, criticism, interviews, letters, diaries, lectures, and creator estates. Discovery is not verification.

Source preference is:

1. primary creator source;
2. estate, archive, scholarly edition, or institutional record;
3. peer-reviewed or university-press scholarship;
4. high-quality biography or criticism;
5. reliable journalism/interview;
6. reference databases as discovery tools.

## A long-term feature: The Obscure Shelf

The graph can eventually identify upstream nodes that are unusually frequent in creator-to-creator paths, relatively obscure in general readership, strongly evidenced, and structurally important as bridges. This can surface books, translations, academic texts, games, magazines, myths, or other sources that writers repeatedly encounter even when general audiences do not.

## Version 0 limitations

Version 0 is a curated seed, not a representative sample. It is Western- and English-language-heavy in places, uses approximate dates for some traditions, includes review-level claims, and contains exploratory metrics. These limitations should remain visible while the corpus expands.

The prototype succeeds if it causes a user to ask a better next question rather than merely admire the network.
