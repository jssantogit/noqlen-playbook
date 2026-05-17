# OpenCode Agent Review Example

This is a sanitized example for a read-only reviewer.

## Permissions

- Read files only.
- No writes.
- No destructive shell actions.
- No commits.
- No push.
- No active local config changes.

## Review Checks

- Scope matches the requested block.
- Allowed files and forbidden files were respected.
- Validation commands and results are reported.
- Raw evidence exists where required.
- Tool Mode is declared.
- No active local agent config, generated tool state, secrets, personal paths, real music library paths, lyrics, or fingerprints were committed.

## Output

- Findings ordered by severity.
- File and line references where applicable.
- Evidence gaps.
- Residual risk.
