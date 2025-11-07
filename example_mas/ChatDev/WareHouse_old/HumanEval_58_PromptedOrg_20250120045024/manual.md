# Common Elements Finder

This software provides a simple utility function to find and return the sorted unique common elements from two lists. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Function

The main function of this software is:

- `common(l1: list, l2: list)`: This function takes two lists as input and returns a sorted list of unique common elements found in both lists.

### Example Usage

```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

## Installation

### Environment Setup

Since this software does not require any external dependencies, setting up the environment is straightforward. You only need to have Python installed on your system.

### Installing Python

If you do not have Python installed, you can download and install it from the official website: [Python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your working directory to where the `main.py` file is located.

   ```bash
   cd path/to/repository
   ```

3. **Run the Function**: You can run the function directly in a Python environment (such as Python shell, Jupyter Notebook, or any Python IDE).

   ```python
   from main import common

   result = common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
   print(result)  # Output: [1, 5, 653]
   ```

## Documentation

This software is designed to be simple and intuitive. The main function `common` is documented with examples in the docstring. For further information or questions, please refer to the comments within the code or contact the development team.

## Support

For any issues or support, please contact our support team at support@chatdev.com. We are here to help you with any questions or problems you might encounter while using this software.