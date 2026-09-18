# Contributing claims

The unit of contribution is a **claim with provenance**, not an opinion and not simply a line on a graph.

Version 0.2 distinguishes **world/environment**, **person/formation**, and **work/expression**. Contributors should identify not only whether two things are connected, but **how the connection travels**.

## Before adding an edge

Ask:

1. What exactly is being claimed?
2. Is this textual transmission, lived experience, historical/social context, intellectual/social formation, genre/formal inheritance, authorship/publication, reaction against, context hierarchy, or comparison only?
3. Could the source plausibly precede and reach the target?
4. Is the claim about the **person** or about a **specific work**?
5. What evidence would falsify or weaken the claim?
6. Is an intermediary missing: translation, adaptation, teacher, editor, collector, archive, anthology, film, game, institution, or oral performer?
7. Is the proposed context node reusable, or is it really a biographical detail that belongs in the evidence note?
8. Are we relying on source availability rather than actual cultural importance?
9. Are there community, language, access, or archival limitations that should be made visible?

## Minimum fields

- source ID
- target ID
- relation
- mechanism when known
- evidence class when known
- confidence (1–5)
- concise explanatory note
- status (`verified`, `review`, future `candidate`/`contested`)
- supporting source URL for substantive claims unless the claim is basic metadata such as authorship

Optional but encouraged:

- `transformation_note` — what changed as the idea/form moved;
- contributor/reviewer provenance;
- date/revision metadata;
- counterevidence;
- source-language or access notes.

## Relationship mechanisms

Use the controlled mechanism vocabulary in `data/ontology.json`.

- `textual_transmission`
- `lived_experience`
- `historical_social_context`
- `intellectual_social_formation`
- `formal_genre_inheritance`
- `authorship_publication`
- `reaction_against`
- `context_hierarchy`
- `comparison`
- `other`

`context_hierarchy` means “broad process → narrower case.” It is not causal influence.

## Abstraction test

Prefer a first-class context node when it:

- recurs across multiple creators/works;
- represents a meaningful historical/cultural/institutional process; or
- is a specific event/case whose specificity is independently significant or essential to a direct work-level relationship.

Otherwise keep the fact in the edge evidence or as a narrower case beneath a broader node.

Do not let the graph become a biography database by turning every travel episode, job, town, relative, or anecdote into a universal conceptual node.

Name World/context nodes for the shared external phenomenon, not for the creator who encountered it. Put the creator-specific encounter on the edge and in the side dossier. For example: **Klondike Gold Rush → Jack London**, with London's Yukon journey explained in the relationship evidence—not a context node called “Klondike Gold Rush / London’s Yukon journey.”

## Person versus work

Do not assume that because an author experienced X, X therefore caused Work Y.

Prefer:

- `X → author` when X is documented formation;
- `X → work` only when there is evidence that X entered the work;
- both edges when both claims are independently supported.

## Confidence rubric

**5** Explicit creator statement, direct textual relation, authorship, direct adaptation, or comparably direct evidence.  
**4** Strong textual, scholarly, historical, or biographical evidence with little dispute.  
**3** Well-motivated lineage/context claim, but causal strength is diffuse.  
**2** Plausible inference worth investigating.  
**1** Comparison only. Never describe this as proven transmission.

Confidence measures support for the relationship, **not literary or cultural importance**.

## Source preference

Default order:

1. Creator, tradition-bearer, community primary source.
2. Community institution, author estate, archive, scholarly edition, or trusted cultural institution.
3. Peer-reviewed article or university-press scholarship.
4. High-quality biography or criticism.
5. Reliable journalism/interview.
6. Reference databases as discovery tools.

This is not mechanical. For living or community-held traditions, community authority may matter more than prestige of an external archive.

Do not use an unsourced wiki statement as the sole evidence for a substantive claim.

## Source-access and representation rules

Sparse evidence is not weak influence.

Before concluding a tradition or creator has few connections, consider:

- non-English scholarship;
- oral/performance transmission;
- community-held sources;
- undigitized archives;
- archival loss;
- collector/missionary/colonial mediation;
- unequal access to publishing, universities, and preservation;
- catalog and description bias.

See `docs/bias-and-coverage.md`.

## Oral, Indigenous, and community-held knowledge

- Do not flatten distinct oral traditions into a universal “oral culture.”
- Use broad transmission nodes only as abstractions; preserve specific communities/traditions beneath them.
- Prefer community-authored description and scholarship where available.
- Respect cultural protocols, restrictions, and community authority.
- Public availability does not automatically authorize republication of sensitive material.
- Model collectors, translators, editors, ethnographers, and archives when they materially mediate transmission.
- If only an external/colonial archive is available, say so.

## Contested claims

Do not “resolve” a dispute by deleting one interpretation. Preserve competing claims or counterevidence and label the relationship contested.

## Negative findings

Do not encode “no influence” simply because a search found nothing.

A defensible negative finding must record what source set, languages, archives, and search scope were actually reviewed.

## Language

Prefer:

- “X explicitly cited Y.”
- “The work directly reuses…”
- “The author had read…”
- “Scholar Z argues…”
- “This event forms documented historical context…”
- “This is a specific case within…”
- “Version 0.2 treats this as a comparison.”

Avoid:

- “X obviously stole from Y.”
- “This proves…”
- “The culture made the author…”
- biographical mind-reading;
- language that treats sparse documentation as cultural absence.
