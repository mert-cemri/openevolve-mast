'''
Main entry point for the stock price checker CLI application.
'''
from cli import CLI
def main():
    cli_app = CLI()
    cli_app.run()
if __name__ == "__main__":
    main()