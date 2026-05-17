# Opencode Prompt: New Project Environment Handoff

Purpose: Handoff from ChatGPT to Opencode for preparing a new Noqlen project environment before coding.

## Handoff

Project name: `<project name>`

Project type/profile: `<core-lib | service-core | app-shell | docs-only | experiment>`

Repository path: `<repository path or workspace-relative description>`

Tooling mode: `recommended`

Allowed installation scope: `user/global config`

Project-local config: `forbidden unless explicitly approved`

Caveman: `disabled`

Forbidden actions:

- Do not start product implementation in this block.
- Do not create or commit project-local `opencode.json`.
- Do not create or commit `.opencode/`, `.serena/`, `.mcp/`, local MCP config, generated tool state, secrets, or personal config files.
- Do not use destructive setup without explicit confirmation.
- Do not overwrite existing user/global config without showing the diff or backup plan first.

Tools to prepare:

- Serena.
- Context Mode.
- RTK.
- Caveman only if explicitly confirmed later.

Validation commands:

- `rtk --version`.
- `rtk gain`.
- `rtk init --show`.
- `context-mode doctor`.
- OpenCode `ctx stats` instruction.
- `serena --help`.

Expected final report:

- Environment summary.
- Installed tools.
- Already present tools.
- Skipped tools.
- Failed steps.
- Manual confirmation required.
- Configs touched.
- Verification results.
- Risks.
- Next recommended action.
