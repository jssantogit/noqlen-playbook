# Architecture

Architecture guidance is activated by the **Design Gate** in `workflow.md` when a decision is durable, cross-cutting, public, or expensive to reverse.

## Boundaries

Prefer clear boundaries that already exist in the codebase. Change them only when the requested behavior or long-term maintainability justifies it.

Noqlen apps should stay thin over solid cores, services, adapters, or explicit public facades. UI screens should not absorb heavy domain logic merely because they are convenient edit points.

## Public APIs And Contracts

Use explicit contracts where independent consumers need a stable boundary.

A contract is justified when it communicates durable behavior between modules, repositories, services, or app/core layers. It is not justified merely to satisfy a workflow template or to make a fake possible.

When changing a public contract, consider:

- compatibility and migration impact;
- consumer assumptions;
- error semantics;
- versioning or rollout strategy;
- tests at the boundary.

## Dependencies

Adding a new runtime dependency can activate the Design Gate when it creates meaningful maintenance, security, packaging, or operational cost.

Prefer existing capabilities or small local code when they solve the need clearly. Do not add a dependency solely because it makes an agent implementation easier.

## Data And Storage

Storage format, persistent schema, migration strategy, and path ownership are architectural when downstream code or user data will depend on them.

These changes often activate both Design and Safety gates.

## ADR Criteria

Use an ADR when a decision is:

- architectural;
- difficult or costly to reverse;
- likely to be questioned later without historical context;
- relevant to multiple future changes or consumers.

Typical ADR topics:

- storage strategy;
- public API strategy;
- app/core or service boundaries;
- security architecture;
- substantial new runtime dependencies;
- cross-repository contracts.

Do not write an ADR for naming, local refactors, obvious implementation details, or easily reversible choices.

Use `templates/adr/adr-template.md` when an ADR is warranted.

## Review

Architecture review should answer concrete questions rather than restate the design:

- Does the boundary solve a real problem?
- Is the abstraction simpler than the coupling it replaces?
- Is the decision harder to reverse than necessary?
- Does the public surface expose more than consumers need?
- Could the same result be achieved with an existing boundary?
- Are tests placed at the behavior boundary rather than coupled to internals?
