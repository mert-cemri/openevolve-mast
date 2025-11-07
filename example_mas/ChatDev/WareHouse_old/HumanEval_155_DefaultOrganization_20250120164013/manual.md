# Even Odd Count

This software provides a simple function to count the number of even and odd digits in a given integer. It is designed to be straightforward and efficient, making it easy to integrate into larger applications where such functionality is needed.

## Main Functionality

The primary function provided by this software is `even_odd_count(num)`. This function takes an integer as input and returns a tuple containing two elements:
- The first element is the count of even digits in the integer.
- The second element is the count of odd digits in the integer.

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

This software is implemented in Python and does not require any additional dependencies beyond the standard Python library. To use the function, simply include the `main.py` file in your project and import the function as needed.

### Quick Setup

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the `main.py` file from the repository.

3. Include the `main.py` file in your project directory.

4. Import the `even_odd_count` function in your Python script:

```python
from main import even_odd_count
```

## How to Use

1. **Import the Function**: Start by importing the `even_odd_count` function from the `main.py` file.

2. **Call the Function**: Pass an integer to the `even_odd_count` function. The function will return a tuple with the counts of even and odd digits.

3. **Handle the Output**: Use the returned tuple as needed in your application.

### Example Code

```python
from main import even_odd_count

# Test the function with a positive integer
print(even_odd_count(2468))  # Output: (4, 0)

# Test the function with a negative integer
print(even_odd_count(-1357))  # Output: (0, 4)

# Test the function with a mix of even and odd digits
print(even_odd_count(1234567890))  # Output: (5, 5)
```

## Conclusion

The `even_odd_count` function is a simple yet effective tool for counting even and odd digits in an integer. It can be easily integrated into any Python project without the need for additional dependencies. Simply include the `main.py` file in your project, import the function, and start using it to analyze integers in your application.