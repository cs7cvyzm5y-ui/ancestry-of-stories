# Bias, source access, and research coverage

The graph can only represent what the project has successfully found, interpreted, and sourced. That is not the same thing as what existed historically or mattered culturally.

## The central warning

**Graph density is not cultural importance.**

A dense Tolkien or Hemingway dossier may partly reflect unusually rich surviving archives, digitized scholarship, English-language accessibility, major institutional collections, and decades of academic attention.

A sparse oral, Indigenous, colonized, working-class, non-English, children's, popular, or community-held tradition may reflect the opposite source environment rather than weaker creative influence.

Version 0.2 records research coverage separately from graph centrality.

## Common visibility biases

### Digitization bias
Search engines and AI-assisted research favor sources that have been digitized, indexed, OCR'd, and made publicly accessible.

### Language bias
The current project is strongest in English-language research. Translated scholarship and sources in original languages require deliberate review rather than assuming English search results are representative.

### Archive-survival bias
Letters, notebooks, personal libraries, drafts, publishing contracts, and interviews survive unevenly. Famous, wealthy, institutionally connected, or heavily studied creators may leave much denser paper trails.

### Collector bias
Archives reflect what collectors, ethnographers, missionaries, universities, governments, and publishers chose to record and preserve.

The Library of Congress notes that its Indigenous ethnographic collections have uneven geographic and demographic coverage reflecting the history of documentary efforts, including underrepresentation of some regions, women, children, and communities:
https://guides.loc.gov/indigenous-peoples-of-the-Americas-folklife/ethnographic-collections

### Consent and authority
The Library of Congress American Folklife Center describes ethnographic documentation as the intellectual property of communities of origin and notes that community restrictions can govern access and use:
https://guides.loc.gov/indigenous-peoples-of-the-Americas-folklife/ethnographic-collections

Its Ancestral Voices project emphasizes co-curation, community-authored description, Traditional Knowledge labels, community-specific access protocols, and tribal cultural authority:
https://www.loc.gov/collections/ancestral-voices/about-this-collection/
https://www.loc.gov/collections/ancestral-voices/about-this-collection/rights-and-access/

### Oral-transmission bias
UNESCO emphasizes that oral traditions transmit knowledge, cultural values, language, and collective memory through living performance and intergenerational transmission. Variation is inherent rather than a defect:
https://ich.unesco.org/en/oral-traditions-and-expressions-00053

A printed collector's edition may therefore be only one mediated snapshot of a much larger living tradition.

### Description bias
Historical catalog records and archival descriptions themselves can carry the language, values, and blind spots of their creators. Smithsonian Libraries and Archives explicitly acknowledges embedded biases in historical materials and description:
https://librariesarchives.si.edu/statement-on-harmful-content-2/

## Research coverage metadata

`data/research-coverage.json` stores project-level research state.

It is deliberately separate from nodes and centrality metrics.

### Status

- `unassessed` — no structured dossier review yet.
- `seed` — starter claims only.
- `partial` — several major dimensions researched, important gaps remain.
- `substantial` — multiple dimensions and source types reviewed; still not exhaustive.

### Source environment

- `digitally_rich` — many strong sources are accessible in currently covered languages.
- `mixed` — good sources exist but important languages, formats, archives, or community perspectives remain under-reviewed.
- `limited` — current project access is weak; targeted non-digital, oral, community, translated, or specialist research is needed.
- `unknown` — not assessed.
- `not_applicable` — framework node rather than a creator/work dossier.

These labels assess **our access**, never the creator or culture.

## Minimum dossier questions

A mature author dossier should consider, where relevant:

- documented reading and named influences;
- languages and translations;
- childhood and family storytelling;
- education;
- religion/philosophy;
- profession;
- place and landscape;
- war, migration, displacement, or other lived events;
- creative circles and mentors;
- media and artistic forms beyond literature;
- historical/economic/social systems;
- major works and work-specific sources;
- downstream influence;
- non-English scholarship;
- community-authored or oral sources;
- known archival silences.

Not every category belongs to every author.

## Community-sensitive research rules

1. Community knowledge is not raw material merely because it is online.
2. Do not reproduce restricted, sacred, ceremonial, or culturally sensitive material simply because an archive exposes it.
3. Prefer community-authored description and scholarship where available.
4. Model collectors, translators, editors, and archives when they mediate what later audiences receive.
5. Record when an external archive is standing in for a community voice.
6. Do not flatten distinct communities into broad civilizational categories for visual neatness.
7. When access is limited, say so rather than filling the gap with inference.
8. When culturally appropriate interpretation is beyond the project's competence, preserve the source and uncertainty rather than pretending authority.

## Expansion audit

Before a major corpus expansion, ask:

- Are English-language writers accumulating edges faster because they are easier to research?
- Are men receiving richer biography because their correspondence and careers were historically better archived?
- Are children's literature, comics, genre fiction, fan culture, games, and oral narrative being treated as less serious sources?
- Are traditions being named through outsiders rather than their own communities?
- Are colonized cultures represented mainly through colonial records?
- Are translations invisible?
- Are women, queer creators, disabled creators, working-class creators, and writers outside dominant publishing centers appearing mainly as downstream recipients rather than upstream sources?
- Are historical systems being represented only from the perspective of the socially dominant group?
- Are we mistaking the absence of searchable evidence for evidence of absence?

The answer should change research priorities, not produce a cosmetic diversity quota.

## What fairness means for this project

The objective is not to force every tradition to have the same number of nodes or edges.

The objective is to make differences in **evidence availability and research attention visible**, deliberately seek sources outside the easiest digital channels, preserve culturally specific structures, and avoid turning archival privilege into a false measure of intellectual importance.
