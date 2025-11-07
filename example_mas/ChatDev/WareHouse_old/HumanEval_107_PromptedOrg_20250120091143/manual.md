# Even Odd Palindrome Counter

This software provides a function to count the number of even and odd integer palindromes within a given range. A palindrome is a number that reads the same forwards and backwards.

## Main Functionality

The main function provided by this software is `even_odd_palindrome(n)`. Given a positive integer `n`, this function returns a tuple containing the number of even and odd integer palindromes within the range from 1 to `n`, inclusive.

### Example Usage

- Input: `3`
  - Output: `(1, 2)`
  - Explanation: The integer palindromes are 1, 2, and 3. One of them is even, and two of them are odd.

- Input: `12`
  - Output: `(4, 6)`
  - Explanation: The integer palindromes are 1, 2, 3, 4, 5, 6, 7, 8, 9, and 11. Four of them are even, and six of them are odd.

## Installation

### Environment Setup

To use this software, you need to have Python installed on your system. The software does not have any external dependencies, so you do not need to install any additional packages.

1. **Install Python**: If you do not have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change your directory to the cloned repository:
   ```
   cd <repository-directory>
   ```

## How to Use

1. **Open the `main.py` File**: Open the `main.py` file in your preferred code editor.

2. **Call the Function**: Use the `even_odd_palindrome(n)` function to get the count of even and odd palindromes. For example:
   ```python
   result = even_odd_palindrome(12)
   print(result)  # Output: (4, 6)
   ```

3. **Run the Script**: Run the script using Python:
   ```
   python main.py
   ```

## Notes

- The function is designed to handle inputs where `1 <= n <= 1000`.
- The function returns a tuple with the first element being the count of even palindromes and the second element being the count of odd palindromes.

This software provides a simple yet effective way to count even and odd palindromes within a specified range, making it a useful tool for educational purposes or basic numerical analysis.