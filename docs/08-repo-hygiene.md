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
- `opencode.json`.
- `.opencode/`.
- `.serena/`.
- `.mcp/`.
- Local MCP configs.
- `.mcp.json`.
- `RTK.md`.
- `.claude/`.
- `.cursor/`.
- `.windsurf/`.
- Generated tool state.
- Personal agent settings.
- Generated deployment artifacts.
- `site/`.

Do not commit `site/`. Do not use `mkdocs gh-deploy`. Do not depend on `gh-pages`. Deploys must be done through GitHub Actions when applicable.

Do not commit local agent configuration files. Do not commit MCP local configs unless explicitly approved. Prefer global, user-level, or untracked configs for optional agent tooling. Keep examples sanitized.

Version only sanitized `.example.*` files for tooling documentation. OpenCode, Serena, MCP, Context Mode, RTK, editor-agent, provider auth, and generated state files should stay user/global or untracked unless an explicit block approves a sanitized example.

Markdown docs may mention forbidden file names as warnings or sanitized examples. It is not allowed to commit the actual local/generated config or state files.

Repository checks should separate path contamination from content contamination so documentation may safely describe forbidden examples without committing actual forbidden files.
