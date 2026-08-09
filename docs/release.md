# Release

Release work activates **Safety** and normally **Audit**.

Release preparation and release publication are separate actions. Preparing a release does not authorize publishing it.

## Prepare

Before a release is considered ready, verify what is relevant to the project:

- required test suites pass;
- documentation and changelog/release notes reflect the shipped behavior;
- version metadata is correct;
- repository contamination/hygiene checks pass;
- expected artifacts are reproducible and inspectable;
- migrations or compatibility changes have rollout and recovery notes;
- risky changes received the level of review they require.

Do not add release ceremony that does not map to an actual project risk.

## Publish

Publishing must be explicit.

- Prefer GitHub Actions or the project's established release automation.
- Do not perform ad-hoc local deploys when a reviewed release path exists.
- Do not publish, tag, merge, or deploy merely because preparation passed.
- Use least-privilege credentials and permissions.
- Preserve enough evidence to identify what commit/artifact was published.

## Repository Rules

- Do not commit generated deployment output such as `site/`.
- Do not use `mkdocs gh-deploy` or depend on `gh-pages` for Noqlen playbook deployment.
- Keep release credentials and provider auth out of the repository.

## Rollback

A rollback or recovery plan is warranted when a failed release can materially affect users, data, compatibility, or future upgrades. It does not need to be a formal document for low-impact, trivially reversible releases.
