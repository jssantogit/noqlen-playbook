# Opencode Prompt: Bootstrap Optimized Environment

Purpose: Prepare the optional optimized AI development environment for one project and stop before product implementation.

## Prompt

Task: Bootstrap the Noqlen optimized development environment for `<project name>`.

Read first:

- Project handoff: `<handoff location>`.
- `AGENTS.md`.
- Noqlen Playbook `README.md`.
- `docs/16-optimized-development-environment.md`.
- `docs/17-new-project-environment-bootstrap.md`.

Environment mode: `<minimal | recommended | full | audit-safe>`.

Allowed installation scope: `<inspect only | user/global config | project-local config>`.

Project-local config: forbidden unless explicitly approved.

Detect:

- OS.
- Shell.
- Package managers.
- `git`.
- `python3` / `python` fallback.
- `node`.
- `npm`.
- `uv`.
- `cargo`.
- `brew`.
- `opencode`.
- Existing user/global OpenCode config.

Rules:

- Do not modify repository files unless explicitly asked.
- Use global/user-level config by default.
- Do not install Caveman unless explicitly confirmed.
- Do not commit `opencode.json`, `.opencode/`, `.serena/`, `.mcp/`, local MCP config, personal config files, secrets, or personal paths.
- Do not overwrite existing global OpenCode config without backing it up or showing the diff first.
- If permission to install global tools is missing, produce commands and stop.

Install or configure when allowed:

- Serena.
- Context Mode.
- RTK.
- Caveman only with explicit confirmation.

Verify:

- `rtk --version`.
- `rtk gain`.
- `rtk init --show`.
- `context-mode doctor`.
- OpenCode session instruction: run `ctx stats`.
- `serena --help`.
- Caveman verification only if installed intentionally.

Produce a sanitized report:

- Installed.
- Already present.
- Skipped.
- Failed.
- Manual steps required.
- Configs touched.
- Verification commands.
- Risks.
- Next step.

Stop condition: stop after environment setup/report. Do not start product implementation in the same block.
