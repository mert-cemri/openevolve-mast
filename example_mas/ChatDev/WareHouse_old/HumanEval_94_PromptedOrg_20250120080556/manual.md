# Prime Digit Sum Finder

This software provides a function to find the largest prime number in a given list of integers and returns the sum of its digits. It is a simple yet effective tool for tasks that require prime number analysis and digit summation.

## Main Functions

The software includes the following main functions:

1. **is_prime(n)**: Checks if a number `n` is a prime number.
2. **sum_of_digits(n)**: Calculates the sum of the digits of a number `n`.
3. **skjkasdkd(lst)**: Takes a list of integers `lst`, finds the largest prime number in the list, and returns the sum of its digits.

## Installation

To use this software, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly use the provided Python script.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Download the script**: Save the provided `main.py` script to your local machine.

## How to Use

1. **Prepare your list of integers**: Create a list of integers that you want to analyze.

2. **Run the script**: Use a Python environment to run the script. You can do this by opening a terminal or command prompt, navigating to the directory where `main.py` is located, and executing the following command:

   ```bash
   python main.py
   ```

3. **Call the function**: In the Python environment, call the `skjkasdkd(lst)` function with your list of integers as the argument. For example:

   ```python
   result = skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3])
   print(result)  # Output should be 10
   ```

4. **Interpret the result**: The function will return the sum of the digits of the largest prime number found in the list.

## Example Usage

Here are some example inputs and expected outputs:

- Input: `[0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]`
  - Output: `10`

- Input: `[1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]`
  - Output: `25`

- Input: `[0, 81, 12, 3, 1, 21]`
  - Output: `3`

This software is designed to be simple and efficient, providing quick results for prime number analysis and digit summation tasks.