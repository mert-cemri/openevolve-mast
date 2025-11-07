# Fizz Buzz Digit Counter

This software provides a function to count the number of times the digit '7' appears in integers less than a given number `n`, where those integers are divisible by either 11 or 13.

## Main Functionality

The main function provided by this software is:

- `fizz_buzz(n: int) -> int`: This function takes an integer `n` as input and returns the count of the digit '7' in integers less than `n` that are divisible by 11 or 13.

### Example Usage

```python
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Start

1. **Ensure you have Python installed**: This software requires Python to run. You can download and install Python from [python.org](https://www.python.org/).

2. **Download the Code**: Save the provided `main.py` file to your local machine.

3. **Run the Code**: You can execute the code by running the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

   This will execute the example usage and display the output.

## How to Use

1. **Import the Function**: If you want to use the `fizz_buzz` function in your own scripts, you can import it from the `main.py` file.

   ```python
   from main import fizz_buzz
   ```

2. **Call the Function**: Use the `fizz_buzz` function by passing an integer `n` as an argument to get the count of the digit '7' in the specified range.

   ```python
   result = fizz_buzz(100)
   print(result)  # This will print the count of '7's in numbers less than 100 divisible by 11 or 13.
   ```

## Documentation

For further details on how the function works, you can refer to the docstring provided in the code. The function is designed to be simple and efficient, leveraging Python's string manipulation capabilities to count occurrences of the digit '7'.

This software is ideal for educational purposes or as a utility in larger projects where such a specific counting functionality is required.