# Block-Based Development

Every block must define:

- Goal.
- Scope.
- Allowed files.
- Forbidden files.
- Non-goals.
- Validation commands.
- Done criteria.
- Stop condition.

Split a block when it crosses unrelated modules, requires different validation strategies, mixes planning with implementation, or cannot be reviewed as a single commit-sized change.

Stop when the block goal is complete, validation fails in a way that changes scope, forbidden files are needed, requirements are unclear, or destructive operations would be required.

Audit after large blocks, risky blocks, public API changes, file operation changes, app/core boundary changes, or release preparation.

Avoid scope creep by preserving non-goals, rejecting opportunistic rewrites, and moving new ideas into the next block or a separate spec.
