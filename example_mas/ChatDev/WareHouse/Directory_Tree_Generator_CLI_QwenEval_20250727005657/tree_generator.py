'''
Module for generating the directory tree structure.
'''
import os
from pathlib import Path
def generate_tree(path, max_depth=None, _prefix='', _root=True):
    '''Generate the tree structure of a given directory up to a specified maximum depth.'''
    path = Path(path)
    if not path.exists():
        return [f"{_prefix}Path does not exist: {path}"]
    if path.is_file():
        raise ValueError(f"Provided path is a file, not a directory: {path}")
    try:
        entries = list(path.iterdir())
    except FileNotFoundError:
        return [f"{_prefix}Directory not found: {path}"]
    except PermissionError:
        return [f"{_prefix}Permission denied: {path}"]
    entries.sort(key=lambda entry: entry.is_file())
    tree = []
    for i, entry in enumerate(entries):
        connector = '└── ' if i == len(entries) - 1 else '├── '
        if _root:
            connector = ''
        tree.append(_prefix + connector + entry.name)
        if entry.is_dir() and (max_depth is None or max_depth > 1):
            subtree = generate_tree(entry, max_depth - 1 if max_depth is not None else None, _prefix + ('    ' if i == len(entries) - 1 else '│   '), False)
            tree.extend(subtree)
    return tree
def print_tree(tree):
    '''Print the tree structure to the console.'''
    for line in tree:
        print(line)