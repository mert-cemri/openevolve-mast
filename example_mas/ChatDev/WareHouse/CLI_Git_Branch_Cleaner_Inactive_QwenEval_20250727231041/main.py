'''
Main entry point for the Git Branch Cleanup Tool.
Handles initialization of the GUI or CLI based on user input.
'''
import sys
from gui import GitBranchGUI
from cli import GitBranchCLI
def main():
    if '--cli' in sys.argv:
        cli = GitBranchCLI()
        cli.list_branches()
        branches_to_delete = input("Enter branch names to delete (comma-separated, or press Enter to skip): ").strip()
        if branches_to_delete:
            branches_to_delete = [branch.strip() for branch in branches_to_delete.split(',')]
            valid_branches = cli.manager.list_merged_branches() + cli.manager.list_inactive_branches()
            invalid_branches = [branch for branch in branches_to_delete if branch not in valid_branches]
            if invalid_branches:
                print(f"Invalid branch names: {', '.join(invalid_branches)}")
                return  # Exit early if there are invalid branches
            for branch in branches_to_delete:
                if branch in valid_branches:
                    cli.delete_branch(branch)
    else:
        gui = GitBranchGUI()
        gui.run()
if __name__ == "__main__":
    main()