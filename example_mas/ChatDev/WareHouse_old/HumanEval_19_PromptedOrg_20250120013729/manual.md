# Sort Numbers User Manual

## Introduction

The Sort Numbers application is a simple Python-based utility designed to sort a space-delimited string of numerals from 'zero' to 'nine'. The application takes an input string of these numerals and returns a string with the numerals sorted in ascending order.

### Main Function

- **sort_numbers(numbers: str) -> str**: This function takes a single string argument, which is a space-delimited string of numerals ('zero' to 'nine'). It returns a string with the numerals sorted from smallest to largest.

Example:
```python
>>> sort_numbers('three one five')
'one three five'
```

## Installation

### Prerequisites

- Python 3.x: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Setting Up the Environment

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine. Otherwise, ensure you have the `main.py` file available.

2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

3. **Install Dependencies**: Although there are no additional dependencies listed in the `requirements.txt` file, ensure your Python environment is set up correctly.

```bash
pip install -r requirements.txt
```

Note: The `requirements.txt` file is currently empty, indicating no external libraries are required beyond the Python standard library.

## Usage

1. **Open a Python Interpreter or Script**: You can use the Python interactive shell or write a script to utilize the `sort_numbers` function.

2. **Import the Function**: If using a script, ensure you import the function from the `main.py` file.

```python
from main import sort_numbers
```

3. **Call the Function**: Pass a space-delimited string of numerals to the `sort_numbers` function and capture the output.

Example:
```python
sorted_numerals = sort_numbers('three one five')
print(sorted_numerals)  # Output: 'one three five'
```

## Conclusion

The Sort Numbers application is a straightforward tool for sorting numerals represented as words. It is designed to be easy to use and integrate into larger Python projects. If you encounter any issues or have questions, please refer to the documentation or contact support for assistance.