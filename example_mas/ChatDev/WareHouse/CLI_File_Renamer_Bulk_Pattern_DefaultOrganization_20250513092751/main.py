'''
Main entry point for the CLI file renamer application.
'''
import argparse
from file_renamer import FileRenamer
def parse_arguments():
    parser = argparse.ArgumentParser(description='CLI File Renamer')
    parser.add_argument('directory', type=str, help='The directory containing files to rename')
    parser.add_argument('--prefix', type=str, help='Prefix to add to file names', default='')
    parser.add_argument('--replace', nargs=2, metavar=('old', 'new'), help='Substring to replace in file names')
    parser.add_argument('--start-number', type=int, help='Starting number for sequential numbering', default=0)
    return parser.parse_args()
if __name__ == "__main__":
    args = parse_arguments()
    file_renamer = FileRenamer()
    if args.prefix:
        file_renamer.add_prefix(args.directory, args.prefix)
    if args.replace:
        old_substring, new_substring = args.replace
        file_renamer.replace_substring(args.directory, old_substring, new_substring)
    if args.start_number > 0:
        file_renamer.add_sequential_numbers(args.directory, args.start_number)