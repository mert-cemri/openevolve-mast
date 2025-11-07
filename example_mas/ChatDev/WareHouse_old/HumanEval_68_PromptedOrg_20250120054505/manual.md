# Pluck Function User Manual

## Introduction

The `pluck` function is a simple utility designed to process an array of non-negative integers. It identifies and returns the smallest even number from the array along with its index. If no even numbers are present, or if the array is empty, the function returns an empty list.

## Main Functionality

- **pluck(arr):** This function takes a list of non-negative integers as input and returns a list containing the smallest even number and its index. If there are multiple occurrences of the smallest even number, the function returns the first occurrence. If no even numbers are found, it returns an empty list.

## Installation

The `pluck` function is implemented in Python and does not require any external dependencies. Ensure that you have Python installed on your system. The recommended Python version is 3.6 or higher.

### Steps to Install Python

1. **Download Python:**
   - Visit the official Python website: [Python.org](https://www.python.org/)
   - Download the latest version of Python for your operating system.

2. **Install Python:**
   - Run the installer and follow the on-screen instructions.
   - Ensure that you check the option to add Python to your system's PATH during installation.

3. **Verify Installation:**
   - Open a terminal or command prompt.
   - Type `python --version` and press Enter.
   - Ensure that the installed version is 3.6 or higher.

## How to Use the Pluck Function

1. **Create a Python Script:**
   - Open a text editor or an Integrated Development Environment (IDE).
   - Create a new file named `main.py`.

2. **Implement the Pluck Function:**
   - Copy the following code into `main.py`:

   ```python
   def pluck(arr):
       """
       Given an array representing a branch of a tree that has non-negative integer nodes,
       your task is to pluck one of the nodes and return it.
       The plucked node should be the node with the smallest even value.
       If multiple nodes with the same smallest even value are found, return the node that has the smallest index.
       The plucked node should be returned in a list, [smallest_value, its index].
       If there are no even values or the given array is empty, return [].
       """
       smallest_even = None
       smallest_index = -1
       for index, value in enumerate(arr):
           if value % 2 == 0:
               if smallest_even is None or value < smallest_even:
                   smallest_even = value
                   smallest_index = index
       if smallest_even is not None:
           return [smallest_even, smallest_index]
       else:
           return []
   ```

3. **Run the Script:**
   - Save the `main.py` file.
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the script using the command: `python main.py`

4. **Test the Function:**
   - You can test the function by calling it with different arrays and printing the results. For example:

   ```python
   print(pluck([4, 2, 3]))  # Output: [2, 1]
   print(pluck([1, 2, 3]))  # Output: [2, 1]
   print(pluck([]))         # Output: []
   print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
   ```

## Conclusion

The `pluck` function is a straightforward utility for identifying the smallest even number in an array of non-negative integers. With no external dependencies, it is easy to integrate into any Python project. Follow the instructions above to install Python and use the function in your applications.