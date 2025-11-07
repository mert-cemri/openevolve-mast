'''
Main file for the Git branch cleaner CLI tool. It handles command-line arguments and user interactions.
'''
import argparse
from git_manager import GitBranchManager
def list_branches(manager):
    merged_branches = manager.get_merged_branches()
    inactive_branches = manager.get_inactive_branches(merged_branches)
    for branch in inactive_branches:
        print(branch)
def delete_branch(manager, branch_name):
    manager.delete_branch(branch_name)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI tool to clean up local Git branches.")
    parser.add_argument('--list', action='store_true', help='List merged and inactive branches')
    parser.add_argument('--delete', type=str, help='Delete the specified branch')
    args = parser.parse_args()
    manager = GitBranchManager()
    if args.list:
        list_branches(manager)
    elif args.delete:
        delete_branch(manager, args.delete)
    else:
        parser.print_help()