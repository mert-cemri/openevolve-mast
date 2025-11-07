# Common Elements Finder

This software provides a simple utility function to find and return sorted unique common elements from two lists. It is designed to be efficient and easy to use, with no external dependencies required.

## Main Function

The main function of this software is `common(l1: list, l2: list)`, which takes two lists as input and returns a sorted list of unique elements that are common to both lists.

### Function Definition

```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    # Convert lists to sets to find common elements
    set1 = set(l1)
    set2 = set(l2)
    # Find intersection of both sets
    common_elements = set1.intersection(set2)
    # Convert to a sorted list
    return sorted(common_elements)
```

## Quick Install

Since there are no external dependencies required for this software, you can directly use the function in your Python environment without any additional installations.

## How to Use

1. **Copy the Function**: Copy the `common` function from the code snippet provided above into your Python script or interactive environment.

2. **Call the Function**: Use the function by passing two lists as arguments. For example:

    ```python
    result = common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    print(result)  # Output: [1, 5, 653]
    ```

3. **Interpret the Results**: The function will return a list of sorted unique elements that are present in both input lists.

## Example Usage

```python
# Example 1
list1 = [1, 4, 3, 34, 653, 2, 5]
list2 = [5, 7, 1, 5, 9, 653, 121]
print(common(list1, list2))  # Output: [1, 5, 653]

# Example 2
list1 = [5, 3, 2, 8]
list2 = [3, 2]
print(common(list1, list2))  # Output: [2, 3]
```

## Conclusion

This utility function is a straightforward solution for finding common elements between two lists. It leverages Python's set operations to efficiently determine the intersection and returns the result as a sorted list. Enjoy using this simple yet powerful tool in your projects!