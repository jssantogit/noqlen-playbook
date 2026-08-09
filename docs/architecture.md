# Architecture

Architecture guidance is activated by the **Design** escalation when the work makes a durable, cross-cutting, public, or expensive-to-reverse architectural decision.

## Boundaries

Prefer clear boundaries that already exist in the codebase. Change them only when the requested behavior or long-term maintainability justifies it.

Noqlen apps should stay thin over solid cores, services, adapters, or explicit public facades. UI screens should not absorb heavy domain logic merely because they are convenient edit points.

## Public APIs And Contracts

Use explicit contracts where independent consumers need a stable boundary.

A contract is justified when it communicates durable behavior between modules, repositories, services, or app/core layers. It is not justified merely to satisfy a workflow template or to make a fake possible.

A routine edit to an existing public API does not automatically activate Design. Design is activated when the work changes durable API **strategy**, compatibility policy, versioning direction, ownership, or a boundary that future consumers will rely on.

When changing a durable public contract or strategy, consider:

- compatibility and migration impact;
- consumer assumptions;
- error semantics;
- versioning or rollout strategy;
- tests at the behavior boundary.

## Dependencies

Adding a new runtime dependency can activate Design when it creates meaningful maintenance, security, packaging, or operational cost.

Prefer existing capabilities or small local code when they solve the need clearly. Do not add a dependency solely because it makes an agent implementation easier.

A small, replaceable dependency does not require an ADR merely because it is new; persistence and consequence matter more than novelty.

## Data And Storage

Storage format, persistent schema, migration strategy, and path ownership are architectural when downstream code or user data will depend on them.

These changes often activate both Design and Safety.

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

Do not write an ADR for naming, local refactors, routine public API edits within an established strategy, obvious implementation details, or easily reversible choices.

Use `templates/adr/adr-template.md` when an ADR is warranted.

## Review

Architecture review should answer concrete questions rather than restate the design:

- Does the boundary solve a real problem?
- Is the abstraction simpler than the coupling it replaces?
- Is the decision harder to reverse than necessary?
- Does the public surface expose more than consumers need?
- Could the same result be achieved with an existing boundary?
- Are tests placed at the behavior boundary rather than coupled to internals?
