'''
This script provides a command-line interface (CLI) for testing regular expressions.
Users can input a regular expression and a test string as command-line arguments.
The script will indicate if the string matches the regex and optionally show matched groups.
'''
import re
import argparse
def test_regex(regex, test_string):
    '''
    Test the regular expression against the input string and print the results.
    '''
    try:
        pattern = re.compile(regex)
        match = pattern.search(test_string)
        if match:
            print("Match found!")
            print(f"Matched groups: {match.groups() if match.groups() else 'No groups'}")
        else:
            print("No match found.")
    except re.error as e:
        print(f"Invalid regular expression: {e}")
def main():
    '''
    The entry point of the CLI application.
    '''
    parser = argparse.ArgumentParser(description='Test regular expressions against a string.')
    parser.add_argument('regex', type=str, help='The regular expression to test.')
    parser.add_argument('test_string', type=str, help='The string to test against the regular expression.')
    args = parser.parse_args()
    test_regex(args.regex, args.test_string)
if __name__ == "__main__":
    main()