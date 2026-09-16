# Model architecture — Version 0.2

Version 0.2 changes the project from a mostly flat influence graph into a layered cultural-transmission model.

## 1. Layers

```text
WORLD / ENVIRONMENT
        ↓
PERSON / FORMATION
        ↓
WORK / EXPRESSION
```

A later work then becomes part of the world encountered by future creators.

### World

History, institutions, language, religion, economy, technology, place, traditions, media, and social structures.

### Person

Reading, schooling, profession, mentors, creative circles, travel, lived events, beliefs, and artistic practice.

### Work

Specific creative expression: quotation, allusion, adaptation, form, structure, title, genre, publication history, and reaction.

## 2. Mechanism and confidence are orthogonal

A confidence-5 edge can be:

- authorship;
- lived experience;
- explicit influence;
- historical setting;
- publication lineage;
- context hierarchy.

The number does not say *what kind* of relationship exists.

Version 0.2 therefore exposes a mechanism filter.

## 3. Abstraction hierarchy

Specific biography and broad historical structure coexist without being confused.

Example:

```text
Resource-extraction frontier / boom economy     [pattern]
                    ↓
Nevada mining-boom frontier                     [case]
                    ↓
Mark Twain                                      [person]
```

The broad node can also contain:

```text
Resource-extraction frontier / boom economy
                    ↓
Klondike Gold Rush
                    ↓
Jack London
```

This allows a reader to discover a recurring structure while retaining the local historical case.

## 4. Node-promotion rule

Do not create a first-class context node merely because a fact is interesting.

Promote a fact into a node when it is:

- reusable across multiple creators or works;
- a meaningful historical/cultural/institutional process;
- an independently significant historical event; or
- necessary to explain a direct work-level relationship.

Otherwise preserve it in evidence.

## 5. Work formation versus author formation

The same source can touch different layers.

```text
World War I → Hemingway
```

means documented lived experience.

```text
World War I → A Farewell to Arms
```

requires separate evidence that the war entered the work.

A user should be able to inspect either question without conflating them.

## 6. Mediated transmission

Future data should represent intermediary channels when material does not travel directly:

```text
older tradition
      ↓
collector / translation / anthology / adaptation
      ↓
later creator
      ↓
new work
```

The mediator can transform meaning, access, language, selection, and authority.

## 7. Coverage is metadata, not centrality

`research-coverage.json` describes what this project has actually investigated.

It must never be combined into an "importance score."

A sparse node can mean:

- insufficient research;
- non-English scholarship not reviewed;
- oral transmission;
- undigitized archives;
- archival destruction;
- community-held sources;
- collecting bias;
- catalog bias;
- weak current access.

## 8. Visual implications

Version 0.2 adds:

- Combined ancestry;
- Author formation;
- Work formation;
- mechanism filtering;
- layer filtering;
- context-detail filtering;
- research-state display;
- source-environment display;
- distinct line grammar for different mechanisms.

Future versions should add:

- expandable/collapsible context hierarchy;
- timeline lanes;
- idea-mutation annotations;
- path scoring by explanatory usefulness;
- coverage-aware graph auditing.

## 9. The governing interpretation rule

The graph should make it possible to say:

> We know these things were connected.

without automatically saying:

> This caused that.

Precision about the type of connection is more important than maximizing the number of edges.
