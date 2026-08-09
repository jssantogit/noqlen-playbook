# App Example: Readiness Status With A Real Boundary

This example demonstrates a case where the **Fake Gate is justified**. It is not a required starting point for every app feature.

## Goal

Show whether an already-defined local service boundary is unknown, starting, ready, unavailable, or in error.

## Why A Fake Helps Here

The app consumes a real service-readiness boundary. Starting and failing the real local service in every UI test would be slower and less deterministic, so tests use a lightweight fake implementation of the **existing** readiness boundary.

The boundary exists because the app and service are separate components — not because the playbook requires a fake.

## Verification

- test state rendering with deterministic readiness states;
- verify safe error text does not expose private paths or sensitive data;
- run the relevant integration check against the real boundary separately when practical.

## Gates

- Fake Gate: yes, because a real external/service boundary benefits from isolation.
- Design Gate: only if the readiness contract itself changes materially.
- Audit Gate: only if the public boundary or security/data risk warrants independent review.
