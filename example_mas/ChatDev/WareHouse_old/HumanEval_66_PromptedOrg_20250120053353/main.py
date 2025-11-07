'''
This module contains the function digitSum which calculates the sum of ASCII values of uppercase characters in a given string.
'''
def digitSum(s):
    """
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.
    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    total = 0
    for char in s:
        if char.isupper():
            total += ord(char)
    return total