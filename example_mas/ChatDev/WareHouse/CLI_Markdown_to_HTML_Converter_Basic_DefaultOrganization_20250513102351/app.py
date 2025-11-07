'''
Main entry point for the CLI Markdown to HTML converter application.
'''
import argparse
from converter import MarkdownConverter
from file_handler import FileHandler
class MarkdownToHtmlApp:
    def __init__(self):
        self.converter = MarkdownConverter()
        self.file_handler = FileHandler()
    def convert_file(self, input_path, output_path):
        markdown_content = self.file_handler.read_markdown(input_path)
        html_content = self.converter.convert(markdown_content)
        self.file_handler.write_html(output_path, html_content)
        print(f"Conversion Complete: HTML file saved as {output_path}")
    def run(self):
        parser = argparse.ArgumentParser(description='Convert Markdown files to HTML.')
        parser.add_argument('input_file', help='Path to the input Markdown file')
        parser.add_argument('output_file', help='Path to the output HTML file')
        args = parser.parse_args()
        self.convert_file(args.input_file, args.output_file)