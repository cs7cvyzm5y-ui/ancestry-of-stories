# Version 1 roadmap

## Contribution workflow

- Add a **Propose connection** action from selected graph nodes.
- Capture source node, target node, proposed relationship type, contributor reasoning, and optional supporting sources.
- Store submissions as `candidate` claims rather than verified graph edges.
- Add research/review tooling that checks chronology, access, primary/secondary sources, competing explanations, and relationship framing.
- Preserve the contributor's original reasoning even when editorial review changes the relationship type or confidence.
- Record contributor, reviewer, timestamps, and revision history.
- Support rejection or conversion to `parallel` / `comparison only` without discarding the original observation.

## Evidence UX

- Continue expanding **Why we think this** as the primary human-readable explanation for every edge.
- Distinguish confidence score from evidence class and source quality.
- Permit multiple supporting sources and counterevidence.
- Make publication sequence, authorship, shared-universe links, historical context, and creative influence visually distinct.

## Public submission architecture

The static GitHub Pages prototype cannot securely write arbitrary public submissions directly into the graph. Two plausible paths are:

1. GitHub Issues/Discussions as an interim queue for contributors with GitHub accounts.
2. A small authenticated/serverless submission API for a general public audience, with accepted claims later versioned into the repository.
