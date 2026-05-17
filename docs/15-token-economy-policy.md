# Token Economy Policy

Token economy is secondary to correctness, clarity, and auditability. The goal is less waste without weaker evidence.

## Rules

- Use the smallest safe context: `tiny`, `standard`, or `full`.
- Prefer semantic retrieval over reading whole files when symbol-level context is enough.
- Prefer summarized command output during exploration.
- Preserve raw evidence for failures, high-risk work, and audits.
- Do not compress away touched files, validation commands, raw failures, risks, assumptions, stop conditions, or security findings.
- Re-run with raw output when a compressed summary is ambiguous.
- Installing token tools is not enough; the agent must still choose tiny, standard, or full context correctly.
- RTK and Context Mode metrics are useful, but they are not audit proof.
- Raw evidence is mandatory for serious debugging, validation failures, release readiness, boundary changes, high-risk audits, and security-sensitive work.
- Final reports must include touched files, validation commands, risks, assumptions, and stop conditions.

## Safe Context Reduction

Context reduction is safe when the block remains understandable, scope remains explicit, and validation evidence remains reproducible. It is unsafe when it hides requirements, file boundaries, failure details, or audit findings.

## Metrics

Track these when piloting token-saving tooling:

- Context level used.
- Tool mode used.
- Commands compressed.
- Raw evidence availability.
- Re-runs caused by missing details.
- Audit findings caused by insufficient context.

Good token economy reduces waste without making the handoff, audit, or next block less reliable.

Token economy must never remove required final-report details. Compressed output is useful during exploration, but it must not hide failures or become the only audit evidence.
