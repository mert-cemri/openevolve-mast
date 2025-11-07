'''
Main application file for the Text Case Converter CLI utility.
'''
import argparse
from text_converter import to_uppercase, to_lowercase, to_titlecase, to_sentencecase
def main():
    parser = argparse.ArgumentParser(description="Convert text to various cases.")
    parser.add_argument("text", nargs="?", help="Text to convert")
    parser.add_argument("-f", "--file", help="File to read text from")
    parser.add_argument("-o", "--output", help="File to save converted text")
    parser.add_argument("-c", "--case", choices=["uppercase", "lowercase", "titlecase", "sentencecase"], required=True, help="Case to convert text to")
    args = parser.parse_args()
    if args.file:
        try:
            with open(args.file, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Error: The file {args.file} was not found.")
            return
    elif args.text:
        text = args.text
    else:
        print("Error: No input text provided.")
        return
    if args.case == "uppercase":
        converted_text = to_uppercase(text)
    elif args.case == "lowercase":
        converted_text = to_lowercase(text)
    elif args.case == "titlecase":
        converted_text = to_titlecase(text)
    elif args.case == "sentencecase":
        converted_text = to_sentencecase(text)
    if args.output:
        try:
            with open(args.output, 'w') as file:
                file.write(converted_text)
            print(f"Converted text saved to {args.output}")
        except IOError:
            print(f"Error: Could not write to file {args.output}.")
    else:
        print(converted_text)
if __name__ == "__main__":
    main()