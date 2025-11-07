manual.md

```
# How Many Times Function

This software provides a simple Python function to determine how many times a given substring appears in a string, including overlapping occurrences. It is designed to be straightforward and efficient, making it easy to integrate into larger projects or use as a standalone utility.

## Main Functionality

The core functionality of this software is encapsulated in the `how_many_times` function. This function takes two string inputs: the main string and the substring to search for. It returns an integer representing the number of times the substring appears in the main string, counting overlapping occurrences.

### Function Signature

```python
def how_many_times(string: str, substring: str) -> int:
```

### Example Usage

```python
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from the [official website](https://www.python.org/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `how_many_times` function.

3. **Run the function**: You can execute the function directly in a Python environment or integrate it into your existing Python projects.

## How to Use

1. **Open your Python environment**: This could be a Python shell, a script file, or an integrated development environment (IDE) like PyCharm or VSCode.

2. **Import the function**: If you have saved the `main.py` file in your project, you can import the function using:
   ```python
   from main import how_many_times
   ```

3. **Call the function**: Use the function by passing the required parameters:
   ```python
   result = how_many_times('your_string_here', 'your_substring_here')
   print(result)
   ```

4. **Interpret the result**: The function will return an integer indicating the number of times the substring appears in the main string, including overlaps.

## Additional Information

- **No External Libraries**: This function is implemented using Python's built-in capabilities, ensuring compatibility and ease of use without additional installations.

- **Efficiency**: The function is designed to efficiently handle overlapping substrings, making it suitable for a variety of applications.

Feel free to integrate this function into your projects or modify it to suit your specific needs. If you encounter any issues or have suggestions for improvements, please reach out to our support team.
```