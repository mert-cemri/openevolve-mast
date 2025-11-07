# Even Odd Palindrome Counter

This software is designed to count the number of even and odd integer palindromes within a given range. A palindrome is a number that reads the same backward as forward. This tool can be useful for educational purposes, algorithm testing, or simply for fun.

## Main Functionality

The main functionality of this software is encapsulated in the `even_odd_palindrome` function. Given a positive integer `n`, the function returns a tuple containing the count of even and odd integer palindromes within the range from 1 to `n`, inclusive.

### Example Usage

- **Input:** `3`
- **Output:** `(1, 2)`
  - Explanation: The integer palindromes are 1, 2, and 3. Among them, 1 is even, and 2 are odd.

- **Input:** `12`
- **Output:** `(4, 6)`
  - Explanation: The integer palindromes are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. Among them, 4 are even, and 6 are odd.

## Installation

This software does not require any external dependencies, making it easy to set up and use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone the repository**: If this software is hosted on a version control system, clone the repository to your local machine.

3. **Navigate to the project directory**: Use the command line to navigate to the directory where the `main.py` file is located.

## How to Use

1. **Open the `main.py` file**: You can open this file in any Python-compatible IDE or text editor.

2. **Call the function**: You can call the `even_odd_palindrome` function with your desired input. For example:

   ```python
   result = even_odd_palindrome(12)
   print(result)  # Output will be (4, 6)
   ```

3. **Run the script**: Execute the script using Python. In the command line, navigate to the directory containing `main.py` and run:

   ```bash
   python main.py
   ```

4. **View the results**: The output will display the number of even and odd palindromes within the specified range.

## Documentation

- **Function Definition**: The `even_odd_palindrome` function is defined to take a single integer input `n` and returns a tuple `(even_count, odd_count)`.

- **Logic**: The function iterates through numbers from 1 to `n`, checks if each number is a palindrome, and then counts how many of these are even and how many are odd.

This manual provides all the necessary information to understand, install, and use the software effectively. Enjoy exploring the world of palindromes!