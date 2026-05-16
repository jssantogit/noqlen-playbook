# Testing And Validation

Use risk-based testing. Low-risk documentation blocks may need structure checks. File operations, security-sensitive behavior, public APIs, and app/core boundaries need stronger validation.

Use fake-first development for integrations. Build with fake providers and fixtures before connecting real services or user data.

Use dry-run-first behavior for operations that move, delete, import, write, or publish data. Apply mode must be explicit and reviewed.

Prefer contract tests around public facades, adapters, and app/core boundaries. Validate path handling, symlink behavior, traversal prevention, and safe error messages.

Automated tests must never use a real music library. Use synthetic metadata and fake paths. When suspicious files are relevant, quarantine them through explicit safe flows rather than processing them directly.
