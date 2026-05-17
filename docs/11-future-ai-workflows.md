# Future AI Workflows

This playbook can support future app agents, audit agents, release agents, documentation agents, migration agents, and data safety agents.

Future agents should be bounded by explicit allowed files, forbidden files, capabilities, validation commands, and stop conditions. They should use the smallest useful context and avoid autonomous destructive actions.

Future agents may use optional tooling only through explicit Tool Mode. Tool capabilities must be bounded by the block. Tooling should be piloted before becoming recommended.

Future project handoffs may include this playbook as an environment bootstrap source. Agents must prepare the environment first, report tooling state, and then implement only in a separate block unless explicitly requested.

New tools must be piloted before becoming default. Future agents may have tool capabilities, but those capabilities must be explicit, bounded, and reported.

High-risk changes require human review. This includes destructive operations, security policy changes, public API changes, storage changes, release actions, and app/core boundary changes.

## Repo Study Agents

Future repo study agents may inspect existing Noqlen repositories to extract workflow lessons. They must be strictly read-only, avoid tests or commands that write artifacts, produce sanitized summaries, omit absolute local paths, and never copy secrets, private data, lyrics, fingerprints, or real library paths.

Human review is required before turning repo study output into templates, specs, or migration work. Study agents recommend; they do not refactor, stage, commit, publish, or merge.
