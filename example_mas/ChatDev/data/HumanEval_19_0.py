'''
This module contains the function `sort_numbers` which sorts a space-delimited string of numerals from 'zero' to 'nine'.
'''
def sort_numbers(numbers: str) -> str:
    """ 
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    numeral_to_number = {
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
    number_to_numeral = {v: k for k, v in numeral_to_number.items()}
    # Split the input string into a list of numerals
    numeral_list = numbers.split()
    # Convert numerals to numbers
    number_list = [numeral_to_number[numeral] for numeral in numeral_list]
    # Sort the numbers
    sorted_numbers = sorted(number_list)
    # Convert numbers back to numerals
    sorted_numerals = [number_to_numeral[number] for number in sorted_numbers]
    # Join the sorted numerals into a single string
    return ' '.join(sorted_numerals)