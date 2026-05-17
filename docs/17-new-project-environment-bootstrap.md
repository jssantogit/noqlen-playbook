# New Project Environment Bootstrap

Environment bootstrap prepares optional optimization tooling for a new Noqlen project. It is its own block.

Do not start product implementation in the same block unless explicitly requested.

## Flow

1. Read project handoff.
2. Read Noqlen Playbook `README.md` and `AGENTS.md`.
3. Detect project profile.
4. Detect OS/shell/package managers.
5. Detect available tools.
6. Choose environment mode.
7. Prepare missing tools only when allowed.
8. Verify each tool.
9. Produce a sanitized installation report.
10. Start development only after environment report is complete.

## Project Profiles

- `core-lib`: library with tests, public API boundaries, and core logic.
- `service-core`: service or backend core with integration boundaries.
- `app-shell`: UI or app layer over core contracts and fake providers.
- `docs-only`: documentation repository or documentation block.
- `experiment`: bounded exploratory project with explicit stop conditions.

## Environment Modes

`minimal`:

- No new tools.
- Inspect and report only.

`recommended`:

- Serena.
- RTK.
- Context Mode only if useful.
- Caveman disabled.

`full`:

- Recommended tools.
- Optional Caveman / terse-output only with explicit confirmation.

`audit-safe`:

- Tools may assist exploration.
- Final evidence must be raw/uncompressed where needed.

Decision rule:

```text
Default for new Noqlen projects:
recommended mode = OpenCode native + Serena + RTK
Context Mode only if useful and validated
Caveman disabled unless explicitly requested
```

Default setup uses user/global config. Project-local config is forbidden unless explicitly approved.

Permission rule:

```text
If the agent lacks permission to install global tools, it must produce commands and stop.
```

Separation rule:

```text
Environment bootstrap is its own block.
Do not start product implementation in the same block unless explicitly requested.
```

## Bootstrap Report

The final report must include:

- Project profile.
- Environment mode.
- OS and shell detected.
- Tools installed.
- Tools already present.
- Tools skipped.
- Failures.
- Manual confirmation required.
- Configs touched.
- Verification commands and results.
- Risks.
- Next step.

The report must be sanitized. Do not include secrets, personal paths, real music library paths, lyrics, fingerprints, or private data.
