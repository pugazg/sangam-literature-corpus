# Pattuppāṭṭu architecture review — 2026-07-22

## Decision

Onboarding is paused before corpus generation. Pattuppāṭṭu cannot be represented as a short-poem anthology and cannot be sourced from one Project Madurai object. The ten long poems must be preserved as ten ordered records, each retaining its own Project Madurai provenance.

## Shared architecture changes that will be required

- Work profiles must support a collection whose canonical records come from multiple preserved source objects.
- Record inventory and physical auditing must be driven by a work profile rather than a fixed 400/401/500 range.
- Fidelity records must identify the source object used for each long-poem record.
- Structural output must distinguish each canonical long poem from its internal source-printed headings and from optional generated navigation.
- Manifest generation must retain the common poem-record schema while allowing long-poem-specific structural fields to be null or provenance-qualified.

## Source-specific parser requirement

A Pattuppāṭṭu parser is required. It must parse each Project Madurai object independently, preserving its header metadata, literary text, line-end markers, internal headings, colophon, and any commentary or notes as distinct source components. It must not interpret internal headings as additional anthology records.

## Record terminology

The existing `poems/` directory can represent the ten canonical long poems because they are literary poem records. Filenames should be `001.md` through `010.md`, with printed title and source-object identity in front matter. This remains a proposal until the ten raw objects and their complete grammar have been audited.

## Navigation strategy

The primary structure is the source-ordered set of ten long poems. No fifty-poem or ten-poem mechanical sections are appropriate. Internal navigation may be generated only from headings actually printed within each source object, and must be labelled as navigation rather than additional canonical poems.

## Metadata policy

Poet, patron/addressee, tiṇai, genre, line count, and internal headings may be populated only when printed in the selected Project Madurai object. Speaker and other interpretive fields remain null unless explicitly printed. Printed forms and provenance must be retained separately from normalized display values.

## Current blockers

1. None of the required HTML objects is preserved locally.
2. Exact raw bytes cannot be retrieved through the current execution environment.
3. Project Madurai exposes Mullai through at least two commentary-bearing objects (`pmuni0053` and `pmuni0488`), so canonical source selection requires an explicit edition decision after full-object inspection.

No corpus files, manifests, parser rules, or frozen-work outputs should be changed until these blockers are resolved.
