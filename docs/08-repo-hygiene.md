# Repo Hygiene

Forbidden content includes:

- Secrets.
- Tokens.
- Credentials.
- Personal paths.
- Private data.
- Real music library paths.
- Lyrics.
- Fingerprints.
- Local agent/tooling directories.
- Generated deployment artifacts.
- `site/`.

Do not commit `site/`. Do not use `mkdocs gh-deploy`. Do not depend on `gh-pages`. Deploys must be done through GitHub Actions when applicable.

Repository checks should separate path contamination from content contamination so documentation may safely describe forbidden examples without committing actual forbidden files.
