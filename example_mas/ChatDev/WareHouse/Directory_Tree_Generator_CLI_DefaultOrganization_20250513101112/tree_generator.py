'''
Module to generate a visual tree structure of a directory.
'''
import os
def generate_tree_structure(path, max_depth, current_depth=0):
    if current_depth > max_depth:
        return ""
    tree_structure = ""
    try:
        entries = os.listdir(path)
    except PermissionError:
        return get_indentation(current_depth) + "Permission Denied: " + os.path.basename(path) + "\n"
    for entry in entries:
        entry_path = os.path.join(path, entry)
        tree_structure += get_indentation(current_depth) + entry + "\n"
        if os.path.isdir(entry_path):
            tree_structure += generate_tree_structure(entry_path, max_depth, current_depth + 1)
    return tree_structure
def get_indentation(depth):
    return "    " * depth