'''
Main entry point for the Markdown to HTML converter application.
'''
import argparse
from converter import MarkdownConverter
from file_handler import FileHandler
def main():
    parser = argparse.ArgumentParser(description='Convert Markdown files to HTML.')
    parser.add_argument('input_file', help='Path to the input Markdown file')
    parser.add_argument('output_file', help='Path to the output HTML file')
    args = parser.parse_args()
    file_handler = FileHandler()
    converter = MarkdownConverter()
    try:
        markdown_content = file_handler.read_file(args.input_file)
        html_content = converter.convert(markdown_content)
        file_handler.write_file(args.output_file, html_content)
        print(f"Successfully converted {args.input_file} to {args.output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()