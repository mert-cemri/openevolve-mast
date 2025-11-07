'''
Main application file for the text case converter CLI utility.
'''
import argparse
from text_converter import to_uppercase, to_lowercase, to_title_case, to_sentence_case
from file_handler import read_file
def convert_text(input_text, conversion_function):
    return conversion_function(input_text)
def main():
    parser = argparse.ArgumentParser(description='Convert text to various cases.')
    parser.add_argument('input', help='Input text or file path')
    parser.add_argument('--uppercase', action='store_true', help='Convert text to uppercase')
    parser.add_argument('--lowercase', action='store_true', help='Convert text to lowercase')
    parser.add_argument('--titlecase', action='store_true', help='Convert text to title case')
    parser.add_argument('--sentencecase', action='store_true', help='Convert text to sentence case')
    parser.add_argument('--file', action='store_true', help='Indicate that input is a file path')
    args = parser.parse_args()
    if args.file:
        input_text = read_file(args.input)
    else:
        input_text = args.input
    if args.uppercase:
        print(convert_text(input_text, to_uppercase))
    elif args.lowercase:
        print(convert_text(input_text, to_lowercase))
    elif args.titlecase:
        print(convert_text(input_text, to_title_case))
    elif args.sentencecase:
        print(convert_text(input_text, to_sentence_case))
    else:
        print("No conversion option selected. Please choose one of --uppercase, --lowercase, --titlecase, or --sentencecase.")
if __name__ == "__main__":
    main()