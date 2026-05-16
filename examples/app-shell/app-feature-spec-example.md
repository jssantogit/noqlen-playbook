# App Feature Spec Example: Display Local Service Readiness Status

## App screen goal

Show whether a local service is ready, starting, unavailable, or in error.

## State model

- `unknown`
- `starting`
- `ready`
- `unavailable`
- `error`

## Fake provider

Use a fake readiness provider that returns deterministic states for tests and demos.

## Contract boundary

The app depends on a public readiness contract, not internal service implementation details.

## Validation

- Validate state transitions with fake provider tests.
- Validate UI errors do not expose private paths or sensitive data.

## Audit

Audit app/core boundaries, state behavior, and data safety before integration with a real provider.
