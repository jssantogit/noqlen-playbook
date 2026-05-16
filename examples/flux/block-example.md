# Flux Block Example

## Goal

Add or harden one safe provider/import boundary using fake providers and dry-run planning only.

## Allowed files

- Active spec files.
- Provider contract or fake provider files named by the spec.
- Planning service tests using synthetic fixtures.
- Handoff or delta summary.

## Forbidden files

- Real network clients unless explicitly approved by a separate spec.
- Real music library paths or fixtures.
- Import/apply code outside the named boundary.
- Cleanup execution outside dry-run planning.

## Validation

- Run focused fake provider tests.
- Run path safety and workspace containment tests.
- Confirm no network access is required.
- Confirm no real music library is used.

## Audit trigger

Audit if provider capabilities, import boundaries, quarantine behavior, cleanup behavior, or apply gates change.

## Stop condition

Stop if real network, real downloads, real imports, or real library access becomes necessary.
