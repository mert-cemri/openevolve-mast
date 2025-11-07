manual.md

```
# Rounded Average Calculator

This software provides a simple function to calculate the rounded average of integers within a specified range and convert the result to a binary string. It is designed to be lightweight and efficient, requiring no external dependencies.

## Main Functionality

The main function provided by this software is `rounded_avg(n, m)`. This function performs the following tasks:

- Computes the average of all integers from `n` to `m` (inclusive).
- Rounds the computed average to the nearest integer.
- Converts the rounded average to a binary string.
- Returns `-1` if the starting integer `n` is greater than the ending integer `m`.

### Example Usage

- `rounded_avg(1, 5)` returns `"0b11"`, which is the binary representation of the rounded average of numbers from 1 to 5.
- `rounded_avg(7, 5)` returns `-1` because `n` is greater than `m`.
- `rounded_avg(10, 20)` returns `"0b1111"`, which is the binary representation of the rounded average of numbers from 10 to 20.
- `rounded_avg(20, 33)` returns `"0b11010"`, which is the binary representation of the rounded average of numbers from 20 to 33.

## Installation

This software does not require any external libraries or dependencies. It is implemented purely in Python, making it easy to integrate into any Python environment.

### Quick Install

To use the `rounded_avg` function, simply download the `main.py` file and include it in your project. There are no additional installation steps required.

## How to Use

1. **Download the `main.py` file**: Ensure that the file is in your working directory or project folder.

2. **Import the function**: In your Python script, import the `rounded_avg` function from the `main.py` file.

   ```python
   from main import rounded_avg
   ```

3. **Call the function**: Use the function by passing two positive integers as arguments.

   ```python
   result = rounded_avg(1, 5)
   print(result)  # Output: "0b11"
   ```

4. **Handle the output**: The function will return a binary string or `-1` based on the input values.

## Documentation

The function is straightforward and self-contained. For further information or assistance, please refer to the comments within the `main.py` file, which provide a detailed explanation of the function's logic and usage.

```