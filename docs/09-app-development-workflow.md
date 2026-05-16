# App Development Workflow

Apps are shells and controllers over solid cores. UI should not own heavy domain logic. App features should start from contracts and state models, then use fake providers before real integration.

Required workflow:

Feature idea -> UX/state sketch -> Core/API contract -> Fake provider -> Screen/state implementation -> Integration boundary -> Validation -> Audit

Required rules:

- Do not put critical domain logic inside UI screens.
- Do not make app code depend on undocumented core behavior.
- App integrations must use public facades, adapters, or contracts.
- App tests should use fake providers first.
- UI errors must not expose private paths or sensitive data.

Keep screen, state, and use-case responsibilities separate. Audit UI flows, data safety, and app/core boundaries before treating an app block as complete.
