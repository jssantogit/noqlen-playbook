# Opencode Prompt: Plan Block

Purpose: Ask Opencode to inspect context and propose a block plan without editing files.

## Prompt

Read the listed files and do not edit files.

Task: inspect the current context and propose a scoped block plan.

Context: `<files and notes>`

Requirements:

- Summarize current state.
- Propose commit-sized blocks.
- Identify risks and validation needs.
- Identify files likely needed per block.
- Do not edit files.

Output: current state, proposed blocks, risks, recommended first block, and stop conditions.
