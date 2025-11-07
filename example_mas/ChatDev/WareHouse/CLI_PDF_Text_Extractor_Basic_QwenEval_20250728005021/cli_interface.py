'''
Handles the command line interface for the PDF text extractor tool.
'''
import sys
import argparse
from pdf_extractor import PDFExtractor
from utils import validate_pdf_path, validate_output_path
class CLIInterface:
    def __init__(self, args):
        self.parser = argparse.ArgumentParser(description="PDF Text Extractor")
        self.parser.add_argument("pdf_path", help="Path to the PDF file")
        self.parser.add_argument("-o", "--output", help="Path to the output text file")
        self.args = self.parser.parse_args(args)
    def run(self):
        pdf_path = self.args.pdf_path
        output_path = self.args.output
        if not validate_pdf_path(pdf_path):
            print(f"Error: Invalid PDF file path '{pdf_path}'")
            sys.exit(1)
        if output_path and not validate_output_path(output_path):
            print(f"Error: Invalid output file path '{output_path}'")
            sys.exit(1)
        pdf_extractor = PDFExtractor()
        try:
            text = pdf_extractor.extract_text(pdf_path)
            if output_path:
                pdf_extractor.save_text_to_file(text, output_path)
                print(f"Text extracted and saved to '{output_path}'")
            else:
                print(text)
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)