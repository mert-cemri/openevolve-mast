'''
Main entry point for the file archiver application.
'''
from file_archiver import FileArchiver
from cli import CLI
def main():
    # Initialize the components
    archiver = FileArchiver()
    cli = CLI(archiver)
    # Start the CLI
    cli.run()
if __name__ == "__main__":
    main()