'''
This module provides a function to sort numerals from 'zero' to 'nine' in ascending order.
'''
def sort_numbers(numbers: str) -> str:
    """ 
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Mapping of numerals to their corresponding integer values
    numeral_to_int = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    # Split the input string into a list of numerals
    numeral_list = numbers.split()
    # Sort the list of numerals based on their integer values
    sorted_numerals = sorted(numeral_list, key=lambda x: numeral_to_int[x])
    # Join the sorted numerals into a space-delimited string
    return ' '.join(sorted_numerals)