# Combined poem-manifest ordering policy

Policy version: `repository-canonical-order-v1`.

`manifests/works.json` defines the authoritative work order. Within each work,
rows are ordered by canonical repository `source_order` (falling back to the
canonical record number), then by canonical Markdown path as a deterministic
tie-breaker. Printed numbering is provenance and is never the primary key.

The stable row key is `(work_slug, markdown_file)`. This preserves restarted,
duplicated, missing, and division-local printed numbers without collision.
Lost canonical records remain rows. Unnumbered source texts and navigation
files are excluded because they are not canonical numbered record files.

This ordering is mechanical repository structure, not literary chronology or
interpretation. The combined manifest is built in one aggregation pass, written
to a same-directory temporary file, flushed and fsynced, validated, and exposed
with atomic `os.replace`. An advisory `fcntl` lock prevents overlapping writers.
