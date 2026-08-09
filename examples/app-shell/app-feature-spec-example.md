# App Example: Readiness Status With A Real Boundary

This example shows where the **Isolation Rule** is useful. It is not a required starting point for every app feature.

## Goal

Show whether an already-defined local service boundary is unknown, starting, ready, unavailable, or in error.

## Why Isolation Helps Here

The app consumes a real service-readiness boundary. Starting and failing the real local service in every UI test would be slower and less deterministic, so tests use a lightweight fake implementation of the **existing** readiness boundary.

The boundary exists because the app and service are separate components — not because the playbook requires a fake.

Use the lightest substitute that proves state behavior. If a fixture or stub is enough, do not create a richer fake.

## Verification

- test state rendering with deterministic readiness states;
- verify safe error text does not expose private paths or sensitive data;
- run the relevant integration check against the real boundary separately when practical.

Design is relevant only if the durable readiness contract or compatibility strategy changes. Audit is relevant only when an important public/security boundary leaves high-impact residual risk after normal validation and diff review.
