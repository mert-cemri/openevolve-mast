# Strange Sort List

This software provides a function to sort a list of integers in a "strange" order. The strange sorting starts with the minimum value, then the maximum of the remaining integers, then the next minimum, and so on.

## Main Functionality

The main function provided by this software is `strange_sort_list(lst)`. This function takes a list of integers as input and returns a new list sorted in the specified strange order.

### Function Definition

```python
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    result = []
    lst = sorted(lst)
    while lst:
        result.append(lst.pop(0))  # Append the smallest element
        if lst:
            result.append(lst.pop(-1))  # Append the largest element
    return result
```

## Installation

There are no external dependencies required for this software, so you can directly use the function in your Python environment.

### Quick Start

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the `main.py` file is located.

   ```bash
   cd <directory-name>
   ```

3. **Run the Function**: You can use the function directly in your Python scripts or interactive environment.

   ```python
   from main import strange_sort_list

   # Example usage
   print(strange_sort_list([1, 2, 3, 4]))  # Output: [1, 4, 2, 3]
   ```

## Usage

To use the `strange_sort_list` function, simply pass a list of integers to it. The function will return a new list sorted in the strange order described.

### Examples

```python
# Example 1
result = strange_sort_list([1, 2, 3, 4])
print(result)  # Output: [1, 4, 2, 3]

# Example 2
result = strange_sort_list([5, 5, 5, 5])
print(result)  # Output: [5, 5, 5, 5]

# Example 3
result = strange_sort_list([])
print(result)  # Output: []
```

## Documentation

For further information and documentation, please refer to the comments within the code. The function is straightforward and does not require additional libraries or dependencies.

Feel free to modify and use the function as needed for your specific use cases.