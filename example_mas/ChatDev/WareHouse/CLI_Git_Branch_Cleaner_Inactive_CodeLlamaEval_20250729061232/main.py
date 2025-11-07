import argparse
import os
import sys
from branch_cleaner import BranchCleaner
def main():
    """
    Main function to clean up local Git branches
    """
    parser = argparse.ArgumentParser(description='Clean up local Git branches')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete branches that have been merged into the main/master branch and are inactive (old commit date)')
    args = parser.parse_args()
    cleaner = BranchCleaner()
    cleaner.clean_branches(args.delete)
if __name__ == '__main__':
    main()