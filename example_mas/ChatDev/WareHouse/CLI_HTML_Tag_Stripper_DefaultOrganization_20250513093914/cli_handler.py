'''
Handles command-line interface operations for the HTML stripping application.
'''
import argparse
from html_stripper import HTMLStripper
class CLIHandler:
    def parse_arguments(self):
        '''
        Parses command-line arguments.
        :return: Parsed arguments.
        '''
        parser = argparse.ArgumentParser(description='Strip HTML tags from a file or string input.')
        parser.add_argument('-f', '--file', type=str, help='Path to the HTML file.')
        parser.add_argument('-s', '--string', type=str, help='HTML string input.')
        return parser.parse_args()
    def run(self):
        '''
        Executes the HTML stripping process based on CLI input.
        '''
        args = self.parse_arguments()
        if args.file:
            try:
                with open(args.file, 'r', encoding='utf-8') as file:
                    content = file.read()
                    print(HTMLStripper.strip_html_tags(content))
            except FileNotFoundError:
                print(f"Error: The file {args.file} was not found.")
        elif args.string:
            print(HTMLStripper.strip_html_tags(args.string))
        else:
            print("Please provide a file or string input.")