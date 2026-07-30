# Manuscript Production Layer

`manuscript/` is the working layer between raw fragments and finished output.

It does not replace `notes/fragments/`.

Existing fragments remain where they are. This layer indexes them, promotes selected material into scenes and integrates scenes into chapters.

## Structure

- `fragments_index.yaml` maps existing fragment files into the production system.
- `fragment_metadata_schema.yaml` describes the metadata used for fragment indexing.
- `scenes/` contains worked scene drafts based on one or more fragments.
- `chapters/` contains integrated chapter drafts.
- `archive/` contains retired or superseded production drafts, not raw source.

## Flow

```text
notes/fragments/*
  ↓
manuscript/fragments_index.yaml
  ↓
manuscript/scenes/*.scene.md
  ↓
manuscript/chapters/*.md
  ↓
output/
```

## Rule

Never destroy a fragment in order to make a scene.

Fragments are source material. Scenes are renderings. Chapters are integrations.
