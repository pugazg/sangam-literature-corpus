# Patiṉeṇkīḻkkaṇakku programme decisions

## 2026-07-29 — programme identity

- The programme contains exactly eighteen canonical work records.
- `முப்பால்` is an alias of `திருக்குறள்`, not a nineteenth corpus work.
- `கைந்நிலை` is the selected eighteenth work.
- `இன்னிலை` is preserved only as non-selected source/apparatus evidence where it shares a Project Madurai object with selected works.

## Source policy

- Eleven exact Project Madurai UTF-8 HTML responses were preserved before parser implementation.
- A shared HTML object may supply more than one work, but every parser must use explicit start/end boundaries.
- No reading may be merged across Project Madurai releases.
- Commentary releases are alternatives, not silent substitutes for the selected source-only object.

## Implementation policy

- Each work receives source reconnaissance, an explicit parser profile, onboarding while unfrozen, idempotence and fidelity validation, frozen-work regression comparison, and a separate recorded freeze decision.
- Shared infrastructure owns schema, manifests, physical inventory, hashes, and validation.
- Source grammar remains explicit and work-specific. Unknown slugs fail; there is no guessing fallback.
