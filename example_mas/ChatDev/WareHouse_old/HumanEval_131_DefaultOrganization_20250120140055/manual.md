# Digits Product Calculator

This software provides a function to calculate the product of odd digits in a given positive integer. If all digits are even, it returns 0. This is a simple utility function that can be used in various applications where such a calculation is needed.

## Main Functionality

The main function of this software is:

- **digits(n):** Given a positive integer `n`, this function returns the product of its odd digits. If all digits are even, it returns 0.

### Examples

- `digits(1)` returns `1`
- `digits(4)` returns `0`
- `digits(235)` returns `15`

## Installation

There are no external dependencies required for this software, so you don't need to install any additional packages. Simply ensure you have Python installed on your system.

## How to Use

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Run the Function:**
   - You can use the `digits` function by including the code in your Python script or by running it in an interactive Python session.

3. **Example Usage:**
   - Open a terminal or command prompt.
   - Run Python by typing `python` and pressing Enter.
   - Copy and paste the following code into the Python interpreter:

     ```python
     def digits(n):
         product = 1
         has_odd = False
         while n > 0:
             digit = n % 10
             if digit % 2 != 0:
                 product *= digit
                 has_odd = True
             n //= 10
         return product if has_odd else 0

     # Example usage:
     print(digits(1))  # Output: 1
     print(digits(4))  # Output: 0
     print(digits(235))  # Output: 15
     ```

4. **Test the Function:**
   - You can test the function with different positive integers to see the results.

## Documentation

This function is straightforward and does not require additional documentation beyond the examples provided. If you have any questions or need further assistance, please feel free to reach out to our support team.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to help you with any problems you might encounter while using this software.