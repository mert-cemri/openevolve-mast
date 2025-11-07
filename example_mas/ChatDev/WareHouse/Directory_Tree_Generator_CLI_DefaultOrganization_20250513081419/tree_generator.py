'''
Contains the TreeGenerator class which generates a visual tree structure of a directory.
'''
import os
class TreeGenerator:
    def generate_tree(self, directory, max_depth):
        '''
        Generates a tree structure of the given directory up to the specified depth.
        :param directory: The root directory to generate the tree from.
        :param max_depth: The maximum depth to traverse.
        :return: A string representing the directory tree.
        '''
        tree = []
        self._generate_tree_recursive(directory, 0, max_depth, tree)
        return "\n".join(tree)
    def _generate_tree_recursive(self, directory, current_depth, max_depth, tree):
        if current_depth > max_depth:
            return
        try:
            entries = os.listdir(directory)
        except PermissionError:
            tree.append("    " * current_depth + "|-- [Permission Denied]")
            return
        for entry in entries:
            path = os.path.join(directory, entry)
            tree.append("    " * current_depth + "|-- " + entry)
            if os.path.isdir(path):
                self._generate_tree_recursive(path, current_depth + 1, max_depth, tree)