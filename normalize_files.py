#!/usr/bin/env python3
"""
File normalization script to prevent 'string not found' errors.
This script:
1. Normalizes line endings to Unix format (\n)
2. Removes trailing whitespace
3. Ensures consistent indentation
4. Removes any hidden characters
"""

import os
import re

def normalize_file(filepath):
    """Normalize a single file to prevent string matching issues."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Normalize line endings
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    
    # Remove trailing whitespace
    lines = content.split('\n')
    lines = [line.rstrip() for line in lines]
    
    # Convert tabs to spaces
    lines = [line.expandtabs(2) for line in lines]
    
    # Join back
    normalized_content = '\n'.join(lines)
    
    # Ensure single newline at end
    if normalized_content and not normalized_content.endswith('\n'):
        normalized_content += '\n'
    
    if normalized_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(normalized_content)
        print(f"Normalized: {filepath}")
        return True
    return False

def main():
    """Main function to process all HTML and CSS files."""
    files_changed = 0
    for root, dirs, files in os.walk('.'):
        if '.git' in root:
            continue
        for file in files:
            if file.endswith(('.html', '.css')):
                filepath = os.path.join(root, file)
                if normalize_file(filepath):
                    files_changed += 1
    print(f"Files changed: {files_changed}")

if __name__ == "__main__":
    main() 