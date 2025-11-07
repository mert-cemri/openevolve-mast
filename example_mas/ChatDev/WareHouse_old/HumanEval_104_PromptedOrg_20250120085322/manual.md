# Unique Digits

This software provides a function to filter and sort a list of positive integers, returning only those that do not contain any even digits. The result is a sorted list in increasing order.

## Main Functionality

The main function provided by this software is `unique_digits`, which takes a list of positive integers and returns a sorted list of integers that do not contain any even digits.

### Example Usage

```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]

>>> unique_digits([152, 323, 1422, 10])
[]
```

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need a Python environment to run the code.

### Setting Up the Environment

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

3. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

## How to Use

1. **Open the Python Environment**: You can use any Python IDE or a simple command line interface.

2. **Run the Code**: Execute the `main.py` file or import the `unique_digits` function into your script.

3. **Call the Function**: Pass a list of positive integers to the `unique_digits` function to get the desired output.

### Example

```python
from main import unique_digits

# Example list of integers
numbers = [15, 33, 1422, 1]

# Get the list of numbers without even digits
result = unique_digits(numbers)

# Print the result
print(result)  # Output: [1, 15, 33]
```

## Documentation

For further information, you can refer to the comments within the `main.py` file, which provide detailed explanations of the function and its components.

This software is designed to be straightforward and easy to integrate into larger projects where filtering numbers based on digit characteristics is required.