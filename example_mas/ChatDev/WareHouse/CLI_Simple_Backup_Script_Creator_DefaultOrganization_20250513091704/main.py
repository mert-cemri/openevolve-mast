'''
Main file to run the Backup Script Creator application as a CLI tool.
'''
import argparse
from script_generator import create_rsync_script, create_tar_script
def main():
    parser = argparse.ArgumentParser(description="Backup Script Creator")
    parser.add_argument('-s', '--sources', nargs='+', required=True, help='List of source directories to backup')
    parser.add_argument('-t', '--target', required=True, help='Target directory for backup')
    parser.add_argument('-m', '--method', choices=['rsync', 'tar'], required=True, help='Method to use for backup script')
    parser.add_argument('-o', '--output', required=True, help='Output file for the generated script')
    args = parser.parse_args()
    if args.method == 'rsync':
        script_content = create_rsync_script(args.sources, args.target)
    elif args.method == 'tar':
        script_content = create_tar_script(args.sources, args.target)
    with open(args.output, 'w') as script_file:
        script_file.write(script_content)
    print(f"Script saved to {args.output}")
if __name__ == "__main__":
    main()