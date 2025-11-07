'''
This module contains a function `total_match` that compares two lists of strings and returns the list with fewer total characters. If both lists have the same number of characters, it returns the first list.
'''
def total_match(lst1, lst2):
    '''
    Accepts two lists of strings and returns the list that has 
    total number of chars in all strings of the list less than the other list.
    If the two lists have the same number of chars, return the first list.
    Parameters:
    lst1 (list of str): The first list of strings.
    lst2 (list of str): The second list of strings.
    Returns:
    list of str: The list with fewer total characters, or the first list if they are equal.
    '''
    # Calculate the total number of characters in each list
    total_chars_lst1 = sum(len(s) for s in lst1)
    total_chars_lst2 = sum(len(s) for s in lst2)
    # Compare the total number of characters and return the appropriate list
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    else:
        return lst2