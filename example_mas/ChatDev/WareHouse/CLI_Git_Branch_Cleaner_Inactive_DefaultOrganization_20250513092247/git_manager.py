'''
Handles Git operations for the Git Branch Cleaner CLI tool.
'''
import subprocess
from datetime import datetime, timedelta
import shlex
class GitBranchManager:
    def get_merged_branches(self):
        result = subprocess.run(['git', 'branch', '--merged'], capture_output=True, text=True)
        branches = result.stdout.splitlines()
        return [branch.strip() for branch in branches if branch.strip() and branch.strip() not in ['main', 'master']]
    def get_inactive_branches(self, branches, days):
        inactive_branches = []
        cutoff_date = datetime.now() - timedelta(days=days)
        for branch in branches:
            result = subprocess.run(['git', 'log', '-1', '--format=%ci', branch], capture_output=True, text=True)
            commit_date_str = result.stdout.strip()
            commit_date = datetime.strptime(commit_date_str, '%Y-%m-%d %H:%M:%S %z')
            if commit_date < cutoff_date:
                inactive_branches.append(branch)
        return inactive_branches
    def delete_branch(self, branch):
        subprocess.run(['git', 'branch', '-D', branch])