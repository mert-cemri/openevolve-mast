'''
Main file for the Text Converter utility. This file contains the main application class and CLI utility functions.
The tool reads text from a string or a file and converts it to various cases: uppercase, lowercase, title case, and sentence case.
'''
import sys
import argparse
import subprocess
import importlib.util
def install_nltk():
    '''
    Install the nltk package if it is not already installed.
    '''
    spec = importlib.util.find_spec("nltk")
    if spec is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk"])
install_nltk()
import nltk
from nltk.tokenize import sent_tokenize
def convert_to_uppercase(text):
    '''
    Convert the given text to uppercase.
    '''
    return text.upper()
def convert_to_lowercase(text):
    '''
    Convert the given text to lowercase.
    '''
    return text.lower()
def convert_to_title_case(text):
    '''
    Convert the given text to title case.
    '''
    return text.title()
def convert_to_sentence_case(text):
    '''
    Convert the given text to sentence case using nltk's sent_tokenize.
    This function splits the text into sentences and capitalizes the first letter of each sentence.
    '''
    nltk.download('punkt')  # Ensure the punkt tokenizer models are downloaded
    sentences = sent_tokenize(text)
    sentences = [sentence.capitalize() for sentence in sentences]
    return ' '.join(sentences)
def read_from_file(file_path):
    '''
    Read text from a file.
    If an error occurs, print an error message and return an empty string.
    '''
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Failed to read file: {e}")
        return ""
def main():
    '''
    Main function to parse command line arguments and perform text conversion.
    '''
    parser = argparse.ArgumentParser(description="Convert text to various cases.")
    parser.add_argument("text", nargs="?", default="", help="Text to convert")
    parser.add_argument("-f", "--file", help="File to read text from")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Convert to uppercase")
    parser.add_argument("-l", "--lowercase", action="store_true", help="Convert to lowercase")
    parser.add_argument("-t", "--titlecase", action="store_true", help="Convert to title case")
    parser.add_argument("-s", "--sentencecase", action="store_true", help="Convert to sentence case")
    args = parser.parse_args()
    if args.file:
        text = read_from_file(args.file)
    else:
        text = args.text
    if not text:
        print("No text provided. Please provide text or a file.")
        sys.exit(1)
    conversion_options = sum([args.uppercase, args.lowercase, args.titlecase, args.sentencecase])
    if conversion_options == 0:
        print("Please specify a conversion option.")
        sys.exit(1)
    elif conversion_options > 1:
        print("Please specify only one conversion option.")
        sys.exit(1)
    if args.uppercase:
        text = convert_to_uppercase(text)
    elif args.lowercase:
        text = convert_to_lowercase(text)
    elif args.titlecase:
        text = convert_to_title_case(text)
    elif args.sentencecase:
        text = convert_to_sentence_case(text)
    print(text)
if __name__ == "__main__":
    main()