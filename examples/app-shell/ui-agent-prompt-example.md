# UI Agent Prompt Example

Task: implement one UI block for displaying local service readiness status.

Scope: screen and state wiring for the fake provider only.

Requirements:

- Keep UI thin.
- Use fake provider.
- Do not access direct core internals.
- Validate state behavior.
- Do not expose private paths or sensitive data in UI errors.

Allowed files: `<screen, state, fake provider, tests>`

Forbidden files: `<core internals, release files, unrelated screens>`

Validation: `<commands>`

Stop condition: stop after the UI block is complete or if contract changes are needed.
