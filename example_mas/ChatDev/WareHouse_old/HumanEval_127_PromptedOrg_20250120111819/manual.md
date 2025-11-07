# Intersection Prime Checker

This software module provides a function to determine if the length of the intersection of two intervals is a prime number. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function provided by this module is `intersection(interval1, interval2)`. This function takes two intervals as input and returns "YES" if the length of their intersection is a prime number, and "NO" otherwise.

### Function Details

- **Function Name:** `intersection`
- **Parameters:**
  - `interval1`: A tuple representing the first interval as a pair of integers (start, end).
  - `interval2`: A tuple representing the second interval as a pair of integers (start, end).
- **Returns:** A string "YES" if the length of the intersection is a prime number, otherwise "NO".

### Example Usage

```python
print(intersection((1, 2), (2, 3)))  # Output: "NO"
print(intersection((-1, 1), (0, 4)))  # Output: "NO"
print(intersection((-3, -1), (-5, 5)))  # Output: "YES"
```

## Installation

This module does not require any external dependencies, so you can use it directly in your Python environment. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository:**
   - If this code is part of a larger repository, clone the repository to your local machine.

2. **Navigate to the Directory:**
   - Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Code:**
   - You can run the code by executing the `main.py` file in your Python environment. Use the function `intersection` to check the intersection of intervals.

4. **Example Command:**
   - Open a Python interpreter or create a script and import the `intersection` function to use it as demonstrated in the example usage section.

## Conclusion

This module provides a straightforward solution to determine if the length of the intersection of two intervals is a prime number. With no external dependencies, it is easy to integrate into existing projects or use as a standalone utility.