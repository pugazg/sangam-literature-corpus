# Classical Tamil Corpus 1.0.0 checkpoint

The verified release-content commit is
`7266a9fcb76568806b371cb31ec47f6aad6b285a`, with tree
`f188b1e9b0acbc6f2355665bca286c1977b73bab`.

This Git repository was initialized after corpus construction. The release tag
certifies the imported frozen repository snapshot, not the earlier development
history.

The checkpoint covers 27 frozen works and 5,632 canonical numbered records:
nine core Sangam works and eighteen Patiṉeṇkīḻkkaṇakku works. It binds 29
unique preserved source artifacts through 36 work/source associations. The
approved combined manifest SHA-256 is
`4c287ee9901d028f97659b3a099bd521efc7d43819424b32184c975de9bf4cb7`;
its ordering policy is `repository-canonical-order-v1`.

The pre-release shared-manifest incident was repaired without canonical corpus
drift. Semantic comparison found no row additions, removals, field changes, or
duplicate keys. The replacement aggregator is deterministic, atomic, and
advisory-lock protected. The recursive audit passed, all 95 tests passed, all
27 validators reported zero errors, and source/body plus source-note fidelity
was 5,632/5,632. Both serial regeneration passes had no path or hash changes.

The repository content-manifest SHA-256 is
`a220173f9b444095b191814622220203cd223d8258744091d7cbbbec1b76d326`.
The intended annotated tag is `classical-tamil-corpus-v1.0.0`.

The checkpoint commit cannot contain its own identity. Its final commit and
tree are therefore recorded by the annotated tag rather than by amending this
file into a self-reference loop.
