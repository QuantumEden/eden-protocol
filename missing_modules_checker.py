#!/usr/bin/env python3
"""
missing_modules_checker.py

Scans the Eden Protocol repository for broken import statements and unresolved modules.
This tool does not modify anything—it only reports what is missing or misaligned.

Designed for continuous diagnostics before or after import path refactoring.

Author: Eidolon & Manus
Date: May 27, 2025
"""

import os
import ast
import sys
import importlib.util
import argparse
from pathlib import Path
from typing import List, Dict

# Exclude patterns and directories
EXCLUDED_DIRS = {"venv", "env", ".git", "__pycache__", ".pytest_cache"}
EXCLUDED_FILES = {"eden_import_fixer.py", "missing_modules_checker.py"}

# Default output file
DEFAULT_REPORT_PATH = "missing_imports_report.md"


def find_python_files(root_path: Path) -> List[Path]:
    """Find all Python files recursively, excluding defined patterns."""
    python_files = []
    for path in root_path.rglob("*.py"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        if path.name in EXCLUDED_FILES:
            continue
        python_files.append(path)
    return python_files


def extract_imports(file_path: Path) -> List[Dict[str, str]]:
    """Extract all import statements using AST parsing."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        tree = ast.parse(content, filename=str(file_path))
    except SyntaxError:
        return []

    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append({"module": alias.name, "lineno": node.lineno})
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                full_module = "." * node.level + node.module
                imports.append({"module": full_module, "lineno": node.lineno})
    return imports


def is_resolvable(module: str) -> bool:
    """Check if a module can be resolved."""
    if module.startswith("."):
        return True  # skip relative for now, assumed contextual
    try:
        return importlib.util.find_spec(module) is not None
    except (ModuleNotFoundError, ValueError):
        return False


def scan_repository(root_path: Path) -> List[Dict[str, str]]:
    """Scan for unresolved imports."""
    python_files = find_python_files(root_path)
    issues = []

    for file_path in python_files:
        imports = extract_imports(file_path)
        for imp in imports:
            module = imp["module"]
            if not is_resolvable(module):
                issues.append({
                    "file": str(file_path.relative_to(root_path)),
                    "line": imp["lineno"],
                    "module": module
                })

    return issues


def write_report(issues: List[Dict[str, str]], report_path: Path) -> None:
    """Write a human-readable Markdown report."""
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# ❌ Missing Modules Report\n\n")
        if not issues:
            f.write("✅ No unresolved imports found.\n")
            return

        f.write(f"**Total Issues Found:** {len(issues)}\n\n")
        f.write("## 📂 Breakdown\n\n")
        for issue in issues:
            f.write(f"- `{issue['file']}` (Line {issue['line']}): `import {issue['module']}`\n")
        f.write("\n---\n\nRun this script after major import changes or before applying refactors.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Scan for unresolved imports in the Eden Protocol repository."
    )
    parser.add_argument("--path", type=str, default=".", help="Root path to scan")
    parser.add_argument("--report", type=str, default=DEFAULT_REPORT_PATH, help="Markdown report file")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    issues = scan_repository(root)

    report_path = root / args.report
    write_report(issues, report_path)

    print(f"\n🔍 Scan complete. Found {len(issues)} issue(s).")
    print(f"📄 Report saved to: {report_path}\n")

    if issues:
        print("⚠️ Suggested Next Steps:")
        print("- Review import paths in affected files")
        print("- Ensure modules exist and __init__.py files are present")
        print("- Adjust resolver paths or module placement if needed")


if __name__ == "__main__":
    main()
