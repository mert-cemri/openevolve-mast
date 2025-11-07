# Even Odd Palindrome Counter

This software provides a function to count the number of even and odd integer palindromes within a given range. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function of this software is `even_odd_palindrome(n)`, which takes a positive integer `n` as input and returns a tuple containing the count of even and odd integer palindromes within the range from 1 to `n`, inclusive.

### Example Usage

- Input: `3`
  - Output: `(1, 2)`
  - Explanation: The integer palindromes are 1, 2, 3. One of them is even, and two of them are odd.

- Input: `12`
  - Output: `(4, 6)`
  - Explanation: The integer palindromes are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. Four of them are even, and six of them are odd.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the function in a Python script or an interactive Python shell. Here’s how you can use it in a Python script:

   ```python
   from main import even_odd_palindrome

   result = even_odd_palindrome(12)
   print(result)  # Output: (4, 6)
   ```

4. **Interactive Shell**: Alternatively, you can test the function in an interactive Python shell:

   ```python
   >>> from main import even_odd_palindrome
   >>> even_odd_palindrome(12)
   (4, 6)
   ```

## Documentation

The function is straightforward and does not require additional configuration. The logic checks each number in the range to determine if it is a palindrome and whether it is even or odd, incrementing the respective counters accordingly.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided within the code comments for further clarification.