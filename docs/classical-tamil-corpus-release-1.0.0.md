# Classical Tamil Corpus release 1.0.0

## Scope

This repository checkpoint contains 27 works frozen at corpus schema version
1.0.0: nine core Sangam works and eighteen Patiṉeṇkīḻkkaṇakku works. Together
they contain 5,632 canonical numbered records. The checkpoint certifies a
source-faithful preservation layer; it does not claim that Project Madurai is a
critical edition or that printed anomalies are philologically correct.

## Imported-history qualification

This Git repository was initialized after corpus construction. The release tag
certifies the imported frozen repository snapshot, not the earlier development
history. No artificial commits were created to imitate that history.

## Release inventories

- `repository-source-inventory-1.0.0.json` and `.csv` enumerate 36 work/source
  associations over 29 unique preserved source artifacts, including all ten
  independently pinned Pattuppāṭṭu objects.
- `repository-frozen-work-inventory-1.0.0.json` and `.csv` enumerate all 27
  frozen work records.
- `repository-record-inventory-1.0.0.json` pins canonical filenames plus body
  and source-note hashes for all 5,632 records.
- `repository-protected-conditions-1.0.0.json` records source losses, lacunae,
  malformed headings, restarted numbering, commentary boundaries, and other
  conditions that must not be silently repaired.
- `repository-content-hashes-1.0.0.sha256` is the deterministic release-content
  fingerprint.

## Shared-manifest incident and repair

The first release attempt detected an overlapping write to the shared
`manifests/poems.csv`. The incident did not affect canonical poem bodies,
source notes, raw source artifacts, work metadata, or physical inventories.
Because no earlier valid byte-for-byte CSV copy was available, the authoritative
manifest was independently reconstructed from the 27 frozen corpora. The
reconstruction proved exactly 5,632 unique canonical row identities with no
semantic additions, removals, changed fields, or duplicate keys.

The repaired aggregator now uses the work order in `works.json`, canonical
source order within each work, a stable `(work_slug, markdown_file)` identity,
fixed UTF-8/LF serialization, same-directory temporary output, flush and
`fsync`, atomic `os.replace`, and an advisory repository lock. The formal policy
is in `manifest-ordering-policy.md`. Two complete serial regeneration passes
were byte-stable.

## Validation gates

The release gate requires the recursive physical audit to pass, the complete
test suite to pass, every work validator to report zero errors, and fidelity to
hold for all 5,632 canonical bodies and source-note representations. It also
requires no canonical-body, source-note, raw-source, inventory, or version
drift from the approved baseline.

## Content-fingerprint policy

The fingerprint uses lexically sorted repository-relative paths and SHA-256.
It includes selected raw artifacts, canonical records, sections, work metadata,
structural inventories, apparatus, source metadata, programme manifests,
combined manifests, release documentation, and the canonicalized release
manifest. It excludes Git internals, caches, temporary and lock files, runtime
logs not designated as release evidence, and the fingerprint file itself.

The release manifest is represented by a canonical projection with its
`repository_content_manifest_sha256` and commit-dependent fields set to null.
This avoids impossible hash and Git self-reference while still binding all
stable release metadata. The projection is explicitly labelled in the hash
manifest.

## Git checkpoint and tag

The release uses two commits: a release-content commit followed by a checkpoint
metadata commit that records the first commit and its tree. The second commit
cannot contain its own hash; the annotated local tag
`classical-tamil-corpus-v1.0.0` records both final commit identities. A later
post-tag verification log is an external audit artifact and does not move the
tag.

No repository or tag is pushed as part of this local checkpoint.
