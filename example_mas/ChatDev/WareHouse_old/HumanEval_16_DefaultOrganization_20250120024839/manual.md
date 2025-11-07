manual.md

```
# Distinct Character Counter

This software provides a simple utility function to count the number of distinct characters in a given string, ignoring case sensitivity. It is implemented in Python and is designed to be straightforward and efficient.

## Main Functionality

The core functionality of this software is encapsulated in the `count_distinct_characters` function. This function takes a string as input and returns the number of distinct characters present in the string, treating uppercase and lowercase versions of a character as the same.

### Function Definition

```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) it consists of.
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
```

### How It Works

1. **Case Insensitivity**: The function converts the input string to lowercase to ensure that character case does not affect the count of distinct characters.
2. **Distinct Character Counting**: It uses a set to store characters, as sets inherently do not allow duplicate entries, thus automatically filtering out duplicates.
3. **Result**: The length of the set, which represents the number of distinct characters, is returned.

## Installation

To use this software, you need to have Python installed on your system. The function does not require any external libraries, so there are no additional dependencies to install.

### Steps to Install Python

1. **Download Python**: Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python.
2. **Install Python**: Run the installer and follow the instructions. Make sure to check the option to add Python to your system PATH during installation.

## Usage

Once Python is installed, you can use the `count_distinct_characters` function by following these steps:

1. **Create a Python Script**: Open a text editor and create a new file named `main.py`.
2. **Copy the Function**: Copy the function definition provided above into your `main.py` file.
3. **Run the Script**: Open a terminal or command prompt, navigate to the directory containing `main.py`, and run the script using the command:
   ```bash
   python main.py
   ```
4. **Test the Function**: You can test the function by calling it with different strings and printing the results. For example:
   ```python
   print(count_distinct_characters('xyzXYZ'))  # Output: 3
   print(count_distinct_characters('Jerry'))   # Output: 4
   ```

## Conclusion

This software provides a simple yet effective way to count distinct characters in a string, ignoring case differences. It is easy to integrate into larger projects or use as a standalone utility for text processing tasks.
```