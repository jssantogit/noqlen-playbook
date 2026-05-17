# Opencode Prompt: Bootstrap Project Environment

Purpose: Prepare a Noqlen project environment and stop before product implementation.

## Prompt

Task: Bootstrap the Noqlen project environment for `<project name>`.

Read first:

- Project handoff: `<handoff location>`.
- Noqlen Playbook `README.md`.
- `AGENTS.md`.
- `docs/14-agent-tooling.md`.
- `docs/16-optimized-development-environment.md`.
- `docs/17-new-project-environment-bootstrap.md`.

Detect:

- OS and shell.
- Package managers.
- `opencode`.
- `uv`.
- `npm`.
- `node`.
- `cargo`.
- `brew`.
- `python3`.

Choose environment mode: `<minimal | recommended | full | audit-safe>`.

Rules:

- Prefer global/user config.
- Do not modify repo files unless explicitly asked.
- Do not commit configs.
- Do not create active project-local `opencode.json`, `.opencode/`, `.serena/`, `.mcp/`, `.mcp.json`, `RTK.md`, `.claude/`, `.cursor/`, `.windsurf/`, generated tool state, credentials, auth files, secrets, or personal paths.
- Prepare missing tools only when allowed.
- Verify every installed or already-present tool before claiming it is usable.
- Produce a sanitized report.
- Stop before product implementation.

Report:

- Project profile.
- Environment mode.
- Installed tools.
- Already present tools.
- Skipped tools.
- Failed steps.
- Manual confirmation required.
- Verification commands and results.
- Configs touched.
- Risks.
- Next recommended Tool Mode.
