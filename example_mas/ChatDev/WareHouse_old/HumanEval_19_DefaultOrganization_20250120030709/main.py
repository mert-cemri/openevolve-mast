'''
This module contains a function to sort numerals represented as strings.
'''
def sort_numbers(numbers: str) -> str:
    """ 
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Mapping of string numerals to their integer values
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
    # Mapping of integer values back to string numerals
    int_to_numeral = {v: k for k, v in numeral_to_int.items()}
    # Split the input string into a list of numerals
    numeral_list = numbers.split()
    # Convert the list of numerals to a list of integers
    int_list = [numeral_to_int[numeral] for numeral in numeral_list]
    # Sort the list of integers
    sorted_int_list = sorted(int_list)
    # Convert the sorted list of integers back to a list of numerals
    sorted_numeral_list = [int_to_numeral[i] for i in sorted_int_list]
    # Join the sorted list of numerals into a space-delimited string
    return ' '.join(sorted_numeral_list)