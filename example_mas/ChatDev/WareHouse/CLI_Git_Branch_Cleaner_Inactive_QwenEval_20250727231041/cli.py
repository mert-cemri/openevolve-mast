'''
Handles the command-line interface for the Git Branch Cleanup Tool.
'''
from git_branch_manager import GitBranchManager
class GitBranchCLI:
    def __init__(self):
        self.manager = GitBranchManager()
    def list_branches(self):
        '''
        Lists branches that can be deleted.
        '''
        branches = self.manager.list_merged_branches() + self.manager.list_inactive_branches()
        print("Branches that can be deleted:")
        for branch in branches:
            print(f" - {branch}")
    def delete_branch(self, branch_name):
        '''
        Deletes a specified branch.
        '''
        if not self.manager.branch_exists(branch_name):
            print(f"Branch '{branch_name}' does not exist.")
            return
        try:
            self.manager.delete_branch(branch_name)
            print(f"Branch '{branch_name}' has been deleted.")
        except subprocess.CalledProcessError as e:
            print(f"Error deleting branch '{branch_name}': {e}")