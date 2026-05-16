# Release Workflow

Release readiness requires a clean validation checklist, updated docs, clear changelog or release notes, and an audit of risky changes.

Use GitHub Actions-based release automation when publishing is applicable. Do not perform local ad-hoc deploys. Do not commit `site/`. Do not depend on `gh-pages`. Do not use `mkdocs gh-deploy`.

Before release, verify tests, documentation, repository hygiene, version metadata, expected artifacts, and rollback or recovery notes where relevant. Publishing must be explicit and separate from preparation.
