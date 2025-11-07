'''
This module contains the function total_match which compares two lists of strings
and returns the list with the fewer total number of characters. If both lists have
the same number of characters, it returns the first list.
'''
def total_match(lst1, lst2):
    '''
    Compare two lists of strings and return the list with fewer total characters.
    If both lists have the same number of characters, return the first list.
    Parameters:
    lst1 (list of str): First list of strings.
    lst2 (list of str): Second list of strings.
    Returns:
    list of str: The list with fewer total characters or the first list if they are equal.
    '''
    total_chars_lst1 = sum(len(s) for s in lst1)
    total_chars_lst2 = sum(len(s) for s in lst2)
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    elif total_chars_lst1 > total_chars_lst2:
        return lst2
    else:
        return lst1