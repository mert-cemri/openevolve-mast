import argparse
import os
from renamer import Renamer
def main():
    parser = argparse.ArgumentParser(description='CLI file renamer')
    parser.add_argument('-p', '--pattern', required=True, help='rename pattern')
    parser.add_argument('-d', '--directory', required=True, help='directory to rename files in')
    args = parser.parse_args()
    renamer = Renamer(args.pattern, args.directory)
    renamer.rename_files()
if __name__ == '__main__':
    main()