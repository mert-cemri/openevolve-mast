'''
Main file for the CLI PDF Text Extractor application.
'''
import argparse
from pdf_utils import extract_text_from_pdf, save_text_to_file
def main():
    parser = argparse.ArgumentParser(description="CLI PDF Text Extractor")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("-o", "--output", help="Path to save the extracted text to a file")
    args = parser.parse_args()
    # Extract text from the PDF
    text = extract_text_from_pdf(args.pdf_path)
    # Print to standard output
    print(text)
    # Save to file if output path is provided
    if args.output:
        save_text_to_file(text, args.output)
        print(f"Text saved to {args.output}")
if __name__ == "__main__":
    main()