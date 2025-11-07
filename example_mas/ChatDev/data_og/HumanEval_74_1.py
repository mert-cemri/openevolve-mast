'''
This module contains a function `total_match` that compares two lists of strings
and returns the list with the fewer total number of characters. If both lists
have the same number of characters, it returns the first list.
'''
def total_match(lst1, lst2):
    '''
    Accepts two lists of strings and returns the list that has the total number
    of characters in all strings of the list less than the other list.
    If the two lists have the same number of characters, returns the first list.
    Parameters:
    lst1 (list): First list of strings.
    lst2 (list): Second list of strings.
    Returns:
    list: The list with the fewer total number of characters, or the first list
          if both have the same number of characters.
    Examples:
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    # Calculate the total number of characters in each list
    total_chars_lst1 = sum(len(s) for s in lst1)
    total_chars_lst2 = sum(len(s) for s in lst2)
    # Compare the total number of characters and return the appropriate list
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    elif total_chars_lst2 < total_chars_lst1:
        return lst2
    else:
        return lst1