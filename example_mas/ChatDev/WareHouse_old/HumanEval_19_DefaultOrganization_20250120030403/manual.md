# Sort Numbers Application

This application provides a simple function to sort a space-delimited string of numerals from 'zero' to 'nine'. The function is designed to take a string input and return a string with the numerals sorted in ascending order based on their numerical value.

## Main Functionality

The core functionality of this application is encapsulated in the `sort_numbers` function. This function:

- Accepts a space-delimited string of numerals as input.
- Sorts the numerals in ascending order based on their numerical value.
- Returns a space-delimited string of the sorted numerals.

### Example

```python
>>> sort_numbers('three one five')
'one three five'
```

## Installation

### Environment Setup

This application does not require any external dependencies, making it straightforward to set up. You can run the code in any Python environment. Here are the steps to set up your environment:

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine. Otherwise, you can directly copy the code into a Python file named `main.py`.

3. **No Additional Packages Required**: Since there are no external dependencies, you do not need to install any additional packages.

## Usage

To use the `sort_numbers` function, follow these steps:

1. **Open a Python Environment**: You can use an IDE like PyCharm, VSCode, or a simple text editor to run the Python script.

2. **Write the Code**: Copy the provided code into a file named `main.py`.

3. **Run the Code**: Execute the script in your Python environment. You can test the function by calling it with different inputs.

### Example Usage

```python
# Import the function from the module
from main import sort_numbers

# Test the function with an example input
result = sort_numbers('three one five')
print(result)  # Output: 'one three five'
```

## Documentation

For further information and examples, you can refer to the inline documentation provided within the code. The docstring in the `sort_numbers` function provides a concise explanation of its purpose and usage.

This application is designed to be simple and efficient, providing a straightforward solution to sorting numerals represented as words. Enjoy using the Sort Numbers Application!