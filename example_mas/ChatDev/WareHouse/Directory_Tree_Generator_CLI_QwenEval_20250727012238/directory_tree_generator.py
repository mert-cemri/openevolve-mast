'''
This module contains the DirectoryTreeGenerator class which is responsible for generating
the directory tree structure as a string. It handles symbolic links to prevent infinite loops.
'''
import os
class DirectoryTreeGenerator:
    def generate_tree(self, path, max_depth):
        '''
        Generates a visual tree structure of a given directory.
        Parameters:
        path (str): The directory path to generate the tree for.
        max_depth (int): The maximum depth of the tree. If None, the tree will be generated to the full depth.
        Returns:
        str: The directory tree structure as a string.
        '''
        if not os.path.exists(path):
            raise ValueError(f"The specified path '{path}' does not exist.")
        if not os.path.isdir(path):
            raise ValueError(f"The specified path '{path}' is not a directory.")
        return self._generate_tree_helper(path, '', max_depth, 0)
    def _generate_tree_helper(self, path, prefix, max_depth, current_depth):
        '''
        Helper method to recursively generate the directory tree structure.
        Parameters:
        path (str): The current path to generate the tree for.
        prefix (str): The prefix string to format the tree structure.
        max_depth (int): The maximum depth of the tree.
        current_depth (int): The current depth of the recursion.
        Returns:
        str: The directory tree structure as a string for the current path.
        '''
        if max_depth is not None and current_depth > max_depth:
            return ''
        tree = prefix + os.path.basename(path) + '\n'
        if os.path.isdir(path) and not os.path.islink(path):
            contents = sorted(os.listdir(path))
            for i, entry in enumerate(contents):
                new_prefix = prefix + ('└── ' if i == len(contents) - 1 else '├── ')
                tree += self._generate_tree_helper(os.path.join(path, entry), new_prefix, max_depth, current_depth + 1)
        return tree