# Textual reference and allusion layer

Testing of *Dungeon Crawler Carl* and *The Dark Tower* showed that the graph needs to distinguish **explicit textual reference** from broad influence or genre lineage.

Examples include:
- a character explicitly comparing an event to another book, film, or television format;
- a title borrowed from an earlier work;
- quoted or paraphrased song lyrics;
- epigraphs and quotations;
- named fictional characters or objects imported from another work;
- self-reference, author self-insertion, or crossovers between works by the same author;
- recurring phrases or deliberate echoes that scholarship or the creator identifies.

These should not automatically be labeled `influenced`. A text can reference another work without that work having caused the later work to exist.

## Proposed relationship types

- `explicit_reference` — named inside the text.
- `quotation` — direct quoted material, with locators where possible.
- `title_source` — title or section title drawn from another work.
- `epigraph_source` — epigraph or chapter-heading source.
- `character_crossover` — a fictional character crosses between works.
- `shared_universe` — works occupy a documented common fictional universe.
- `self_insertion` — creator appears as a character/persona within the work.
- `musical_reference` — song/lyric is explicitly invoked.
- `allusion` — textual relationship argued by strong evidence but not explicitly named.

## Evidence rule

The interface should show both **what the text references** and **whether there is separate evidence that the referenced work influenced composition**. Those are different claims and may have different confidence scores.

Example:

`The Running Man -> Dungeon Crawler Carl` might eventually have:
1. an `explicit_reference` claim if the primary text is verified to name it;
2. a separate `influenced` claim only if Dinniman identifies it as a creative source.

Likewise, *The Dark Tower* can eventually expose its unusually dense intertextual network without treating every song lyric, quotation, fictional crossover, or cultural reference as an origin story.

## Product direction

Add an optional **References / Intertexts** lens so dense works do not overwhelm the normal ancestry graph. Users should be able to toggle these edges independently from biography, historical context, publication lineage, and influence.
