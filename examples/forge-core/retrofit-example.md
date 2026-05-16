# Forge Core Retrofit Example

## Goal

Add current workflow scaffolding to an existing CLI/core repository without changing product behavior.

## Steps

- Add `context/current.md` with active block, allowed files, forbidden files, validation, and stop condition.
- Add `context/delta.md` for session-to-session updates.
- Add a spec for the next non-trivial CLI/core boundary task.
- Add an ADR only if the public API or service boundary decision is hard to reverse.
- Add validation commands for CLI smoke checks, focused tests, structure checks, and repo hygiene.
- Add an audit checklist for public CLI behavior, service/Core API behavior, dry-run/apply safety, and output sanitization.

## Non-goals

- Do not refactor CLI commands during workflow retrofit.
- Do not change public behavior.
- Do not add dependencies.
- Do not use real music library paths or data.
