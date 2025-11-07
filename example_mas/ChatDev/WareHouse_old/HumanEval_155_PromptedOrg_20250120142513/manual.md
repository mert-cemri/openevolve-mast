# Even Odd Count Function

This software provides a simple Python function to count the number of even and odd digits in a given integer. It is designed to be straightforward and easy to integrate into any Python application where such functionality is needed.

## Main Functionality

The core functionality of this software is encapsulated in the `even_odd_count` function. This function takes an integer as input and returns a tuple containing the count of even and odd digits in the number.

### Example Usage

```python
# Example 1
result = even_odd_count(-12)
print(result)  # Output: (1, 1)

# Example 2
result = even_odd_count(123)
print(result)  # Output: (1, 2)
```

## Installation

This software does not require any external libraries or dependencies beyond Python itself. To use the function, simply ensure you have Python installed on your system.

### Installing Python

If you do not have Python installed, you can download it from the official website: [Python Downloads](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

## How to Use

1. **Download the Code:**
   - Copy the code provided in the `main.py` file into your Python environment or script.

2. **Run the Function:**
   - Use the `even_odd_count` function by passing an integer as an argument.
   - The function will return a tuple with the first element being the count of even digits and the second element being the count of odd digits.

3. **Example Code:**

   ```python
   def even_odd_count(num):
       # Convert the number to its absolute value
       num = abs(num)
       # Convert the number to a string to iterate over each digit
       num_str = str(num)
       # Initialize counters for even and odd digits
       even_count = 0
       odd_count = 0
       # Iterate over each character in the string representation of the number
       for digit in num_str:
           # Convert character back to integer
           digit = int(digit)
           # Check if the digit is even or odd
           if digit % 2 == 0:
               even_count += 1
           else:
               odd_count += 1
       # Return the tuple with the counts of even and odd digits
       return (even_count, odd_count)

   # Example usage
   print(even_odd_count(-12))  # Output: (1, 1)
   print(even_odd_count(123))  # Output: (1, 2)
   ```

## Additional Information

This function is designed to handle integers of any size, including negative numbers. The function first converts the number to its absolute value, ensuring that the sign does not affect the digit count. The function then iterates over each digit, checking if it is even or odd, and updates the respective counters accordingly.

For any questions or further assistance, please contact our support team.