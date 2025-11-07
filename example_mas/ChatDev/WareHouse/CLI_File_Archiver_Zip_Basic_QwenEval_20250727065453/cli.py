'''
Handles command-line interactions.
'''
import argparse
from archiver import Archiver
class CLI:
    def run(self):
        parser = argparse.ArgumentParser(description='CLI File Archiver')
        subparsers = parser.add_subparsers(dest='command', help='Sub-command help')
        add_parser = subparsers.add_parser('add', help='Add files/directories to a ZIP archive')
        add_parser.add_argument('zip_path', help='Path to the ZIP archive')
        add_parser.add_argument('files', nargs='+', help='Files/directories to add')
        extract_parser = subparsers.add_parser('extract', help='Extract contents from a ZIP archive')
        extract_parser.add_argument('zip_path', help='Path to the ZIP archive')
        extract_parser.add_argument('extract_to', help='Directory to extract to')
        args = parser.parse_args()
        if args.command is None:
            parser.print_help()
            return
        archiver = Archiver()
        try:
            if args.command == 'add':
                archiver.add_to_zip(args.zip_path, args.files)
                print(f"Files added to ZIP archive '{args.zip_path}' successfully!")
            elif args.command == 'extract':
                archiver.extract_zip(args.zip_path, args.extract_to)
                print(f"Files extracted from ZIP archive '{args.zip_path}' to '{args.extract_to}' successfully!")
        except Exception as e:
            print(f"Error: {e}")