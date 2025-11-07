# Strange Sort List

This software provides a function to sort a list of integers in a "strange" order. The strange sorting method starts with the minimum value, then the maximum of the remaining integers, then the next minimum, and so on.

## Main Functionality

The main function provided by this software is `strange_sort_list(lst)`, which takes a list of integers as input and returns a new list sorted in the strange order.

### Examples

- `strange_sort_list([1, 2, 3, 4])` returns `[1, 4, 2, 3]`
- `strange_sort_list([5, 5, 5, 5])` returns `[5, 5, 5, 5]`
- `strange_sort_list([])` returns `[]`

## Installation

This software does not require any external dependencies. It is implemented in pure Python, so you only need to have Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

## Usage

To use the `strange_sort_list` function, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python interpreter and import the function:

   ```bash
   python
   ```

   ```python
   from main import strange_sort_list
   ```

4. Call the function with a list of integers:

   ```python
   result = strange_sort_list([1, 2, 3, 4])
   print(result)  # Output: [1, 4, 2, 3]
   ```

5. You can test the function with different lists to see the strange sorting in action.

## Documentation

The function is straightforward and does not require additional configuration. For any questions or further assistance, please refer to the comments within the `main.py` file, which provide a brief explanation of the function's logic.