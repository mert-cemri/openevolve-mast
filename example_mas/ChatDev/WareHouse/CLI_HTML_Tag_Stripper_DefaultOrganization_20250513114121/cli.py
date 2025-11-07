'''
Handles command-line interface operations for the HTML stripping application.
'''
import argparse
from html_stripper import HTMLStripper
class CLI:
    def run(self):
        '''
        Parse command-line arguments and execute HTML stripping.
        '''
        parser = argparse.ArgumentParser(description='Strip HTML tags from a file or string input.')
        parser.add_argument('input', help='HTML file path or string input')
        parser.add_argument('--file', action='store_true', help='Indicate if the input is a file path')
        args = parser.parse_args()
        if args.file:
            with open(args.input, 'r', encoding='utf-8') as file:
                html_content = file.read()
        else:
            html_content = args.input
        stripped_content = HTMLStripper.strip_tags(html_content)
        print(stripped_content)