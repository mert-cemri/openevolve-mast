'''
Given a string, find out how many distinct characters (regardless of case) it consists of.
'''
def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ignore case
    lower_string = string.lower()
    # Use a set to store distinct characters
    distinct_characters = set(lower_string)
    # Return the number of distinct characters
    return len(distinct_characters)