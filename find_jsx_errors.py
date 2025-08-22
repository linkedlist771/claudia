#!/usr/bin/env python3
"""
Script to find JSX syntax errors where {t("...")} is used in ternary operators
This pattern causes syntax errors and should be t("...") without the extra braces
"""

import os
import re
from pathlib import Path

def find_jsx_errors(directory):
    """Find all potential JSX syntax errors with {t(...)} pattern in ternary operators"""
    errors = []
    
    # Pattern to find problematic {t("...")} in ternary operators
    # This looks for patterns like: ) : (\n{t("...")}
    pattern = re.compile(r'\)\s*:\s*\(\s*\n\s*\{t\(["\'].*?["\']\)\}', re.MULTILINE)
    
    # Also check for single-line versions
    pattern2 = re.compile(r'\)\s*:\s*\(\s*\{t\(["\'].*?["\']\)\}')
    
    # Search all .tsx and .jsx files
    for ext in ['*.tsx', '*.jsx']:
        for file_path in Path(directory).rglob(ext):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Find all matches
                matches = list(pattern.finditer(content)) + list(pattern2.finditer(content))
                
                if matches:
                    # Count line numbers for each match
                    for match in matches:
                        # Find line number
                        line_num = content[:match.start()].count('\n') + 1
                        errors.append({
                            'file': str(file_path),
                            'line': line_num,
                            'text': match.group(0)
                        })
                        
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    
    return errors

def main():
    # Search in src directory
    src_dir = '/Users/a1234/Desktop/GithubProjects/claudia/src'
    
    print("Searching for JSX syntax errors with {t(...)} pattern...")
    errors = find_jsx_errors(src_dir)
    
    if errors:
        print(f"\nFound {len(errors)} potential errors:\n")
        for error in errors:
            print(f"File: {error['file']}")
            print(f"Line: {error['line']}")
            print(f"Pattern: {error['text'][:50]}...")
            print("-" * 50)
    else:
        print("\nNo JSX syntax errors found with {t(...)} pattern!")
    
    return len(errors)

if __name__ == "__main__":
    exit(main())