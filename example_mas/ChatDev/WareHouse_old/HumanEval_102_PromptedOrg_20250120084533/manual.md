# Choose_Num Function User Manual

## Introduction

The `choose_num` function is a simple Python utility designed to find the largest even integer within a specified inclusive range [x, y]. If no even number exists within the range, the function returns -1. This function is particularly useful for applications that require quick identification of even numbers within a given range.

## Main Functionality

- **Function Name**: `choose_num`
- **Purpose**: To return the largest even integer within the inclusive range [x, y]. If no even number is found, it returns -1.
- **Parameters**:
  - `x`: The starting integer of the range.
  - `y`: The ending integer of the range.
- **Returns**: The largest even integer within the range [x, y], or -1 if no even number is found.

### Example Usage

```python
result1 = choose_num(12, 15)  # Returns 14
result2 = choose_num(13, 12)  # Returns -1
```

## Installation

To use the `choose_num` function, you need to have Python installed on your machine. Follow the steps below to set up your environment:

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

### Step 2: Set Up Your Environment

1. **Create a Virtual Environment (Optional but Recommended)**:
   - Open your terminal or command prompt.
   - Navigate to your project directory.
   - Run the following command to create a virtual environment:
     ```bash
     python -m venv myenv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       myenv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source myenv/bin/activate
       ```

2. **Install Necessary Dependencies**:
   - For this function, there are no additional dependencies required beyond Python itself.

## How to Use

1. **Create a Python File**:
   - Create a file named `main.py` in your project directory.

2. **Implement the Function**:
   - Copy the following code into `main.py`:

     ```python
     def choose_num(x, y):
         """This function takes two positive numbers x and y and returns the
         biggest even integer number that is in the range [x, y] inclusive. If 
         there's no such number, then the function should return -1.
         """
         # Ensure x is less than or equal to y
         if x > y:
             x, y = y, x
         # Start from the largest number and check for evenness
         for num in range(y, x - 1, -1):
             if num % 2 == 0:
                 return num
         # Return -1 if no even number is found
         return -1
     ```

3. **Run the Function**:
   - In the terminal, navigate to the directory containing `main.py`.
   - Run the script using Python:
     ```bash
     python main.py
     ```

4. **Test the Function**:
   - You can test the function by calling it with different values of `x` and `y` and printing the results.

## Conclusion

The `choose_num` function is a straightforward utility for identifying the largest even integer within a specified range. By following the instructions in this manual, you can easily integrate and use this function in your Python projects.