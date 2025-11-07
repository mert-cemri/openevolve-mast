'''
Entry point of the application. Handles command-line arguments and strips HTML tags.
'''
import argparse
from html_processor import strip_html_tags
def parse_arguments():
    '''
    Parses command-line arguments for the HTML stripping tool.
    '''
    parser = argparse.ArgumentParser(description='CLI tool to strip HTML tags from an HTML file or string input.')
    parser.add_argument('-f', '--file', type=str, help='Path to the HTML file')
    parser.add_argument('-s', '--string', type=str, help='HTML string input')
    return parser.parse_args()
def main():
    '''
    Main function to handle CLI input.
    '''
    args = parse_arguments()
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as file:
                html_content = file.read()
        except FileNotFoundError:
            print(f"Error: The file {args.file} does not exist.")
            return
        except Exception as e:
            print(f"Error reading the file: {e}")
            return
    elif args.string:
        html_content = args.string
    else:
        print("Error: Please provide either a file or a string input.")
        return
    plain_text = strip_html_tags(html_content)
    print(plain_text)
if __name__ == '__main__':
    main()