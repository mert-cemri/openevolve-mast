# Starts One Ends

A Python function to calculate the count of n-digit positive integers that start or end with the digit '1'.

## Introduction

The `starts_one_ends` function is designed to solve a specific problem: given a positive integer `n`, it returns the count of n-digit positive integers that either start or end with the digit '1'. This function is useful in mathematical computations and number theory applications where such patterns are analyzed.

## Quick Install

This project does not require any external dependencies, so you can run the function directly in any Python environment. However, ensure you have Python installed on your system.

### Python Installation

If you do not have Python installed, you can download it from the official website: [Python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository:**

   You can clone the repository using Git or download the ZIP file and extract it to your desired location.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

   ```bash
   cd path/to/project-directory
   ```

3. **Run the Function:**

   You can run the function by executing the `main.py` file in a Python environment. You can either call the function directly in the script or import it into another Python script.

   ```python
   from main import starts_one_ends

   # Example usage
   n = 3
   result = starts_one_ends(n)
   print(f"The count of {n}-digit numbers starting or ending with 1 is: {result}")
   ```

4. **Modify and Experiment:**

   Feel free to modify the code to experiment with different values of `n` or integrate the function into larger projects as needed.

## Function Explanation

The `starts_one_ends` function works as follows:

- **Input:** A positive integer `n`.
- **Output:** The count of n-digit positive integers that start or end with the digit '1'.

### Logic

- For `n = 1`, the function returns `2` because the numbers `1` and `10` are the only 1-digit numbers that start or end with '1'.
- For `n > 1`, the function calculates:
  - Numbers starting with '1': `10**(n-1)`
  - Numbers ending with '1': `10**(n-1)`
  - Numbers both starting and ending with '1': `10**(n-2)`
- The total count is calculated as the sum of numbers starting with '1' and ending with '1', minus those counted twice (both starting and ending with '1').

This logic ensures that all numbers fitting the criteria are counted accurately.

## Conclusion

The `starts_one_ends` function is a simple yet powerful tool for counting specific patterns in numbers. With no external dependencies, it is easy to integrate into any Python project. Feel free to explore and utilize this function in your mathematical and computational tasks.