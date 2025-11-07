'''
Given list of integers, return list in strange order.
Strange sorting, is when you start with the minimum value,
then maximum of the remaining integers, then minimum and so on.
Examples:
strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
strange_sort_list([]) == []
'''
def strange_sort_list(lst):
    result = []
    lst.sort()
    while lst:
        result.append(lst.pop(0))  # Append the smallest element
        if lst:
            result.append(lst.pop(-1))  # Append the largest element
    return result