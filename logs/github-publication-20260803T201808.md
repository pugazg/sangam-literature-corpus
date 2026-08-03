# GitHub publication attempt — 2026-08-03 20:18:08 +05:30

Publication stopped safely before remote configuration. The GitHub CLI reports
that the active `pugazg` credential is invalid, and the API connection could not
verify `pugazg/classical-tamil` identity, visibility, emptiness, permissions,
branches or tags.

No `origin` was added. No branch or tag was pushed. No force operation or
visibility change was attempted.

The verified local state is ready at `main`
`51c65b36d07ecf604c11d8cc6399ad40ab7e7086`, with immutable annotated tags
`classical-tamil-corpus-v1.0.0` and `classical-tamil-corpus-v1.1.0`. The stable
research branch remains `research/sangam-evidence-r0` at
`7087626347b56e0145ab69b2fb7ef355f6bc07d5d`.

Before publication, authenticate with `gh auth login -h github.com`. Then verify
that the destination is the intended empty private repository. Only after that
verification should `origin` be added and `main`, the two release tags, and the
stable research branch be pushed without force.

The rights review contains unresolved questions. The repository must remain
private unless a later, separately authorized decision follows resolution of
that review.
