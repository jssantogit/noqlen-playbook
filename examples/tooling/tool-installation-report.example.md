# Tool Installation Report Example

This is a sanitized example. It contains no real user paths, secrets, credentials, auth data, real music library paths, lyrics, or fingerprints.

## Installed

- RTK: installed globally. Verified with `rtk --version` and `rtk gain`.

## Already Present

- OpenCode: present. Native permissions reviewed.
- `python3`: present. Used for playbook validation.

## Skipped

- Caveman: skipped because it is disabled by default.
- Project-local OpenCode config: skipped because project-local config was not approved.

## Failed

- None in this example.

## Manual Confirmation Required

- Context Mode OpenCode support must be verified inside a supported session with `ctx stats`.

## Verification Commands

- `opencode --help`.
- `uv --version`.
- `serena --help`.
- `rtk --version`.
- `rtk gain`.
- `context-mode doctor`.
- `python3 scripts/validate_playbook_structure.py`.
- `python3 scripts/check_repo_contamination.py`.

## Configs Touched

- User/global config only, if explicitly allowed.
- No repo files modified.
- No active local configs committed.

## Risks

- Shell restart may be required after global installs.
- RTK telemetry/privacy state must be verified during pilot.
- Compressed output is not audit proof.

## Next Recommended Action

Start the next scoped block with Tool Mode `serena-ro` or `rtk` only if the block benefits from it.
