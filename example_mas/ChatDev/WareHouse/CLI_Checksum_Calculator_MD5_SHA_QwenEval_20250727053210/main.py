'''
Main entry point for the Checksum Utility CLI application.
This script calculates and displays the MD5 and SHA256 checksums of a given file.
'''
import sys
from checksum_cli import ChecksumCLI
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)
    # Run CLI version
    cli = ChecksumCLI()
    cli.run(sys.argv[1])
if __name__ == "__main__":
    main()