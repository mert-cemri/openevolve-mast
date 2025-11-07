'''
Main application file for the CLI PDF Text Extractor.
'''
import argparse
from pdf_utils import extract_text_from_pdf
def main():
    parser = argparse.ArgumentParser(description='CLI PDF Text Extractor')
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file')
    parser.add_argument('--output', type=str, help='Path to save the extracted text', default=None)
    args = parser.parse_args()
    text = extract_text_from_pdf(args.pdf_path)
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text saved to {args.output}")
    else:
        print(text)
if __name__ == "__main__":
    main()