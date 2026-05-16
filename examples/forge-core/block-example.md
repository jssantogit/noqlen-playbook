# Forge Core Block Example

## Goal

Harden one CLI/core boundary so the CLI remains a thin adapter over a service result.

## Allowed files

- One active spec directory.
- One service or Core API module named by the spec.
- Matching focused tests with fake data.
- Handoff or delta summary.

## Forbidden files

- Unrelated CLI commands.
- Release files.
- Real local configuration.
- Real music library fixtures.

## Validation

- Run focused tests for the service/Core API boundary.
- Run a CLI smoke command that does not require a real library.
- Run repository hygiene checks.

## Audit trigger

Audit if public CLI output, public API shape, apply behavior, or file operation safety changes.

## Stop condition

Stop if the change requires broad CLI rewrites, real library access, or behavior outside the active spec.
