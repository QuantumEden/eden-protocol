#!/usr/bin/env python3
"""
Eden Protocol Precision Import Fixer

A surgical tool for fixing import paths in the Eden Protocol repository with
extreme precision and validation at every step.

Features:
- Context-aware import detection and modification
- Module existence verification before changes
- Import validation after changes
- Duplicate file detection and management
- Comprehensive reporting
- Configurable behavior via command line arguments
- Dry-run mode for safe testing

Author: Manus AI
Date: May 27, 2025
"""

import os
import re
import sys
import ast
import json
import hashlib
import argparse
import importlib
import importlib.util
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Set, Tuple, Optional, Any, Union

# Default configuration
DEFAULT_CONFIG = {
    "target_mappings": {
        "xp.": "infra.xp.",
        "src.xp.": "infra.xp.",
        "zkxp.": "infra.zkxp.",
        "src.zkxp.": "infra.zkxp."
    },
    "canonical_modules": {
        "meritcoin_ledger": "infra.xp.meritcoin_ledger",
        "meritcoin_minter": "infra.xp.meritcoin_minter"
    },
    "exclude_patterns": [
        "__pycache__",
        ".git",
        "venv",
        "env",
        ".pytest_cache"
    ],
    "exclude_files": [
        "import_path_fixer.py",
        "eden_protocol_precision_import_fixer.py"
    ]
}

class ImportAnalyzer(ast.NodeVisitor):
    """AST-based analyzer for import statements."""
    
    def __init__(self):
        self.imports = []
        self.import_froms = []
        self.import_lines = set()
        
    def visit_Import(self, node):
        """Process 'import x' statements."""
        for name in node.names:
            self.imports.append(name.name)
            self.import_lines.add(node.lineno)
        self.generic_visit(node)
        
    def visit_ImportFrom(self, node):
        """Process 'from x import y' statements."""
        if node.module:
            self.import_froms.append(node.module)
            self.import_lines.add(node.lineno)
        self.generic_visit(node)

class VariableAnalyzer(ast.NodeVisitor):
    """AST-based analyzer for variable names and attributes."""
    
    def __init__(self):
        self.variables = set()
        self.attributes = set()
        
    def visit_Name(self, node):
        """Process variable names."""
        self.variables.add(node.id)
        self.generic_visit(node)
        
    def visit_Attribute(self, node):
        """Process attribute access."""
        attrs = []
        current = node
        while isinstance(current, ast.Attribute):
            attrs.append(current.attr)
            current = current.value
        if isinstance(current, ast.Name):
            attrs.append(current.id)
        if attrs:
            self.attributes.add('.'.join(reversed(attrs)))
        self.generic_visit(node)

def find_python_files(root_dir: Path, exclude_patterns: List[str], exclude_files: List[str]) -> List[Path]:
    """Find all Python files in the repository, respecting exclusions."""
    python_files = []
    
    for path in root_dir.rglob("*.py"):
        # Skip excluded patterns
        if any(exclude in str(path) for exclude in exclude_patterns):
            continue
        
        # Skip excluded files
        if path.name in exclude_files:
            continue
            
        if path.is_file():
            python_files.append(path)
            
    return python_files

def calculate_file_hash(file_path: Path) -> str:
    """Calculate SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def find_duplicate_files(files: List[Path]) -> Dict[str, List[Path]]:
    """Find duplicate files based on content hash."""
    file_hashes = {}
    duplicates = defaultdict(list)
    
    for file_path in files:
        file_hash = calculate_file_hash(file_path)
        if file_hash in file_hashes:
            duplicates[file_hash].append(file_path)
        else:
            file_hashes[file_hash] = file_path
            duplicates[file_hash] = [file_path]
    
    # Only return sets with more than one file (actual duplicates)
    return {h: paths for h, paths in duplicates.items() if len(paths) > 1}

def is_module_importable(module_name: str) -> bool:
    """Check if a module can be imported."""
    try:
        spec = importlib.util.find_spec(module_name)
        return spec is not None
    except (ModuleNotFoundError, ValueError):
        return False

def verify_module_exists(module_path: str, root_dir: Path) -> bool:
    """Verify that a module exists at the specified path."""
    # Convert module path (e.g., 'infra.xp.meritcoin_ledger') to file path
    file_path = root_dir.joinpath(*module_path.split('.')).with_suffix('.py')
    return file_path.exists()

def get_import_context(file_content: str, line_idx: int, window: int = 3) -> str:
    """Get context around an import statement for better reporting."""
    lines = file_content.splitlines()
    start = max(0, line_idx - window)
    end = min(len(lines), line_idx + window + 1)
    
    context_lines = []
    for i in range(start, end):
        prefix = "→ " if i == line_idx else "  "
        context_lines.append(f"{prefix}{i+1}: {lines[i]}")
    
    return "\n".join(context_lines)

def analyze_file_imports(file_path: Path) -> Tuple[List[str], List[str], Set[int]]:
    """Analyze imports in a file using AST."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        import_analyzer = ImportAnalyzer()
        import_analyzer.visit(tree)
        
        return import_analyzer.imports, import_analyzer.import_froms, import_analyzer.import_lines
    except SyntaxError:
        # If the file has syntax errors, fall back to regex-based analysis
        imports = []
        import_froms = []
        import_lines = set()
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if re.match(r'^\s*import\s+', line):
                    modules = re.findall(r'import\s+([\w\.]+)', line)
                    imports.extend(modules)
                    import_lines.add(i)
                elif re.match(r'^\s*from\s+', line):
                    modules = re.findall(r'from\s+([\w\.]+)', line)
                    import_froms.extend(modules)
                    import_lines.add(i)
        
        return imports, import_froms, import_lines

def analyze_file_variables(file_path: Path) -> Tuple[Set[str], Set[str]]:
    """Analyze variable names and attributes in a file using AST."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        var_analyzer = VariableAnalyzer()
        var_analyzer.visit(tree)
        
        return var_analyzer.variables, var_analyzer.attributes
    except SyntaxError:
        # If the file has syntax errors, return empty sets
        return set(), set()

def fix_imports(
    file_path: Path, 
    target_mappings: Dict[str, str],
    canonical_modules: Dict[str, str],
    root_dir: Path,
    dry_run: bool = True,
    verify_imports: bool = True,
    context_aware: bool = True
) -> Tuple[bool, List[Dict[str, str]], List[str]]:
    """
    Fix imports in a file with surgical precision.
    
    Args:
        file_path: Path to the file to fix
        target_mappings: Mapping of problematic imports to their correct versions
        canonical_modules: Mapping of module names to their canonical import paths
        root_dir: Root directory of the repository
        dry_run: If True, don't actually modify the file
        verify_imports: If True, verify that the new imports are valid
        context_aware: If True, use AST to ensure we only modify actual imports
        
    Returns:
        Tuple of (changed, changes, warnings)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use AST to identify actual import statements and their line numbers
    imports, import_froms, import_lines = analyze_file_imports(file_path)
    
    if context_aware:
        # Also analyze variable names and attributes to avoid modifying them
        variables, attributes = analyze_file_variables(file_path)
    
    lines = content.splitlines()
    new_lines = []
    changed = False
    changes = []
    warnings = []
    
    for i, line in enumerate(lines):
        new_line = line
        original_line = line
        
        # Only process import statements if context_aware is True
        if context_aware and i not in import_lines:
            new_lines.append(new_line)
            continue
        
        # Fix import statements
        for bad_prefix, good_prefix in target_mappings.items():
            # Careful replacement to avoid modifying variable names
            if bad_prefix in line and good_prefix not in line:
                # For 'import x' statements
                import_match = re.search(r'import\s+([\w\.]+)', line)
                if import_match and bad_prefix in import_match.group(1):
                    module_name = import_match.group(1)
                    new_module_name = module_name.replace(bad_prefix, good_prefix)
                    new_line = line.replace(f"import {module_name}", f"import {new_module_name}")
                
                # For 'from x import y' statements
                from_match = re.search(r'from\s+([\w\.]+)', line)
                if from_match and bad_prefix in from_match.group(1):
                    module_name = from_match.group(1)
                    new_module_name = module_name.replace(bad_prefix, good_prefix)
                    new_line = line.replace(f"from {module_name}", f"from {new_module_name}")
                
                # Only apply the change if it modified an actual import
                if new_line != line:
                    # Verify the new module exists if requested
                    if verify_imports:
                        new_module_match = re.search(r'(?:import|from)\s+([\w\.]+)', new_line)
                        if new_module_match:
                            new_module = new_module_match.group(1)
                            if not verify_module_exists(new_module, root_dir):
                                warnings.append(f"Module not found: {new_module} in {file_path}")
                                new_line = line  # Revert the change
                    
                    if new_line != line:
                        changed = True
                        changes.append({
                            "file": str(file_path),
                            "line": i + 1,
                            "before": line,
                            "after": new_line,
                            "context": get_import_context(content, i)
                        })
        
        new_lines.append(new_line)
    
    # Only write the file if changes were made and this is not a dry run
    if changed and not dry_run:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
            # Add trailing newline if original file had one
            if content.endswith('\n'):
                f.write('\n')
    
    return changed, changes, warnings

def rename_duplicate_files(
    duplicates: Dict[str, List[Path]], 
    canonical_modules: Dict[str, str],
    root_dir: Path,
    dry_run: bool = True
) -> List[Dict[str, str]]:
    """
    Rename duplicate files to .example extension, keeping canonical files.
    
    Args:
        duplicates: Dictionary mapping file hashes to lists of duplicate file paths
        canonical_modules: Mapping of module names to their canonical import paths
        root_dir: Root directory of the repository
        dry_run: If True, don't actually rename files
        
    Returns:
        List of dictionaries with information about renamed files
    """
    renamed_files = []
    
    # Convert canonical module paths to file paths
    canonical_file_paths = {}
    for module_name, module_path in canonical_modules.items():
        file_path = root_dir.joinpath(*module_path.split('.')).with_suffix('.py')
        canonical_file_paths[module_name] = file_path
    
    for hash_val, paths in duplicates.items():
        # Skip __init__.py files regardless of content
        if any(path.name == "__init__.py" for path in paths):
            continue
        
        # Check if any of the duplicates match our canonical modules
        canonical_path = None
        for path in paths:
            for module_name, canon_path in canonical_file_paths.items():
                if path.name == f"{module_name}.py" and str(canon_path) in str(path):
                    canonical_path = path
                    break
            if canonical_path:
                break
        
        # If no canonical path was found, use the first one
        if not canonical_path and paths:
            canonical_path = paths[0]
        
        # Rename non-canonical duplicates
        for path in paths:
            if path != canonical_path:
                new_path = path.with_suffix('.py.example')
                renamed_files.append({
                    "original": str(path),
                    "renamed": str(new_path),
                    "canonical": str(canonical_path) if canonical_path else None
                })
                
                if not dry_run:
                    try:
                        path.rename(new_path)
                    except Exception as e:
                        print(f"Error renaming {path}: {e}")
    
    return renamed_files

def generate_report(
    changes: List[Dict[str, str]],
    warnings: List[str],
    renamed_files: List[Dict[str, str]],
    duplicates: Dict[str, List[Path]],
    dry_run: bool,
    output_file: Path,
    json_output: Optional[Path] = None
) -> None:
    """
    Generate a comprehensive report of all changes and issues.
    
    Args:
        changes: List of dictionaries with information about changed imports
        warnings: List of warning messages
        renamed_files: List of dictionaries with information about renamed files
        duplicates: Dictionary mapping file hashes to lists of duplicate file paths
        dry_run: Whether this was a dry run
        output_file: Path to write the report to
        json_output: Optional path to write a JSON version of the report
    """
    # Count changes by file
    changes_by_file = Counter(change["file"] for change in changes)
    
    # Generate markdown report
    report = [
        "# 🔬 Eden Protocol Precision Import Fixer Report",
        "",
        f"**Mode:** `{'--dry-run' if dry_run else '--apply'}`",
        f"**Files Modified:** {len(changes_by_file)} {'(would be modified)' if dry_run else ''}",
        f"**Import Statements Fixed:** {len(changes)} {'(would be fixed)' if dry_run else ''}",
        f"**Duplicate Files Renamed:** {len(renamed_files)} {'(would be renamed)' if dry_run else ''}",
        f"**Warnings:** {len(warnings)}",
        ""
    ]
    
    # Summary of changes by file
    if changes_by_file:
        report.extend([
            "## 📊 Changes Summary",
            "",
            "| File | Changes |",
            "|------|---------|",
        ])
        
        for file, count in changes_by_file.most_common():
            report.append(f"| `{file}` | {count} |")
        
        report.append("")
    
    # Detailed changes
    if changes:
        report.extend([
            "## 🔍 Detailed Changes",
            ""
        ])
        
        current_file = None
        for change in changes:
            if current_file != change["file"]:
                current_file = change["file"]
                report.extend([
                    f"### {current_file}",
                    ""
                ])
            
            report.extend([
                f"**Line {change['line']}:**",
                "```python",
                f"Before: {change['before']}",
                f"After:  {change['after']}",
                "```",
                "",
                "**Context:**",
                "```",
                change["context"],
                "```",
                ""
            ])
    
    # Duplicate files
    if duplicates:
        report.extend([
            "## 🔄 Duplicate Files",
            ""
        ])
        
        for hash_val, paths in duplicates.items():
            if any(path.name == "__init__.py" for path in paths):
                continue  # Skip __init__.py files
                
            report.extend([
                f"**Hash:** `{hash_val[:8]}...`",
                ""
            ])
            
            for path in paths:
                report.append(f"- `{path}`")
            
            report.append("")
    
    # Renamed files
    if renamed_files:
        report.extend([
            "## 📝 Renamed Files",
            "",
            "| Original | Renamed | Canonical |",
            "|----------|---------|-----------|",
        ])
        
        for rename in renamed_files:
            report.append(f"| `{rename['original']}` | `{rename['renamed']}` | `{rename['canonical'] or 'N/A'}` |")
        
        report.append("")
    
    # Warnings
    if warnings:
        report.extend([
            "## ⚠️ Warnings",
            ""
        ])
        
        for warning in warnings:
            report.append(f"- {warning}")
        
        report.append("")
    
    # Next steps
    report.extend([
        "## 🚀 Next Steps",
        "",
        "1. Review the changes made to import statements",
        "2. Check warnings for potential issues",
        "3. Review renamed duplicate files",
        "4. Run tests to verify the fixes resolved the import errors",
        "5. If this was a dry run, run with `--apply` to apply the changes",
        ""
    ])
    
    # Write the report
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    # Write JSON report if requested
    if json_output:
        json_report = {
            "mode": "dry-run" if dry_run else "apply",
            "files_modified": len(changes_by_file),
            "imports_fixed": len(changes),
            "duplicates_renamed": len(renamed_files),
            "warnings": len(warnings),
            "changes": changes,
            "warnings_list": warnings,
            "renamed_files": renamed_files,
            "duplicates": {h: [str(p) for p in paths] for h, paths in duplicates.items()}
        }
        
        with open(json_output, 'w', encoding='utf-8') as f:
            json.dump(json_report, f, indent=2)

def main():
    parser = argparse.ArgumentParser(
        description="Eden Protocol Precision Import Fixer - A surgical tool for fixing import paths",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry run to see what would be changed
  python eden_protocol_precision_import_fixer.py --dry-run
  
  # Apply changes
  python eden_protocol_precision_import_fixer.py --apply
  
  # Apply changes with custom configuration
  python eden_protocol_precision_import_fixer.py --apply --config my_config.json
  
  # Apply changes and generate JSON report
  python eden_protocol_precision_import_fixer.py --apply --json-report report.json
        """
    )
    
    # Mode arguments
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("--dry-run", action="store_true", help="Simulate changes without modifying files")
    mode_group.add_argument("--apply", action="store_true", help="Apply fixes to files")
    
    # Path arguments
    parser.add_argument("--path", type=str, default=".", help="Path to the repository root")
    parser.add_argument("--report", type=str, default="import_fix_report.md", help="Path to output report file")
    parser.add_argument("--json-report", type=str, help="Path to output JSON report file")
    
    # Configuration arguments
    parser.add_argument("--config", type=str, help="Path to configuration JSON file")
    parser.add_argument("--no-verify", action="store_true", help="Skip verification of module existence")
    parser.add_argument("--no-context", action="store_true", help="Disable context-aware import detection")
    parser.add_argument("--no-rename", action="store_true", help="Skip renaming duplicate files")
    
    args = parser.parse_args()
    
    # Load configuration
    config = DEFAULT_CONFIG.copy()
    if args.config:
        try:
            with open(args.config, 'r') as f:
                custom_config = json.load(f)
                config.update(custom_config)
        except Exception as e:
            print(f"Error loading configuration: {e}")
            return 1
    
    # Set up paths
    root_dir = Path(args.path).resolve()
    report_path = Path(args.report)
    json_report_path = Path(args.json_report) if args.json_report else None
    
    # Find Python files
    python_files = find_python_files(
        root_dir, 
        config.get("exclude_patterns", []),
        config.get("exclude_files", [])
    )
    print(f"Found {len(python_files)} Python files")
    
    # Find duplicate files
    duplicates = find_duplicate_files(python_files)
    print(f"Found {len(duplicates)} sets of duplicate files")
    
    # Fix imports
    all_changes = []
    all_warnings = []
    
    for file_path in python_files:
        changed, changes, warnings = fix_imports(
            file_path,
            config.get("target_mappings", {}),
            config.get("canonical_modules", {}),
            root_dir,
            dry_run=args.dry_run,
            verify_imports=not args.no_verify,
            context_aware=not args.no_context
        )
        
        all_changes.extend(changes)
        all_warnings.extend(warnings)
    
    print(f"Fixed {len(all_changes)} import statements in {len(set(change['file'] for change in all_changes))} files")
    
    # Rename duplicate files
    renamed_files = []
    if not args.no_rename:
        renamed_files = rename_duplicate_files(
            duplicates,
            config.get("canonical_modules", {}),
            root_dir,
            dry_run=args.dry_run
        )
        print(f"Renamed {len(renamed_files)} duplicate files")
    
    # Generate report
    generate_report(
        all_changes,
        all_warnings,
        renamed_files,
        duplicates,
        args.dry_run,
        report_path,
        json_report_path
    )
    print(f"Report generated: {report_path}")
    if json_report_path:
        print(f"JSON report generated: {json_report_path}")
    
    # Print summary
    print("\nSummary:")
    print(f"- Files scanned: {len(python_files)}")
    print(f"- Files modified: {len(set(change['file'] for change in all_changes))}")
    print(f"- Import statements fixed: {len(all_changes)}")
    print(f"- Duplicate files renamed: {len(renamed_files)}")
    print(f"- Warnings: {len(all_warnings)}")
    
    if args.dry_run:
        print("\nThis was a dry run. No files were modified.")
        print("Run with --apply to apply the changes.")
    else:
        print("\nAll changes have been applied.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
