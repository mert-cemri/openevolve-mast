# Even Odd Palindrome Counter

This software provides a function to calculate the number of even and odd integer palindromes within a given range from 1 to n. It is a simple Python application designed to help users determine the count of even and odd palindromes up to a specified number.

## Main Functions

The main function of this software is `even_odd_palindrome(n)`, which takes a positive integer `n` as input and returns a tuple containing the number of even and odd integer palindromes within the range from 1 to `n`, inclusive.

### Function Details

- **`is_palindrome(num)`**: A helper function that checks if a given number is a palindrome. It returns `True` if the number is a palindrome and `False` otherwise.

- **`even_odd_palindrome(n)`**: This function iterates through all numbers from 1 to `n`, checks if each number is a palindrome using the `is_palindrome` function, and counts how many of these palindromes are even and how many are odd. It returns a tuple `(even_count, odd_count)`.

## Installation

This software does not require any external dependencies, so there is no need for a `requirements.txt` file. You only need Python installed on your system to run the code.

### Quick Install

Ensure you have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Code**: You can run the code by executing the following command in your terminal:

   ```bash
   python main.py
   ```

4. **Use the Function**: To use the `even_odd_palindrome` function, you can import it into your Python script or interactive shell and call it with a positive integer `n` as an argument. For example:

   ```python
   from main import even_odd_palindrome

   result = even_odd_palindrome(12)
   print(result)  # Output: (4, 6)
   ```

## Example Usage

Here are a couple of examples to demonstrate how the function works:

- **Example 1**: For `n = 3`, the function will return `(1, 2)` because the integer palindromes are 1, 2, and 3. One of them is even, and two of them are odd.

- **Example 2**: For `n = 12`, the function will return `(4, 6)` because the integer palindromes are 1, 2, 3, 4, 5, 6, 7, 8, 9, and 11. Four of them are even, and six of them are odd.

This software is designed to be simple and efficient, providing accurate results for any positive integer input within the specified range.