'''
Main entry point for the CLI regex tester application.
This script takes a regular expression and a test string as input,
and checks if the string matches the regex. It can optionally show matched groups
and allows the user to specify whether to use re.search or re.match.
'''
import sys
from regex_tester import RegexTester
def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <regex> <test_string> [show_groups] [match_type]")
        print("match_type can be 'search' (default) or 'match'")
        sys.exit(1)
    regex = sys.argv[1]
    test_string = sys.argv[2]
    show_groups = len(sys.argv) > 3 and sys.argv[3].lower() in ['true', '1', 'yes']
    match_type = sys.argv[4] if len(sys.argv) > 4 else 'search'
    regex_tester = RegexTester(regex, test_string, match_type)
    match_result, matched_groups = regex_tester.test_regex()
    if match_result:
        print("Match found!")
        if show_groups and matched_groups:
            print(f"Matched groups: {matched_groups}")
    else:
        print("No match found.")
if __name__ == "__main__":
    main()