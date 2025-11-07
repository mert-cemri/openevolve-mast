'''
This module contains a function to convert an integer to its Roman numeral representation in lowercase.
'''
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000
    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # Define the Roman numeral mappings
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    # Initialize the result as an empty string
    result = ''
    # Iterate over the Roman numeral mappings
    for value, numeral in roman_numerals:
        # While the number is greater than or equal to the value
        while number >= value:
            # Append the numeral to the result
            result += numeral
            # Subtract the value from the number
            number -= value
    # Return the result in lowercase
    return result.lower()