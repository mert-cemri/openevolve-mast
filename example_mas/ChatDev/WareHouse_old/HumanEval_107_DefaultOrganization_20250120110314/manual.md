# Even Odd Palindrome Software

This software provides a function to calculate the number of even and odd integer palindromes within a given range. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function of this software is `even_odd_palindrome(n)`, which takes a positive integer `n` as input and returns a tuple containing the count of even and odd integer palindromes from 1 to `n`, inclusive.

### Example Usage

- **Input:** `3`
  - **Output:** `(1, 2)`
  - **Explanation:** The integer palindromes are 1, 2, and 3. One of them is even, and two of them are odd.

- **Input:** `12`
  - **Output:** `(4, 6)`
  - **Explanation:** The integer palindromes are 1, 2, 3, 4, 5, 6, 7, 8, 9, and 11. Four of them are even, and six of them are odd.

## Installation

This software does not require any external dependencies. You can simply download the `main.py` file and run it using Python.

### Prerequisites

- Python 3.x

### Installation Steps

1. **Download the Code:**
   - Download the `main.py` file to your local machine.

2. **Run the Code:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the following command:
     ```bash
     python main.py
     ```

## How to Use

1. **Import the Function:**
   - If you want to use the function in another script, you can import it as follows:
     ```python
     from main import even_odd_palindrome
     ```

2. **Call the Function:**
   - Pass a positive integer `n` to the function to get the count of even and odd palindromes.
     ```python
     result = even_odd_palindrome(12)
     print(result)  # Output: (4, 6)
     ```

## Documentation

For further details and examples, please refer to the comments within the `main.py` file. The code is well-documented to help you understand how it works and how to modify it if needed.

## Support

If you encounter any issues or have questions, feel free to reach out to our support team. We are here to help you make the most out of this software.