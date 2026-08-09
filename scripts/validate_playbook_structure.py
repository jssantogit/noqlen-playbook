#!/usr/bin/env python3
"""Validate the essential Noqlen Playbook V2.2 structure and canonical workflow."""

from pathlib import Path
import sys


REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "docs/workflow.md",
    "docs/safety.md",
    "docs/testing.md",
    "docs/architecture.md",
    "docs/release.md",
    "docs/tooling.md",
    "templates/change-brief.md",
    "templates/handoff.md",
    "templates/adr/adr-template.md",
    "scripts/check_repo_contamination.py",
    "scripts/validate_playbook_structure.py",
    ".github/workflows/playbook-validate.yml",
]

REQUIRED_DIRS = [
    "docs",
    "templates",
    "templates/adr",
    "scripts",
    ".github/workflows",
]

REQUIRED_TEXT = {
    "README.md": [
        "Inspect -> Implement -> Verify -> Review",
        "Triggered Escalations",
        "Isolation Rule",
        "Delegation Rule",
        "Harness Feedback Rule",
        "Handoff Trigger",
        "Do the work; do not narrate the process.",
        "do not ask for the same confirmation twice",
        "Prefer observable outcomes over agent claims",
    ],
    "docs/workflow.md": [
        "The four escalations are **Plan, Design, Safety, and Audit**.",
        "Isolation Rule",
        "Delegation Rule",
        "Harness Feedback Rule",
        "Handoff Trigger",
        "Do not create an interface only so a fake can exist.",
        "Do not enumerate inactive escalations.",
        "Diff size alone does not activate Audit.",
        "Delegate when **separate context or independent execution saves more work than coordination costs**.",
        "Durable agent guidance should come from observed need, not speculation.",
    ],
    "docs/safety.md": [
        "Authorization And Apply Intent",
        "Read-only inspection of user-authorized real data does not by itself require a confirmation pause.",
        "Do not ask the user to confirm the same action twice.",
        "Implementation Versus Real Execution",
        "does **not** itself require user confirmation",
    ],
    "docs/testing.md": [
        "Outcome Verification",
        "Agent claims such as \"implemented\", \"fixed\", or \"looks correct\" are not verification evidence by themselves.",
        "Isolation is a verification technique, not a workflow phase or gate that must be declared.",
        "Parallel Verification",
    ],
    "docs/tooling.md": [
        "Capabilities Before Brands",
        "Skills And Reusable Procedures",
        "Subagents And Workspaces",
        "Permissions, Sandboxes, And Hooks",
        "Search, Context, And Observability",
        "Harness Feedback",
    ],
    "AGENTS.md": [
        "Validate changed behavior before claiming completion.",
        "do not ask for the same confirmation twice.",
        "Do not invent an abstraction only to create a fake.",
        "When the same correction or failure recurs",
        "Treat third-party skills, plugins, MCP servers, and agent packages as software trust dependencies",
        "Diff size or task duration alone does not require formal audit, delegation, planning, or branch isolation.",
    ],
}

LEGACY_PATHS = [
    "templates/context",
    "templates/specs",
    "templates/prompts",
]

LEGACY_NUMBERED_DOCS = [f"docs/{number:02d}-" for number in range(20)]

FORBIDDEN_ACTIVE_PHRASES = [
    "Triggered Gates",
    "Plan Gate",
    "Design Gate",
    "Safety Gate",
    "Fake Gate",
    "Audit Gate",
    "Handoff Gate",
]

SCAN_ROOTS = ["README.md", "AGENTS.md", "docs", "templates", "examples"]


def iter_active_text_files(root: Path):
    for relative in SCAN_ROOTS:
        path = root / relative
        if path.is_file():
            yield path
            continue
        if not path.is_dir():
            continue
        for child in path.rglob("*"):
            if child.is_file() and child.suffix.lower() in {".md", ".txt", ".py", ".yml", ".yaml", ".json", ".jsonc"}:
                yield child


def main() -> int:
    root = Path.cwd()
    failures: list[str] = []

    for path in REQUIRED_DIRS:
        if not (root / path).is_dir():
            failures.append(f"missing required directory: {path}")

    for path in REQUIRED_FILES:
        if not (root / path).is_file():
            failures.append(f"missing required file: {path}")

    for path, phrases in REQUIRED_TEXT.items():
        file_path = root / path
        if not file_path.is_file():
            continue
        text = file_path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                failures.append(f"{path} is missing canonical text: {phrase!r}")

    for path in LEGACY_PATHS:
        if (root / path).exists():
            failures.append(f"legacy process directory still present: {path}")

    docs_dir = root / "docs"
    if docs_dir.is_dir():
        for path in docs_dir.iterdir():
            if not path.is_file():
                continue
            relative = f"docs/{path.name}"
            if any(relative.startswith(prefix) for prefix in LEGACY_NUMBERED_DOCS):
                failures.append(f"legacy numbered workflow doc still present: {relative}")

    for path in iter_active_text_files(root):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root)
        for phrase in FORBIDDEN_ACTIVE_PHRASES:
            if phrase in text:
                failures.append(f"legacy gate terminology in {relative}: {phrase!r}")

    if failures:
        print("Playbook V2.2 validation failures:")
        for failure in failures:
            print(f"- {failure}")
        print("FAIL: playbook does not match the V2.2 essential structure.")
        return 1

    print("PASS: playbook matches the V2.2 essential structure.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
