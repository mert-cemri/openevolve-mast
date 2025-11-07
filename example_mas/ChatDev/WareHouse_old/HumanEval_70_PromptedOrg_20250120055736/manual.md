# Strange Sort List

This software provides a function to sort a list of integers in a "strange" order. The strange sorting method starts with the minimum value, then the maximum of the remaining integers, then the next minimum, and so on.

## Main Functionality

The main function provided by this software is `strange_sort_list(lst)`. It takes a list of integers as input and returns a new list sorted in the strange order described above.

### Examples

- `strange_sort_list([1, 2, 3, 4])` returns `[1, 4, 2, 3]`
- `strange_sort_list([5, 5, 5, 5])` returns `[5, 5, 5, 5]`
- `strange_sort_list([])` returns `[]`

## Installation

### Environment Setup

This software does not require any external dependencies, so you can run it in any Python environment. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Running the Code

1. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where `main.py` is located.

3. **Run the Code**: You can run the code by executing the `main.py` file in a Python environment. Use the following command:

   ```bash
   python main.py
   ```

## How to Use

To use the `strange_sort_list` function, follow these steps:

1. **Import the Function**: Ensure that the `strange_sort_list` function is accessible in your Python environment. You can do this by importing it from the `main.py` file.

   ```python
   from main import strange_sort_list
   ```

2. **Call the Function**: Pass a list of integers to the `strange_sort_list` function and store the result.

   ```python
   sorted_list = strange_sort_list([1, 2, 3, 4])
   print(sorted_list)  # Output: [1, 4, 2, 3]
   ```

## Documentation

For further details on the implementation and usage of the `strange_sort_list` function, refer to the comments and examples provided within the `main.py` file. The code is straightforward and self-explanatory, designed to meet the specific task requirements efficiently.