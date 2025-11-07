'''
Command-line interface for generating a Markdown table from a CSV file.
'''
import argparse
from csv_parser import CSVParser
from markdown_generator import MarkdownGenerator
class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Generate a Markdown table from a CSV file.")
        self.parser.add_argument("csv_file", type=str, help="Path to the CSV file.")
        self.parser.add_argument("md_file", type=str, help="Path to the output Markdown file.")
    def parse_arguments(self):
        return self.parser.parse_args()
    def run(self):
        args = self.parse_arguments()
        try:
            csv_parser = CSVParser()
            data = csv_parser.parse_csv(args.csv_file)
            md_generator = MarkdownGenerator()
            markdown_table = md_generator.generate_table(data)
            with open(args.md_file, 'w', encoding='utf-8') as f:
                f.write(markdown_table)
        except FileNotFoundError:
            print(f"Error: The file {args.csv_file} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")