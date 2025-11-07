# Prime Length Checker

This software provides a simple utility to check if the length of a given string is a prime number. It includes a function `prime_length` that returns `True` if the length of the string is a prime number and `False` otherwise.

## Main Functions

### `prime_length(string)`

- **Description**: This function takes a string as input and checks if the length of the string is a prime number.
- **Parameters**: 
  - `string` (str): The input string whose length is to be checked.
- **Returns**: 
  - `bool`: Returns `True` if the length of the string is a prime number, `False` otherwise.
- **Examples**:
  - `prime_length('Hello')` returns `True`
  - `prime_length('abcdcba')` returns `True`
  - `prime_length('kittens')` returns `True`
  - `prime_length('orange')` returns `False`

## Installation

### Environment Setup

This software does not require any external dependencies, making it easy to set up and use. You can run the software in any Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the `main.py` file to your local machine.

3. Navigate to the directory containing `main.py` using your terminal or command prompt.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python script by executing the following command:

   ```bash
   python main.py
   ```

4. You can modify the script to test different strings by calling the `prime_length` function with your desired input.

## Example Usage

Here's a simple example of how you can use the `prime_length` function in your Python script:

```python
from main import prime_length

print(prime_length('Hello'))  # Output: True
print(prime_length('abcdcba'))  # Output: True
print(prime_length('kittens'))  # Output: True
print(prime_length('orange'))  # Output: False
```

This software is designed to be straightforward and efficient, allowing you to easily determine if the length of a string is a prime number. Enjoy using the Prime Length Checker!