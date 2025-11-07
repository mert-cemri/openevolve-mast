'''
This module contains a function to sort numerals from 'zero' to 'nine' in ascending order.
'''
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
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
    # Mapping of integers back to their corresponding numeral words
    int_to_numeral = {v: k for k, v in numeral_to_int.items()}
    # Split the input string into a list of numeral words
    numeral_list = numbers.split()
    # Convert numeral words to integers, sort them, and convert back to numeral words
    sorted_numerals = sorted(numeral_list, key=lambda x: numeral_to_int[x])
    # Join the sorted numeral words into a single string
    return ' '.join(sorted_numerals)