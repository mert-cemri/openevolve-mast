import os
import subprocess
class BranchCleaner:
    """
    Class to clean up local Git branches
    """
    def __init__(self):
        self.branches = self.get_branches()
    def get_branches(self):
        """
        Get all branches in the local Git repository
        """
        branches = []
        for line in subprocess.check_output(['git', 'branch']).decode().splitlines():
            if line.startswith('*'):
                continue
            branches.append(line.strip())
        return branches
    def clean_branches(self, delete):
        """
        Clean up local Git branches
        """
        for branch in self.branches:
            if delete:
                self.delete_branch(branch)
            else:
                self.print_branch(branch)
    def delete_branch(self, branch):
        """
        Delete a branch in the local Git repository
        """
        subprocess.check_call(['git', 'branch', '-d', branch])
    def print_branch(self, branch):
        """
        Print a branch in the local Git repository
        """
        print(branch)