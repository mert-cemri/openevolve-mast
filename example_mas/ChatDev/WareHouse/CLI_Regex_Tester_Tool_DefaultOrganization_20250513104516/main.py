'''
FILENAME: main.py
'''
import re
def main():
    '''
    DOCSTRING: Main function to execute the CLI regex tester.
    '''
    regex = input("Enter the regular expression: ")
    test_string = input("Enter the test string: ")
    try:
        pattern = re.compile(regex)
        match = pattern.search(test_string)  # Changed from match() to search()
        if match:
            result_text = "Match found!"
            groups = match.groups()
            if groups:
                result_text += f" Matched groups: {groups}"
            else:
                result_text += " No groups captured."
        else:
            result_text = "No match found."
        print(result_text)
    except re.error as e:
        print(f"Error in regular expression: {e}")
if __name__ == "__main__":
    '''
    DOCSTRING: Entry point of the CLI application.
    '''
    main()