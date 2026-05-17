# Serena Example

This is a sanitized example only. It is not active Serena config.

## Policy

- Start with `serena-ro` for read-only semantic navigation.
- Use `serena-edit` only when the block lists explicit allowed files.
- Do not use Serena for broad refactors unless the block explicitly asks.
- Keep `.serena/` untracked.
- If Serena creates project-local state, report it and keep it out of commits unless explicitly approved and sanitized.

## Example Block Declaration

- Tool Mode: `serena-ro`.
- Tooling goal: locate symbols and references before a scoped edit.
- Allowed files: `<explicit list>`.
- Forbidden files: active local tool configs, generated state, credentials, and unrelated product files.
- Raw evidence required: validation failures, audit findings, and scope-boundary concerns.
