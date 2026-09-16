# User-proposed connections — Version 1 design

A core future feature should let a reader create a candidate relationship directly from the graph without allowing an unsourced suggestion to become graph truth automatically.

## Proposed interaction

1. User selects a source node and target node in the visualization.
2. User chooses or suggests a relationship type.
3. User writes **Why I think this** in plain language.
4. User may attach one or more URLs, citations, interviews, page references, or other supporting evidence.
5. Submission enters a **candidate** queue. It is not displayed as verified influence.
6. A research/review process checks chronology, access, source quality, competing interpretations, and whether the relationship type is correctly framed.
7. Reviewer assigns an evidence class, confidence level, and status, or rejects/rewrites the candidate.
8. Accepted claims are versioned into the public graph with contributor/reviewer provenance.

## Important design rule

The system should preserve the contributor's reasoning separately from the editorial conclusion. A user may notice a meaningful relationship even when the final classification changes from `influenced` to `parallel`, `genre_lineage`, `historical_context`, or another more defensible relationship type.

## Version 0 implementation constraint

The current site is static GitHub Pages. It can render a proposal form, but safely accepting arbitrary public submissions requires either:

- GitHub Issues/Discussions as an interim submission queue; or
- a small authenticated/serverless API and datastore for non-GitHub users.

The eventual agent/reviewer should be able to research candidate claims and recommend confidence, but it must not silently promote its own inference to verified status.
