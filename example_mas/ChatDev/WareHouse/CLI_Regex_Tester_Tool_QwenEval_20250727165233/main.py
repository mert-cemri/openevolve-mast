'''
CLI module for the regex tester application.
Handles command-line input and output.
'''
import argparse
from regex_engine import match_regex
def main():
    # Set up the argument parser with a description
    parser = argparse.ArgumentParser(description="Regex Tester CLI Tool")
    # Add arguments for the regex and test string
    parser.add_argument("regex", help="The regular expression to test")
    parser.add_argument("test_string", help="The test string to match against the regex")
    # Add an optional argument to show matched groups
    parser.add_argument("-g", "--groups", action="store_true", help="Show matched groups if any")
    # Parse the command-line arguments
    args = parser.parse_args()
    # Call the match_regex function to perform the regex matching
    result = match_regex(args.regex, args.test_string)
    # Check if the result is an error message
    if isinstance(result, str):
        print(result)
    else:
        # Display the results with or without matched groups
        display_results(result, show_groups=args.groups)
def display_results(match, show_groups=False):
    # Check if a match was found
    if match:
        # Prepare the result text with the matched string
        result_text = f"Match found: {match.group()}"
        # If showing groups is requested and there are matched groups, add them to the result text
        if show_groups and match.groups():
            result_text += f"\nMatched groups: {match.groups()}"
    else:
        # Prepare the result text indicating no match was found
        result_text = "No match found."
    # Print the result text
    print(result_text)
if __name__ == '__main__':
    main()