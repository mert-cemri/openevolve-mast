manual.md

```
# Prime Number Checker

This software provides a simple function to determine if a given number is prime. It is implemented in Python and can be used to check the primality of numbers efficiently.

## Main Function

The main function provided by this software is `is_prime(n)`. This function takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise.

### Function Details

- **Function Name:** `is_prime`
- **Input:** An integer `n`
- **Output:** A boolean value (`True` or `False`)
- **Description:** The function checks if the input number `n` is a prime number. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

### Example Usage

```python
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```

## Installation

To use this software, you need to have Python installed on your system. The function does not require any external dependencies, so no additional packages are needed.

### Quick Install

1. **Ensure Python is installed:** You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository:** Obtain the `main.py` file containing the `is_prime` function.

3. **Run the function:** You can use the function in your Python scripts or interactively in a Python shell.

## How to Use

1. **Open a Python environment:** You can use an IDE like PyCharm, VSCode, or a simple text editor with a terminal.

2. **Import the function:** If you have saved the `main.py` file in your project, you can import the function using:
   ```python
   from main import is_prime
   ```

3. **Call the function:** Use the `is_prime` function with any integer to check its primality:
   ```python
   result = is_prime(29)
   print(result)  # Output: True
   ```

## Documentation

For further information and examples, you can refer to the docstring provided within the `is_prime` function in the `main.py` file. The docstring includes example usages and expected outputs.

```