# Odd Collatz Sequence Finder

This software provides a function to compute the odd numbers in the Collatz sequence for a given positive integer. The Collatz conjecture is a well-known mathematical sequence that always ends at 1, regardless of the starting integer. This tool is useful for mathematical exploration and educational purposes.

## Main Functionality

The main function provided by this software is `get_odd_collatz(n)`, which takes a positive integer `n` as input and returns a sorted list of odd numbers in the Collatz sequence starting from `n`.

### How It Works

1. **Collatz Sequence Definition**: 
   - Start with any positive integer `n`.
   - If `n` is even, the next term is `n / 2`.
   - If `n` is odd, the next term is `3 * n + 1`.
   - Repeat the process until the sequence reaches 1.

2. **Odd Number Extraction**:
   - As the sequence is generated, odd numbers are collected.
   - The sequence always ends with 1, which is included in the result.

3. **Output**:
   - The function returns a sorted list of the odd numbers encountered in the sequence.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**:
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Download the Code**:
   - Clone or download the repository containing the `main.py` file.

## Usage

To use the `get_odd_collatz` function, follow these steps:

1. **Open a Terminal or Command Prompt**:
   - Navigate to the directory where `main.py` is located.

2. **Run Python Interpreter**:
   - Open the Python interpreter by typing `python` in the terminal.

3. **Import the Function**:
   - Import the function by executing:
     ```python
     from main import get_odd_collatz
     ```

4. **Call the Function**:
   - Call the function with a positive integer, for example:
     ```python
     print(get_odd_collatz(5))
     ```
   - This will output `[1, 5]`, as the odd numbers in the Collatz sequence starting from 5 are 5 and 1.

## Example

Here is an example of how to use the function:

```python
# Example usage:
print(get_odd_collatz(5))  # Output: [1, 5]
```

This example demonstrates calling the function with the integer 5, which returns the sorted list of odd numbers `[1, 5]` in the Collatz sequence.

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The function is self-contained and does not require additional libraries or dependencies.