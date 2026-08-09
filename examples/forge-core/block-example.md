# Example: Small Local Change Without Extra Process

Task: add deterministic alphabetical ordering to an existing in-memory result list.

The relevant sorting code and focused tests already make the implementation path obvious. Change the existing logic directly, add or update the focused regression test, run the relevant test set, and inspect the diff for unintended ordering behavior or unrelated edits.

Do not create a sorting interface, provider abstraction, fake provider, spec directory, audit report, Tool Mode declaration, handoff, risk tier, or process-status checklist merely for compliance.

No planning artifact, architecture record, formal audit, or isolation technique is needed unless inspection reveals a concrete reason — for example, the ordering actually defines a durable public compatibility contract or depends on an external system.
