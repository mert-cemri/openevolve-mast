'''
Regex tester module for the CLI regex tester application.
This module contains the RegexTester class which provides functionality
to test a regular expression against a test string and optionally return matched groups.
'''
import re
class RegexTester:
    def __init__(self, regex, test_string, match_type='search'):
        '''
        Initializes the RegexTester with a regex pattern, a test string, and a match type.
        :param regex: The regular expression pattern to test.
        :param test_string: The string to test against the regex pattern.
        :param match_type: The type of match to perform ('search' or 'match').
        '''
        self.regex = regex
        self.test_string = test_string
        self.match_type = match_type
    def test_regex(self):
        '''
        Tests the regex pattern against the test string.
        :return: A tuple containing a boolean indicating if a match was found,
                 and a tuple of matched groups if any.
        '''
        try:
            if self.match_type == 'match':
                match = re.match(self.regex, self.test_string)
            else:
                match = re.search(self.regex, self.test_string)
            if match:
                matched_groups = match.groups()
                return True, matched_groups
            else:
                return False, None
        except re.error as e:
            print(f"Invalid regex pattern: {e}")
            return False, None