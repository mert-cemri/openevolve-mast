# Even Odd Palindrome Counter

This software provides a function to count the number of even and odd integer palindromes within a given range. It is designed to be simple and efficient, suitable for use in various applications where such functionality is required.

## Main Functionality

The main function provided by this software is `even_odd_palindrome(n)`, which takes a positive integer `n` as input and returns a tuple containing the count of even and odd integer palindromes within the range from 1 to `n`, inclusive.

### Example Usage

- **Input:** `3`
  - **Output:** `(1, 2)`
  - **Explanation:** The integer palindromes within the range are 1, 2, and 3. Among them, 1 and 3 are odd, and 2 is even.

- **Input:** `12`
  - **Output:** `(4, 6)`
  - **Explanation:** The integer palindromes within the range are 1, 2, 3, 4, 5, 6, 7, 8, 9, and 11. Among them, 2, 4, 6, and 8 are even, and 1, 3, 5, 7, 9, and 11 are odd.

## Installation

To use this software, you need to have Python installed on your system. The software does not have any external dependencies, so you can directly use the provided code.

### Steps to Install Python

1. **Download Python:**
   - Visit the official Python website: [python.org](https://www.python.org/)
   - Download the latest version of Python for your operating system.

2. **Install Python:**
   - Follow the installation instructions provided on the website for your specific operating system.

3. **Verify Installation:**
   - Open a terminal or command prompt.
   - Type `python --version` and press Enter.
   - Ensure that the Python version is displayed correctly.

## How to Use

1. **Copy the Code:**
   - Copy the provided `even_odd_palindrome` function code into a Python file, e.g., `main.py`.

2. **Run the Code:**
   - Open a terminal or command prompt.
   - Navigate to the directory where your `main.py` file is located.
   - Run the file using the command: `python main.py`

3. **Test the Function:**
   - You can test the function by calling it with different values of `n` and printing the results.
   - Example:
     ```python
     print(even_odd_palindrome(3))  # Output: (1, 2)
     print(even_odd_palindrome(12)) # Output: (4, 6)
     ```

## Conclusion

This software provides a simple yet effective way to count even and odd integer palindromes within a specified range. With no external dependencies, it is easy to integrate into existing Python projects.