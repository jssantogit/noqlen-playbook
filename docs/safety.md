# Safety

Safety is enforced by the **Safety Gate** in `workflow.md`. It is conditional, but when triggered its controls are mandatory.

## When The Gate Activates

Use the Safety Gate for work that can materially affect:

- real user or library data;
- credentials, authentication, authorization, or security policy;
- production or deployment state;
- repository history;
- published packages, releases, or artifacts;
- migrations, destructive cleanup, or irreversible operations.

## Default Controls

Choose the smallest set that addresses the actual risk:

- explicit confirmation before destructive or publishing actions;
- dry-run or preview before apply;
- temporary workspace or synthetic dataset before real data;
- backup, rollback, recovery, or restore path where failure could cause loss;
- restricted tool permissions for shell, network, write, deploy, push, or delete actions;
- targeted negative tests for unsafe paths;
- stronger independent review when impact is high.

Do not require every control mechanically. The control must map to a concrete failure mode.

## Data Rules

Never expose or commit:

- secrets, tokens, credentials, auth files, or private keys;
- personal filesystem paths;
- private user data;
- real music-library paths or content;
- lyrics;
- audio fingerprints or similar private derived data;
- unsanitized provider output or local configuration.

Automated tests must use synthetic metadata, sanitized fixtures, temporary directories, or fake services.

## Destructive Operations

For delete, move, overwrite, import, cleanup, migration, or publication over real data:

1. understand the exact target set;
2. prefer preview/dry-run;
3. validate path and boundary handling;
4. make recovery possible when practical;
5. require explicit apply intent;
6. report what changed.

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
- Prefer branch isolation for substantial changes.

## Security-Sensitive Work

Authentication, authorization, secret handling, trust boundaries, sandboxing, and externally exposed behavior normally activate both Safety and Audit gates. Use the Architecture gate as well when the security decision changes a durable boundary or policy.
