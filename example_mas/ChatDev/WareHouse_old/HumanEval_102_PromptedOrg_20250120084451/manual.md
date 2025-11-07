# Choose_Num Function User Manual

## Introduction

The `choose_num` function is a simple Python utility designed to find the largest even integer within a specified range of two positive numbers, `x` and `y`. This function is particularly useful in scenarios where you need to determine the largest even number within a given range, and it efficiently handles cases where no such number exists.

## Main Functionality

- **Function Name:** `choose_num(x, y)`
- **Purpose:** Returns the largest even integer within the inclusive range `[x, y]`. If no even number exists in the range, it returns `-1`.
- **Parameters:**
  - `x`: A positive integer representing the start of the range.
  - `y`: A positive integer representing the end of the range.
- **Returns:** The largest even integer within the range `[x, y]`, or `-1` if no even number is found.

## Quick Install

To use the `choose_num` function, ensure you have Python installed on your system. No additional dependencies are required for this function.

## How to Use

1. **Copy the Code:**

   Copy the following code into a Python file named `main.py`:

   ```python
   def choose_num(x, y):
       """This function takes two positive numbers x and y and returns the
       biggest even integer number that is in the range [x, y] inclusive. If 
       there's no such number, then the function should return -1.
       For example:
       choose_num(12, 15) = 14
       choose_num(13, 12) = -1
       """
       # Ensure x is less than or equal to y
       if x > y:
           x, y = y, x
       # Iterate from y to x to find the largest even number
       for num in range(y, x - 1, -1):
           if num % 2 == 0:
               return num
       # If no even number is found, return -1
       return -1
   ```

2. **Run the Function:**

   Open a terminal or command prompt, navigate to the directory containing `main.py`, and run the Python interpreter. You can then call the `choose_num` function with your desired parameters.

   Example usage:

   ```python
   result = choose_num(12, 15)
   print(result)  # Output: 14

   result = choose_num(13, 12)
   print(result)  # Output: -1
   ```

3. **Understanding the Output:**

   - If the function returns an even number, it is the largest even integer within the specified range.
   - If the function returns `-1`, it indicates that no even number exists within the range.

## Conclusion

The `choose_num` function is a straightforward and efficient tool for finding the largest even integer within a specified range. With no additional dependencies required, it is easy to integrate into any Python project where such functionality is needed.