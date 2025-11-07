manual.md

```
# Search Function Application

This application provides a simple yet effective solution to find the greatest integer in a list that has a frequency greater than or equal to the integer itself. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The core functionality of this application is encapsulated in the `search` function. This function takes a list of positive integers as input and returns the greatest integer that meets the specified frequency condition. If no such integer exists, it returns -1.

### Function Definition

```python
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
```

## Installation

This application does not require any external libraries or dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the source code for the application.

3. **Navigate to the project directory**: Use your command line interface to navigate to the directory containing the `main.py` file.

## How to Use

1. **Open the `main.py` file**: This file contains the implementation of the `search` function.

2. **Call the `search` function**: You can test the function by calling it with different lists of integers. For example:

    ```python
    result = search([4, 1, 2, 2, 3, 1])
    print(result)  # Output: 2
    ```

3. **Modify and test**: Feel free to modify the input list and test the function with different scenarios to see how it behaves.

## Documentation

For further information and detailed examples, please refer to the comments within the `main.py` file. The function is well-documented to help you understand its purpose and usage.

## Support

If you encounter any issues or have questions, please feel free to reach out to our support team. We are here to assist you in making the most out of this application.

```