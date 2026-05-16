# Anchor Retrofit Example

## Goal

Add service-core context, contracts, fake clients, provider checks, and audit practices to an Anchor-like repository.

## Steps

- Add current context naming the active service boundary.
- Add specs for service contracts, provider contracts, health/readiness, diagnostics, or app-facing API surface.
- Add fake clients for service lifecycle, provider status, and degraded/error states.
- Add validation for path safety, sanitized logs, readiness reports, and public API summaries.
- Add audit checks for app/core boundaries, service side effects, local operations, and output sanitization.
- Update handoff so future app work knows which facade to use and which internals are forbidden.

## Stop condition

Stop if retrofit starts real service execution, app implementation, or provider-specific behavior outside the active spec.
