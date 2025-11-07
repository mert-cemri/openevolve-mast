'''
Task:
Write a function that takes a string as input and returns the sum of the upper characters only'
ASCII codes.
Examples:
    digitSum("") => 0
    digitSum("abAB") => 131
    digitSum("abcCd") => 67
    digitSum("helloE") => 69
    digitSum("woArBld") => 131
    digitSum("aAaaaXa") => 153
'''
def digitSum(s):
    """
    Calculate the sum of ASCII values of uppercase characters in the input string.
    :param s: Input string
    :return: Sum of ASCII values of uppercase characters
    """
    return sum(ord(char) for char in s if char.isupper())