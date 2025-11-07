'''
Main entry point for the HTML stripping application.
'''
from cli import CLI
def main():
    # Initialize and run the CLI
    cli = CLI()
    cli.run()
if __name__ == "__main__":
    main()