# Monotonic List Checker

This software module provides a function to check if a list of numbers is monotonically increasing or decreasing. It is a simple utility function that can be used in various applications where such a check is necessary.

## Quick Install

No external dependencies are required for this module. You only need Python installed on your system.

## 🤔 What is this?

The `monotonic` function determines whether a list of numbers is either entirely non-increasing or non-decreasing. This can be useful in scenarios where the order of elements matters, such as in sorting algorithms, data analysis, or validating input sequences.

### Main Function

- **monotonic(l: list) -> bool**: This function takes a list of numbers as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise.

  **Examples**:
  ```python
  >>> monotonic([1, 2, 4, 20])
  True
  >>> monotonic([1, 20, 4, 10])
  False
  >>> monotonic([4, 1, 0, -10])
  True
  ```

## How to Use

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Save the Code**: Copy the code provided below and save it in a file named `main.py`.

   ```python
   '''
   This module contains a function to check if a list is monotonically increasing or decreasing.
   '''
   def monotonic(l: list):
       """Return True if list elements are monotonically increasing or decreasing.
       >>> monotonic([1, 2, 4, 20])
       True
       >>> monotonic([1, 20, 4, 10])
       False
       >>> monotonic([4, 1, 0, -10])
       True
       """
       if not l:
           return True
       increasing = decreasing = True
       for i in range(1, len(l)):
           if l[i] > l[i - 1]:
               decreasing = False
           if l[i] < l[i - 1]:
               increasing = False
       return increasing or decreasing
   ```

3. **Run the Code**: Open a terminal or command prompt, navigate to the directory where `main.py` is located, and run the Python script using the command:

   ```bash
   python main.py
   ```

4. **Test the Function**: You can test the function by calling it with different lists and observing the output.

## Documentation

This module is straightforward and does not require additional documentation. The function is self-contained and does not rely on external libraries or dependencies. For any further questions or support, please contact our support team.