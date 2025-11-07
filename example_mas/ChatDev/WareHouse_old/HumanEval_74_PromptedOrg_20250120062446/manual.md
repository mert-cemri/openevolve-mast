manual.md

```
# Total Match Function

This software provides a simple Python function, `total_match`, which compares two lists of strings and returns the list with fewer total characters. If both lists have the same number of characters, it returns the first list.

## Main Functionality

The main function of this software is:

- **total_match(lst1, lst2):** This function accepts two lists of strings and returns the list that has a total number of characters in all strings of the list less than the other list. If the two lists have the same number of characters, it returns the first list.

### Examples

- `total_match([], [])` ➞ `[]`
- `total_match(['hi', 'admin'], ['hI', 'Hi'])` ➞ `['hI', 'Hi']`
- `total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])` ➞ `['hi', 'admin']`
- `total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])` ➞ `['hI', 'hi', 'hi']`
- `total_match(['4'], ['1', '2', '3', '4', '5'])` ➞ `['4']`

## Installation

This project does not require any external dependencies, making it straightforward to set up and use.

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Ensure you have Python installed** on your system. This function is compatible with Python 3.x.

3. **No additional installation steps are required** as there are no external dependencies.

## How to Use

1. **Open your Python environment** (such as IDLE, PyCharm, or any other Python IDE).

2. **Load the `main.py` file** into your environment.

3. **Call the `total_match` function** with the desired lists of strings as arguments.

   Example usage:
   ```python
   from main import total_match

   result = total_match(['hi', 'admin'], ['hI', 'Hi'])
   print(result)  # Output: ['hI', 'Hi']
   ```

4. **Run your script** to see the results.

## Documentation

For further details on the function and its usage, refer to the docstring provided within the `main.py` file. The docstring includes a description of the function, its parameters, and examples of its usage.

```