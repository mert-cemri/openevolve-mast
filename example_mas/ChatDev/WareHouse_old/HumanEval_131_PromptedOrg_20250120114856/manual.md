# Digits Product Calculator

This software provides a simple function to calculate the product of odd digits in a given positive integer. If all digits in the number are even, the function returns 0.

## Main Functionality

The main functionality of this software is encapsulated in the `digits` function. This function takes a positive integer `n` as input and returns the product of its odd digits. If the number contains no odd digits, the function returns 0.

### Example Usage

- `digits(1)` returns `1`
- `digits(4)` returns `0`
- `digits(235)` returns `15`

## Installation

This software does not require any external dependencies, making it easy to set up and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py`.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python interpreter and import the `digits` function:

   ```bash
   python
   ```

   ```python
   from main import digits
   ```

4. Call the `digits` function with a positive integer as an argument:

   ```python
   result = digits(235)
   print(result)  # Output will be 15
   ```

5. You can test the function with different positive integers to see the results.

## Documentation

The `digits` function is straightforward and does not require any additional setup or configuration. It is designed to be used in any Python environment without the need for external libraries or dependencies.

For further assistance or questions, please refer to the comments within the `main.py` file, which provide additional context and examples.