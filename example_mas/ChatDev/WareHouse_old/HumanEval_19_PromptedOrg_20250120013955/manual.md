# Sort Numbers User Manual

Welcome to the Sort Numbers application! This software is designed to sort a space-delimited string of numerals from 'zero' to 'nine' in ascending order. This manual provides a comprehensive guide on how to use the software, including its main functions, installation instructions, and usage examples.

## Main Function

The primary function of this software is:

### `sort_numbers(numbers: str) -> str`

- **Description**: This function takes a space-delimited string of numerals (from 'zero' to 'nine') and returns a string with the numerals sorted in ascending order.
- **Input**: A string containing numeral words separated by spaces. Valid numeral words are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
- **Output**: A string with the numeral words sorted from smallest to largest.

#### Example
```python
>>> sort_numbers('three one five')
'one three five'
```

## Installation

This software does not require any external dependencies, making it simple and easy to use. Follow the steps below to set up your environment:

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: Download or clone the repository containing the `main.py` file to your local machine.

3. **Navigate to the project directory**: Open a terminal or command prompt and navigate to the directory where `main.py` is located.

## Usage

To use the `sort_numbers` function, follow these steps:

1. **Open a Python interpreter**: You can do this by typing `python` in your terminal or command prompt.

2. **Import the function**: Import the `sort_numbers` function from the `main.py` file.
   ```python
   from main import sort_numbers
   ```

3. **Call the function**: Use the `sort_numbers` function with your desired input.
   ```python
   result = sort_numbers('three one five')
   print(result)  # Output: 'one three five'
   ```

That's it! You can now sort any string of numeral words using the `sort_numbers` function.

## Conclusion

The Sort Numbers application is a simple yet effective tool for sorting numeral words. With no external dependencies required, it is easy to set up and use. We hope this manual helps you get the most out of the software. If you have any questions or need further assistance, please feel free to reach out.