'''
This module contains the function next_smallest which returns the second smallest
element in a list of integers or None if there is no such element.
'''
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # Convert list to a set to remove duplicates
    unique_elements = set(lst)
    # If there are fewer than 2 unique elements, return None
    if len(unique_elements) < 2:
        return None
    # Sort the unique elements
    sorted_elements = sorted(unique_elements)
    # Return the second smallest element
    return sorted_elements[1]
# Example usage
if __name__ == "__main__":
    print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
    print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
    print(next_smallest([]))               # Output: None
    print(next_smallest([1, 1]))           # Output: None