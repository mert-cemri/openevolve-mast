'''
Given a string, find out how many distinct characters (regardless of case) does it consist of
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
'''
def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ensure case insensitivity
    lowercased_string = string.lower()
    # Use a set to store distinct characters
    distinct_characters = set(lowercased_string)
    # Return the number of distinct characters
    return len(distinct_characters)