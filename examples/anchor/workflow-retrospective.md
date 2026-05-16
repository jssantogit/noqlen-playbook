# Anchor Workflow Retrospective

A local service core benefits from the current workflow because service lifecycle, health, readiness, diagnostics, provider contracts, and logs can affect user machines. The workflow keeps local operations explicit and reviewable.

Anchor-like work should define service boundaries before implementation. Public API methods, fake clients, health/readiness reports, diagnostics, and provider contracts should be visible to future app layers without exposing provider internals.

Logs and errors should be sanitized so private paths and sensitive values are not exposed. Local operations should be dry-run-first or explicitly apply-gated. Tests should use fake providers, temporary workspaces, and offline checks.

The main lesson is that an app should consume readiness and diagnostics contracts, not provider internals or CLI output.
