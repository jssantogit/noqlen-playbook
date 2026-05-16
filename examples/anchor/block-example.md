# Anchor Block Example

## Goal

Add or harden one safe service readiness or diagnostics boundary.

## Allowed files

- Active spec files.
- Readiness or diagnostics contract files named by the spec.
- Fake client tests.
- Handoff or delta summary.

## Forbidden files

- Real service startup scripts.
- Provider internals not named by the spec.
- App UI files.
- Local configuration files.

## Validation

- Run focused tests for readiness or diagnostics contracts.
- Confirm fake clients cover unavailable, degraded, ready, and error states.
- Confirm logs and errors do not expose private paths or sensitive data.

## Audit trigger

Audit if public API surface, service lifecycle behavior, readiness state, diagnostics output, or log sanitization changes.

## Stop condition

Stop if real local service side effects, app behavior, or provider-specific internals are required.
