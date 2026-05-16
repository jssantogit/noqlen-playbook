# Flux Workflow Retrospective

A search/download/import core benefits from the current workflow because provider, transfer, staging, cleanup, and handoff behavior can become risky quickly. The workflow keeps those risks bounded with contracts before execution.

Flux-like work should start with provider-neutral models, fake providers, no network by default in tests, and explicit planning results. Real provider access, downloads, imports, cleanup, and handoff should each have separate apply boundaries.

Quarantine and rejected states should be modeled before import behavior. Path safety, traversal protection, symlink checks, workspace containment, and dry-run-first execution should be part of the spec, not discovered late in implementation.

The playbook lesson is to split risky provider/import work into small blocks: contract, fake provider, planning service, dry-run execution boundary, apply gate, audit, and handoff.
