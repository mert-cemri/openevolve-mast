'''
main.py
This module contains the implementation of the strange_sort_list function,
which sorts a list of integers in a "strange" order: starting with the minimum
value, then the maximum of the remaining integers, then the next minimum, and so on.
'''
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.
    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    result = []
    while lst:
        min_val = min(lst)
        result.append(min_val)
        lst.remove(min_val)
        if lst:
            max_val = max(lst)
            result.append(max_val)
            lst.remove(max_val)
    return result