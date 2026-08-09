# Safety

Safety is a triggered escalation for work whose **real execution** can materially affect data, users, credentials, repository history, production, or published state.

Safety controls are mandatory when the corresponding failure mode is present, but use only the controls that address the actual risk.

## When Safety Activates

Use Safety for work involving real-state impact such as:

- real user or library data;
- credentials, authentication, authorization, or security policy;
- production or deployment state;
- repository history;
- published packages, releases, or artifacts;
- migrations, destructive cleanup, or irreversible operations.

## Implementation Versus Real Execution

Distinguish **building/testing a capability** from **performing the high-impact action**.

Implementing or testing delete, move, overwrite, import, migration, deployment, or publication behavior against synthetic data, temporary directories, mocks, emulators, or isolated state does **not** itself require user confirmation.

Explicit confirmation or apply intent is required before the agent performs a destructive, publishing, production, history-rewriting, or otherwise high-impact action against real state when that action has not already been explicitly authorized.

A safe implementation should make this boundary difficult to cross accidentally.

## Controls

Choose the smallest set that addresses the concrete failure mode:

- explicit apply intent before high-impact real-state actions;
- dry-run or preview before apply;
- temporary workspace or synthetic dataset during development and tests;
- backup, rollback, recovery, or restore path where failure could cause material loss;
- restricted tool permissions for shell, network, write, deploy, push, or delete actions;
- targeted negative tests for unsafe paths;
- independent review when impact remains high after normal validation.

Do not require every control mechanically.

## Data Rules

Never expose or commit:

- secrets, tokens, credentials, auth files, or private keys;
- personal filesystem paths;
- private user data;
- real music-library paths or content;
- lyrics;
- audio fingerprints or similar private derived data;
- unsanitized provider output or local configuration.

Automated tests must use synthetic metadata, sanitized fixtures, temporary directories, or isolated services.

## Destructive Operations Against Real State

For delete, move, overwrite, import, cleanup, migration, or publication over real data/state:

1. understand the exact target set;
2. prefer preview/dry-run;
3. validate path and boundary handling;
4. make recovery possible when practical;
5. require explicit apply intent;
6. report what actually changed.

Operations should fail closed when target selection or safety checks are ambiguous.

## Repository Hygiene

Keep local agent/tool state untracked. This includes active OpenCode, Serena, MCP, editor-agent, Context Mode, provider-auth, generated state, and similar local configuration unless the task explicitly asks for a sanitized example.

Do not commit generated deployment output such as `site/`.

Documentation may mention forbidden filenames as warnings or sanitized examples; the actual active local files remain forbidden.

The repository contamination checker is an executable guardrail:

```bash
python3 scripts/check_repo_contamination.py
```

## Git And Publishing

- Do not force push or rewrite history unless explicitly requested.
- Do not merge, deploy, publish, tag, or release unless explicitly requested.
- Release preparation and release publication are separate actions.
- Prefer branch isolation for substantial or high-impact changes.

## Security-Sensitive Work

Authentication, authorization, secret handling, trust boundaries, sandboxing, and externally exposed security behavior normally activate both Safety and Audit. Use Design as well when the work changes a durable security boundary or policy.
