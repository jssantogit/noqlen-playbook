# Opencode Prompt: Handoff Bootstrap

Purpose: Reconstruct the next block environment from handoff/current context without touching product code.

## Prompt

Task: Prepare only the environment needed for the next Noqlen block.

Read first:

- Current context: `<path>`.
- Handoff: `<path>`.
- Noqlen Playbook `README.md`.
- `AGENTS.md`.
- `docs/14-agent-tooling.md`.
- `docs/16-optimized-development-environment.md`.
- `docs/17-new-project-environment-bootstrap.md`.

Reconstruct:

- Current Tool Mode.
- Next block goal.
- Whether the next block needs OpenCode native capabilities, Serena, RTK, Context Mode, Caveman, or no extra tools.
- Raw evidence requirements.
- Allowed files and forbidden files.

Rules:

- Prepare only the next block environment.
- Do not touch product code.
- Do not commit local configs.
- Prefer global/user config.
- Do not create active project-local `opencode.json`, `.opencode/`, `.serena/`, `.mcp/`, `.mcp.json`, `RTK.md`, `.claude/`, `.cursor/`, `.windsurf/`, generated tool state, credentials, auth files, secrets, or personal paths.
- Treat Context Mode as pilot unless validated in the current environment.
- Keep Caveman disabled unless explicitly confirmed.

Report:

- Installed/global tools.
- Already present tools.
- Skipped tools.
- Pilot tools.
- Configs touched.
- Verification results.
- Tooling risks.
- Recommended Tool Mode for the next block.
