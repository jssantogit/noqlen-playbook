#!/usr/bin/env python3
"""Validate the essential Noqlen Playbook V2 structure and canonical workflow."""

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
        "Triggered Gates",
    ],
    "docs/workflow.md": [
        "Plan Gate",
        "Design Gate",
        "Safety Gate",
        "Fake Gate",
        "Audit Gate",
        "Handoff Gate",
        "Do not create an interface only so a fake can exist.",
    ],
    "AGENTS.md": [
        "Validate changed behavior before claiming completion.",
        "Do not invent an abstraction only to create a fake.",
    ],
}

LEGACY_PATHS = [
    "templates/context",
    "templates/specs",
    "templates/prompts",
]

LEGACY_NUMBERED_DOCS = [f"docs/{number:02d}-" for number in range(20)]


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

    if failures:
        print("Playbook V2 validation failures:")
        for failure in failures:
            print(f"- {failure}")
        print("FAIL: playbook does not match the V2 essential structure.")
        return 1

    print("PASS: playbook matches the V2 essential structure.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
