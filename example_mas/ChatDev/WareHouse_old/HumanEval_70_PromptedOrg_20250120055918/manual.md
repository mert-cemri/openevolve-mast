manual.md

```
# Strange Sort List

This software provides a function to sort a list of integers in a "strange" order. The strange sorting starts with the minimum value, then the maximum of the remaining integers, then the next minimum, and so on.

## Main Function

### strange_sort_list(lst)

- **Description**: This function takes a list of integers and returns a new list sorted in a strange order.
- **Parameters**: 
  - `lst` (list): A list of integers to be sorted.
- **Returns**: 
  - A list of integers sorted in the strange order.

### Examples

- `strange_sort_list([1, 2, 3, 4])` returns `[1, 4, 2, 3]`
- `strange_sort_list([5, 5, 5, 5])` returns `[5, 5, 5, 5]`
- `strange_sort_list([])` returns `[]`

## Installation

This software does not require any external dependencies. You only need Python installed on your system to run the function.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the `main.py` file to your local machine.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python interpreter and import the function:

   ```bash
   python
   ```

   ```python
   from main import strange_sort_list
   ```

4. Use the function by passing a list of integers:

   ```python
   result = strange_sort_list([1, 2, 3, 4])
   print(result)  # Output: [1, 4, 2, 3]
   ```

5. Exit the Python interpreter by typing `exit()`.

## Documentation

For further details on how the function works, refer to the docstring provided in the `main.py` file. The docstring includes a description of the function, its parameters, and examples of usage.

```