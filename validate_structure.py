#!/usr/bin/env python3
"""
Project Structure Validator for DL-Simplified
Validates that project folders follow the repository's structure guidelines.
"""

import os
import sys
from pathlib import Path

REQUIRED_DIRS = ["Dataset", "Model", "Images"]
REQUIRED_FILES = ["README.md", "requirements.txt"]


def validate_project(project_path: Path) -> list[str]:
    """Validate a single project folder structure."""
    issues = []

    # Check required directories
    for req_dir in REQUIRED_DIRS:
        found = False
        for item in project_path.iterdir():
            if item.is_dir() and item.name.lower() == req_dir.lower():
                if item.name != req_dir:
                    issues.append(f"  FAIL {item.name}/ -> Should be {req_dir}/")
                else:
                    found = True
        if not found:
            issues.append(f"  MISSING {req_dir}/")

    # Check required files
    for req_file in REQUIRED_FILES:
        found = False
        for item in project_path.iterdir():
            if item.is_file() and item.name.lower() == req_file.lower():
                if item.name != req_file:
                    issues.append(f"  FAIL {item.name} -> Should be {req_file}")
                else:
                    found = True
        if not found:
            issues.append(f"  MISSING {req_file}")

    return issues


def main():
    """Main validation function."""
    repo_root = Path(".")
    project_dirs = []

    for item in repo_root.iterdir():
        if item.is_dir() and not item.name.startswith("."):
            has_dataset = any(
                sub.name.lower() == "dataset" for sub in item.iterdir() if sub.is_dir()
            )
            has_model = any(
                sub.name.lower() == "model" for sub in item.iterdir() if sub.is_dir()
            )
            if has_dataset or has_model:
                project_dirs.append(item)

    print(f"Found {len(project_dirs)} project directories\n")

    total_issues = 0
    projects_with_issues = 0

    for project in sorted(project_dirs):
        issues = validate_project(project)
        if issues:
            projects_with_issues += 1
            total_issues += len(issues)
            print(f"Checking: {project.name}")
            for issue in issues:
                print(issue)
            print()

    print("=" * 50)
    print(f"Summary:")
    print(f"  Projects checked: {len(project_dirs)}")
    print(f"  Projects with issues: {projects_with_issues}")
    print(f"  Total issues: {total_issues}")

    return 0 if total_issues == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
