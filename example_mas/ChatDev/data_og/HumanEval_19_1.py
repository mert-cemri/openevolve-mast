'''
This module contains the function `sort_numbers` which sorts a space-delimited string of numeral words from 'zero' to 'nine'.
'''
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Mapping of numeral words to their corresponding integer values
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
    # Mapping of integer values back to numeral words
    int_to_numeral = {v: k for k, v in numeral_to_int.items()}
    # Split the input string into a list of numeral words
    numeral_words = numbers.split()
    # Convert numeral words to integers
    int_values = [numeral_to_int[word] for word in numeral_words]
    # Sort the integer values
    sorted_int_values = sorted(int_values)
    # Convert sorted integers back to numeral words
    sorted_numeral_words = [int_to_numeral[value] for value in sorted_int_values]
    # Join the sorted numeral words into a space-delimited string
    return ' '.join(sorted_numeral_words)