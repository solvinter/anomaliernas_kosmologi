# Production Pipeline

This repository separates raw material from rendered literary output.

## Flow

```text
Idea
  ↓
Fragment
  ↓
YAML metadata
  ↓
Scene objective
  ↓
AI builds first literary version
  ↓
Director feedback
  ↓
Rewrite
  ↓
Continuity review
  ↓
Research review
  ↓
Language polish
  ↓
Chapter integration
  ↓
Final manuscript output
```

## Repository Mapping

- `notes/fragments/` contains raw and semi-raw author material.
- `notes/fragments/*.yaml` contains fragment-level metadata.
- `manuscript/fragments_index.yaml` maps existing fragments into the production system.
- `manuscript/scenes/` contains worked scene files created from one or more fragments.
- `manuscript/chapters/` contains integrated chapter drafts.
- `story_bible/` describes what is true in the novel's world.
- `production/` describes how raw material may be rendered.
- `output/` contains reading copies, PDFs, Obsidian vaults and other generated views.

## Rendering Rule

Fragment and YAML are source material.

Story bible is world truth.

Production files are rendering instructions.

The rendered manuscript must obey all three.
