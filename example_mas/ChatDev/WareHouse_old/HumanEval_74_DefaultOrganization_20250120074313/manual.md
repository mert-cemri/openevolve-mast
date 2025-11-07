# Total Match Function

This software provides a function `total_match` that compares two lists of strings and returns the list with the fewer total number of characters. If both lists have the same number of characters, it returns the first list.

## Main Functionality

The main functionality of this software is to determine which of the two provided lists of strings has fewer total characters. This can be useful in scenarios where you need to compare datasets or prioritize shorter text content.

### Function Definition

```python
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
```

## Installation

There are no external dependencies required for this software. It is implemented purely in Python and can be run in any standard Python environment.

### Quick Start

1. **Ensure you have Python installed**: This software requires Python to run. You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `total_match` function.

3. **Run the function**: You can use the function by importing it into your Python script or by running it directly in a Python environment.

## Usage

To use the `total_match` function, simply call it with two lists of strings as arguments. Here are some examples:

```python
# Example 1
result = total_match([], [])
print(result)  # Output: []

# Example 2
result = total_match(['hi', 'admin'], ['hI', 'Hi'])
print(result)  # Output: ['hI', 'Hi']

# Example 3
result = total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
print(result)  # Output: ['hi', 'admin']

# Example 4
result = total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])
print(result)  # Output: ['hI', 'hi', 'hi']

# Example 5
result = total_match(['4'], ['1', '2', '3', '4', '5'])
print(result)  # Output: ['4']
```

## Conclusion

This software provides a simple yet effective way to compare two lists of strings based on their total character count. It is easy to integrate into existing Python projects and requires no additional dependencies.