# Strange Sort List

This software provides a function to sort a list of integers in a "strange" order. The strange sorting starts with the minimum value, then the maximum of the remaining integers, then the next minimum, and so on.

## Main Functionality

The main function provided by this software is `strange_sort_list(lst)`. This function takes a list of integers as input and returns a new list sorted in the described strange order.

### Examples

- `strange_sort_list([1, 2, 3, 4])` returns `[1, 4, 2, 3]`
- `strange_sort_list([5, 5, 5, 5])` returns `[5, 5, 5, 5]`
- `strange_sort_list([])` returns `[]`

## Installation

This software does not require any external dependencies, so there is no need to install additional packages. You can directly use the function in your Python environment.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to the cloned repository.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can use the `strange_sort_list` function in your Python scripts. Here is an example of how to use it:

   ```python
   from main import strange_sort_list

   # Example usage
   sorted_list = strange_sort_list([1, 2, 3, 4])
   print(sorted_list)  # Output: [1, 4, 2, 3]
   ```

## Documentation

For more detailed documentation, please refer to the comments within the `main.py` file. The function is straightforward and does not require additional configuration or setup.

## Support

If you encounter any issues or have questions, please feel free to reach out through the repository's issue tracker. We are here to help you with any problems or inquiries you might have regarding the software.