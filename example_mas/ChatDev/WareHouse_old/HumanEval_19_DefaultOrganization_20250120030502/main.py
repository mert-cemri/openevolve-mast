'''
This module contains a function to sort numbers represented as strings from 'zero' to 'nine'.
'''
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Mapping from string to integer
    num_map = {
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
    # Reverse mapping from integer to string
    reverse_num_map = {v: k for k, v in num_map.items()}
    # Split the input string into a list of words
    num_list = numbers.split()
    # Convert the list of words to a list of integers
    int_list = [num_map[num] for num in num_list]
    # Sort the list of integers
    int_list.sort()
    # Convert the sorted list of integers back to a list of words
    sorted_num_list = [reverse_num_map[num] for num in int_list]
    # Join the list of words back into a single string
    return ' '.join(sorted_num_list)