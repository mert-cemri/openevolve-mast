'''
Main entry point for the CLI File Archiver application.
'''
import argparse
from file_archiver import FileArchiver
def main():
    parser = argparse.ArgumentParser(description='CLI File Archiver')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    # Create ZIP command
    create_parser = subparsers.add_parser('create', help='Create a ZIP archive')
    create_parser.add_argument('archive_name', help='Name of the archive to create')
    create_parser.add_argument('files', nargs='+', help='Files or directories to include in the archive')
    # Extract ZIP command
    extract_parser = subparsers.add_parser('extract', help='Extract a ZIP archive')
    extract_parser.add_argument('archive_name', help='Name of the archive to extract')
    extract_parser.add_argument('extract_to', help='Directory to extract files to')
    args = parser.parse_args()
    archiver = FileArchiver()
    if args.command == 'create':
        archiver.create_zip(args.archive_name, args.files)
        print(f"Archive created: {args.archive_name}")
    elif args.command == 'extract':
        archiver.extract_zip(args.archive_name, args.extract_to)
        print(f"Archive extracted to: {args.extract_to}")
if __name__ == "__main__":
    main()