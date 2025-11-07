'''
DOCSTRING
This function takes a list of integers and returns the second smallest distinct element.
If the list has fewer than two distinct elements, it returns None.
'''
def next_smallest(lst):
    if len(lst) < 2:
        return None
    # Convert list to a set to remove duplicates and sort it
    unique_sorted_lst = sorted(set(lst))
    # Check if there are at least two distinct elements
    if len(unique_sorted_lst) < 2:
        return None
    # Return the second smallest element
    return unique_sorted_lst[1]
# Example usage:
# print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
# print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
# print(next_smallest([]))              # Output: None
# print(next_smallest([1, 1]))          # Output: None