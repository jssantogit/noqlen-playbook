# Safety

Safety is a triggered escalation for work whose **real execution** can materially affect data, users, credentials, repository history, production, or published state.

Safety controls are mandatory when the corresponding failure mode is present, but use only the controls that address the actual risk.

## When Safety Activates

Use Safety when the task introduces, changes, or performs behavior with material real-state impact such as:

- destructive changes to real user or library data;
- credentials, authentication, authorization, or security policy;
- production or deployment state;
- repository history;
- published packages, releases, or artifacts;
- migrations, destructive cleanup, or irreversible operations.

Read-only inspection of user-authorized real data does not by itself require a confirmation pause. Handle that data carefully, minimize reproduction, and do not turn ordinary inspection into a destructive/apply workflow.

## Authorization And Apply Intent

An explicit user instruction to perform a named action on a sufficiently defined target counts as authorization for that action. **Do not ask the user to confirm the same action twice.**

Ask for clarification or renewed confirmation only when:

- the target or scope is materially ambiguous;
- the action expands beyond what the user authorized;
- newly discovered consequences materially increase the impact;
- a destructive apply target cannot be verified safely;
- the tool or platform itself requires confirmation.

A broad goal such as "clean up my library" does not authorize an unspecified destructive operation if the exact target/action still needs to be decided. Authorization should match the action actually being performed.

## Implementation Versus Real Execution

Distinguish **building/testing a capability** from **performing the high-impact action**.

Implementing or testing delete, move, overwrite, import, migration, deployment, or publication behavior against synthetic data, temporary directories, mocks, emulators, or isolated state does **not** itself require user confirmation.

When a real-state action is already explicitly authorized by the user, proceed without adding a redundant confirmation step. If it is not authorized, obtain explicit apply intent before performing a destructive, publishing, production, history-rewriting, or otherwise high-impact mutation.

A safe implementation should make the boundary between preview/test behavior and real apply behavior difficult to cross accidentally.

## Controls

Choose the smallest set that addresses the concrete failure mode:

- explicit apply intent when a high-impact real-state action has not already been authorized;
- dry-run or preview when target selection, rollback, or impact is uncertain;
- temporary workspace or synthetic dataset during development and tests;
- backup, rollback, recovery, or restore path where failure could cause material loss;
- restricted tool permissions for shell, network, write, deploy, push, or delete actions;
- targeted negative tests for unsafe paths;
- independent review when impact remains high after normal validation.

Do not require every control mechanically. Do not add a dry-run, backup, branch, or approval step solely because an operation sounds risky when that control would not reduce a concrete failure mode.

## Data Handling

Do not commit or unnecessarily reproduce:

- secrets, tokens, credentials, auth files, or private keys;
- personal filesystem paths;
- private user data;
- real music-library paths or content;
- lyrics;
- audio fingerprints or similar private derived data;
- unsanitized provider output or local configuration.

User-authorized local/private data may be inspected transiently when the task actually requires it. Minimize what is copied into chat, logs, reports, fixtures, commits, or other durable/shareable artifacts.

A personal path may be used to perform user-directed local work; avoid persisting it in documentation, examples, or committed output unless the user explicitly intends that path to be durable.

Automated tests must use synthetic metadata, sanitized fixtures, temporary directories, or isolated services.

## Destructive Operations Against Real State

For delete, move, overwrite, import, cleanup, migration, or publication over real data/state:

1. identify the target set precisely enough to act safely;
2. use preview/dry-run when it materially reduces uncertainty;
3. validate path and boundary handling when relevant;
4. preserve a recovery path when practical and when failure could cause material loss;
5. verify that the action is authorized; do not re-ask if it already is;
6. report material effects or unexpected deviations after execution.

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
- An explicit request for one of those actions is the authorization; do not ask for a second identical confirmation unless scope or impact changes.
- Release preparation and release publication are separate actions.
- Use branch isolation when it materially improves rollback or review; do not create an extra branch solely because a diff is large.

## Security-Sensitive Work

Authentication, authorization, secret handling, trust boundaries, sandboxing, and externally exposed security behavior normally activate both Safety and Audit. Use Design as well when the work changes a durable security boundary or policy.
