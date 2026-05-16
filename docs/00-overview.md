# Overview

Noqlen Playbook is the operating guide for AI-assisted software work in the Noqlen ecosystem. It documents how planning, scoped prompts, implementation, validation, audits, handoffs, and GitHub history fit together.

Noqlen uses this method because the ecosystem has multiple cores, public interfaces, future apps, and safety-sensitive file workflows. Work must stay repeatable, reviewable, and bounded.

The playbook solves common AI-assisted development risks:

- Too much context causing drift.
- Broad rewrites instead of scoped changes.
- Missing validation before claiming completion.
- Unclear handoffs between human planning and agent execution.
- Accidental exposure of secrets, paths, private data, lyrics, or fingerprints.
- App code absorbing domain logic that belongs in cores or contracts.

For future app development, the playbook keeps apps thin over solid cores by requiring contracts, fake providers, state models, validation, and audits. For future AI workflows, it provides boundaries that can be reused by app agents, audit agents, release agents, documentation agents, migration agents, and data safety agents.
