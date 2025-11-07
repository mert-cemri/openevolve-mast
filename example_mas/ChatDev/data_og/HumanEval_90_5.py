'''
You are given a list of integers.
Write a function next_smallest() that returns the 2nd smallest element of the list.
Return None if there is no such element.
next_smallest([1, 2, 3, 4, 5]) == 2
next_smallest([5, 1, 4, 3, 2]) == 2
next_smallest([]) == None
next_smallest([1, 1]) == None
'''
def next_smallest(lst):
    # Convert list to a set to remove duplicates
    unique_elements = set(lst)
    # If there are less than 2 unique elements, return None
    if len(unique_elements) < 2:
        return None
    # Convert the set back to a sorted list
    sorted_elements = sorted(unique_elements)
    # Return the second smallest element
    return sorted_elements[1]