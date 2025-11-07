# Distinct Character Counter

This software provides a simple function to count the number of distinct characters in a given string, regardless of case sensitivity. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function provided by this software is `count_distinct_characters`. This function takes a string as input and returns the number of distinct characters in that string, ignoring case differences.

### Function Signature

```python
def count_distinct_characters(string: str) -> int:
```

### Example Usage

```python
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
```

## Installation

Since this software does not require any external dependencies, you can run it in any Python environment without additional installation steps. Ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine. Otherwise, simply copy the code provided into a file named `main.py`.

## How to Use

1. **Open a Terminal or Command Prompt**: Navigate to the directory where `main.py` is located.

2. **Run Python Interpreter**: Open the Python interpreter by typing `python` in your terminal.

3. **Import the Function**: Import the function from `main.py` using the following command:

   ```python
   from main import count_distinct_characters
   ```

4. **Call the Function**: Use the function with your desired input string:

   ```python
   result = count_distinct_characters('YourStringHere')
   print(result)
   ```

This will output the number of distinct characters in the provided string, ignoring case differences.

## Documentation

For further documentation or examples, you can refer to the docstring provided within the `main.py` file. The docstring includes example usages and expected outputs.

This software is designed to be simple and straightforward, making it easy to integrate into larger projects or use as a standalone utility.