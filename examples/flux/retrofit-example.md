# Flux Retrofit Example

## Goal

Retrofit specs, fakes, contracts, and safety checks into a Flux-like repository.

## Steps

- Inventory provider contracts, search models, transfer models, staging models, cleanup models, and handoff models.
- Add current context that names the active provider/import boundary.
- Add a spec for the next risky boundary before implementation.
- Add fake-first examples for provider responses, queue states, quality outcomes, routing decisions, and staging plans.
- Add dry-run-first validation for workspace writes, staging, cleanup, reports, and handoff generation.
- Add audit checks for path containment, quarantine routing, rejected states, no-network default, and no real library access.

## Stop condition

Stop if the retrofit starts implementing real provider access, real downloads, real imports, or real cleanup behavior.
