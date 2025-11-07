'''
This module contains the implementation of the digitSum function, which calculates the sum of ASCII values of uppercase characters in a given string.
'''
def digitSum(s):
    """
    Takes a string as input and returns the sum of the ASCII values of the uppercase characters only.
    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum(ord(char) for char in s if char.isupper())