'''
Git manager file that handles operations related to Git branches, such as listing and deleting branches.
'''
import subprocess
from datetime import datetime, timedelta
class GitBranchManager:
    def get_merged_branches(self):
        result = subprocess.run(['git', 'branch', '--merged'], capture_output=True, text=True)
        branches = result.stdout.splitlines()
        return [branch.strip() for branch in branches if branch.strip() and branch.strip() != 'main' and branch.strip() != 'master']
    def get_inactive_branches(self, merged_branches):
        inactive_branches = []
        for branch in merged_branches:
            result = subprocess.run(['git', 'log', '-1', '--format=%ci', branch], capture_output=True, text=True)
            commit_date = result.stdout.strip()
            # Assuming branches inactive for more than 30 days are considered old
            if self.is_old_commit(commit_date):
                inactive_branches.append(branch)
        return inactive_branches
    def is_old_commit(self, commit_date):
        commit_datetime = datetime.strptime(commit_date, '%Y-%m-%d %H:%M:%S %z')
        return (datetime.now(commit_datetime.tzinfo) - commit_datetime) > timedelta(days=30)
    def delete_branch(self, branch_name):
        # Warning the user about force deletion
        confirmation = input(f"Are you sure you want to forcefully delete the branch '{branch_name}'? This action cannot be undone. (yes/no): ")
        if confirmation.lower() == 'yes':
            subprocess.run(['git', 'branch', '-D', branch_name])
            print(f"Branch '{branch_name}' has been deleted.")
        else:
            print("Branch deletion aborted.")