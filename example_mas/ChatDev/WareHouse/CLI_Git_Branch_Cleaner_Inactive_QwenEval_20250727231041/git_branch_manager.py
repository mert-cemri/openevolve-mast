'''
Handles the logic for interacting with Git branches.
Includes methods to list merged and inactive branches, and delete branches.
'''
import subprocess
from datetime import datetime, timedelta
class GitBranchManager:
    def __init__(self):
        self.main_branch = self._get_main_branch()
    def _get_main_branch(self):
        '''
        Determines the main branch name (either 'main' or 'master').
        '''
        try:
            result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'origin/HEAD'], capture_output=True, text=True, check=True)
            return result.stdout.strip().split('/')[-1]
        except subprocess.CalledProcessError:
            return 'master'  # Default to 'master' if the command fails
    def list_merged_branches(self):
        '''
        Lists branches that have been merged into the main branch.
        '''
        try:
            result = subprocess.run(['git', 'branch', '--merged', self.main_branch], capture_output=True, text=True, check=True)
            branches = result.stdout.strip().split('\n')
            return [branch.strip() for branch in branches if branch.strip() and not branch.startswith('*')]
        except subprocess.CalledProcessError as e:
            print(f"Error listing merged branches: {e}")
            return []
    def list_inactive_branches(self, days=30):
        '''
        Lists branches that have not been committed to for a specified number of days.
        '''
        try:
            result = subprocess.run(['git', 'for-each-ref', '--format="%(refname:short) %(committerdate:iso8601)"', 'refs/heads/'], capture_output=True, text=True, check=True)
            branches = result.stdout.strip().split('\n')
            inactive_branches = []
            for branch in branches:
                name, date_str = branch.split(' ', 1)
                commit_date = datetime.fromisoformat(date_str.strip().replace(' ', 'T'))
                if (datetime.now() - commit_date) > timedelta(days=days):
                    inactive_branches.append(name)
            return inactive_branches
        except subprocess.CalledProcessError as e:
            print(f"Error listing inactive branches: {e}")
            return []
    def delete_branch(self, branch_name):
        '''
        Deletes a specified branch.
        '''
        try:
            subprocess.run(['git', 'branch', '-D', branch_name], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error deleting branch '{branch_name}': {e}")
    def branch_exists(self, branch_name):
        '''
        Checks if a specified branch exists.
        '''
        try:
            result = subprocess.run(['git', 'branch', '--list', branch_name], capture_output=True, text=True, check=True)
            return branch_name in result.stdout.strip().split('\n')
        except subprocess.CalledProcessError as e:
            print(f"Error checking branch existence: {e}")
            return False