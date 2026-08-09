# Example: Small Local Change With No Gates

## Task

Add deterministic alphabetical ordering to an existing in-memory result list.

## Inspect

Locate the existing sorting/result code and its focused tests. Confirm the change is local and does not alter a public persistence format, destructive operation, external provider, or security boundary.

## Implement

Change the existing logic directly. Do not create a sorting interface, provider abstraction, fake provider, spec directory, audit report, Tool Mode declaration, or handoff merely for process compliance.

## Verify

Add or update a focused regression test for ordering and run the relevant test set.

## Review

Inspect the diff for unintended ordering behavior or unrelated edits.

## Gates

None.

If inspection reveals that ordering is actually part of a public contract or spans several independent systems, activate the relevant gate at that point. Do not pre-activate gates for hypothetical complexity.
