# Tolkāppiyam corpus architecture review

## Decision

Tolkāppiyam is a grammatical work, not a short-poem anthology. The canonical
record type is `nurpa`; records live under `corpus/tolkappiyam/nurpas/`. The
source hierarchy is preserved as work → அதிகாரம் → இயல் → நூற்பா. No arbitrary
fifty-record navigation sections or `poems/` compatibility directory is made.

## Shared architecture changes

The recursive auditor gains an explicit neutral-record profile. The work
orchestrator dispatches only the named `tolkappiyam` profile. The existing
`poems.csv` remains the immutable 5,632-poem manifest; a generic `records.csv`
combines poem and நூற்பா identities. Shared poem aggregation skips non-poem
work profiles instead of pretending நூற்பா are poems.

## Identity

Repository identity follows continuous source order (`tolkappiyam-0001` …
`tolkappiyam-1602`). Traditional numbering restarts within each இயல். Verified
upstream semantic IDs such as `ezhuthu-noolmarabu-001` are retained as aliases.
These four notions—repository ID, source sequence, traditional number, and
upstream semantic ID—are never silently equated.

## Source grammar

The independent parser converts HTML `<br>` and block boundaries to stable text
lines, identifies the three printed part headings and 27 `A.I. heading`
patterns, and closes a நூற்பா only at a trailing printed number. Five numbers
are attached directly to text. The parser separates only that layout marker;
it does not edit the preceding source string.

## Rejected inputs

The Next.js application, UI components, search/transliteration tools, māttirai
calculators, SEO pages, Tailwind/Vercel configuration, glossary, analysis,
English explanations, concepts, keywords, and commentary placeholders are not
canonical corpus inputs.
