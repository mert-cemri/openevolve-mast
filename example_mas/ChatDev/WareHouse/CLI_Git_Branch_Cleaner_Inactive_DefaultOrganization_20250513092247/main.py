'''
Main application file for the Git Branch Cleaner CLI tool.
'''
import argparse
from git_manager import GitBranchManager
def main():
    parser = argparse.ArgumentParser(description="CLI tool to clean up local Git branches.")
    parser.add_argument('--list', action='store_true', help="List merged and inactive branches.")
    parser.add_argument('--delete', nargs='+', help="Delete specified branches.")
    args = parser.parse_args()
    manager = GitBranchManager()
    if args.list:
        merged_branches = manager.get_merged_branches()
        inactive_branches = manager.get_inactive_branches(merged_branches, 30)
        print("Merged and inactive branches:")
        for branch in inactive_branches:
            print(branch)
    if args.delete:
        for branch in args.delete:
            manager.delete_branch(branch)
        print("Selected branches deleted.")
if __name__ == "__main__":
    main()