'''
Main entry point for the CLI tool to find and kill processes by their name.
'''
from process_finder import ProcessFinder
from process_killer import ProcessKiller
from cli_interface import CLIInterface
import logging
# Setting up logging
logging.basicConfig(filename='process_tool.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def main():
    logging.info("Starting the process tool.")
    cli = CLIInterface(ProcessFinder(), ProcessKiller())
    cli.run()
    logging.info("Process tool execution completed.")
if __name__ == "__main__":
    main()