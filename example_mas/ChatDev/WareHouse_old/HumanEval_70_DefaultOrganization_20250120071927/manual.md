# Strange Sort List

This software provides a function to sort a list of integers in a "strange" order. The strange sorting starts with the minimum value, then the maximum of the remaining integers, then the next minimum, and so on.

## Main Functionality

The main function provided by this software is `strange_sort_list(lst)`. This function takes a list of integers as input and returns a new list sorted in the specified "strange" order.

### Examples

- `strange_sort_list([1, 2, 3, 4])` returns `[1, 4, 2, 3]`
- `strange_sort_list([5, 5, 5, 5])` returns `[5, 5, 5, 5]`
- `strange_sort_list([])` returns `[]`

## Installation

This software does not have any external dependencies, so there is no need to install additional packages. You can directly use the provided `main.py` file in your Python environment.

## Usage

1. **Clone or Download the Repository:**

   Clone the repository to your local machine or download the `main.py` file.

2. **Run the Code:**

   You can run the code by executing the `main.py` file in a Python environment. Make sure you have Python installed on your machine.

   ```bash
   python main.py
   ```

3. **Use the Function:**

   You can use the `strange_sort_list` function in your own Python scripts by importing it from `main.py`.

   ```python
   from main import strange_sort_list

   result = strange_sort_list([1, 2, 3, 4])
   print(result)  # Output: [1, 4, 2, 3]
   ```

## Documentation

The function is straightforward and does not require additional configuration. For any questions or further assistance, please refer to the comments within the code or contact the support team.

## Support

For any issues or questions, please contact our support team. We are here to help you with any problems you might encounter while using the software.