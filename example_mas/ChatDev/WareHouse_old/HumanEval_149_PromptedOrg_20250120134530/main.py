'''
This module contains the implementation of the sorted_list_sum function,
which processes a list of strings by removing those with odd lengths and
sorting the remaining strings by length and alphabetically.
'''
def sorted_list_sum(lst):
    """Accepts a list of strings, removes strings with odd lengths,
    and returns the list sorted by length and alphabetically for strings
    of the same length.
    Args:
        lst (list): A list of strings.
    Returns:
        list: A sorted list of strings with even lengths.
    Examples:
        >>> sorted_list_sum(["aa", "a", "aaa"])
        ['aa']
        >>> sorted_list_sum(["ab", "a", "aaa", "cd"])
        ['ab', 'cd']
    """
    # Filter out strings with odd lengths
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    # Sort the list by length and alphabetically
    sorted_strings = sorted(even_length_strings, key=lambda x: (len(x), x))
    return sorted_strings