# Tool Installation Report Example

This is a sanitized example. It uses no real user paths, secrets, or private data.

## Environment Summary

- Project profile: `app-shell`.
- Environment mode: `recommended`.
- Install scope: `user/global config`.
- OS/shell: detected and summarized without personal paths.

## Tool Status

| Tool | Status | Notes |
|---|---|---|
| Serena | Already present | Verified with help command. Read-only mode recommended first. |
| Context Mode | Installed | Global install completed. OpenCode config requires user review before activation. |
| RTK | Installed | Version and gain commands passed. |
| Caveman | Skipped | Disabled by default. |

Status categories: Installed, Already present, Skipped, Failed, Manual confirmation required.

## Commands Run

- `uv --version`.
- `serena --help`.
- `npm install -g context-mode`.
- `context-mode doctor`.
- `rtk --version`.
- `rtk gain`.
- `rtk init --show`.

## Config Changes

- User/global config reviewed.
- No project-local config created.
- No repository files modified.
- No secrets or personal paths written.

## Verification

- Serena: passed.
- Context Mode: passed or manual OpenCode `ctx stats` still required.
- RTK: passed.
- Caveman: not installed.

## Skipped Items

- Caveman / terse-output tooling skipped because it is disabled by default.
- Project-local OpenCode config skipped because project-local config was forbidden.

## Risks

- Global shell PATH may require restart after install.
- Existing global OpenCode config must be reviewed before modification.
- Compressed output must not be treated as final audit evidence.

## Next Recommended Action

Start the first scoped implementation block only after the user accepts this environment report.
