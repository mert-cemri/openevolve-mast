manual.md

```
# How Many Times

This software provides a simple utility function to count the number of times a given substring appears in a string, including overlapping occurrences. It is implemented in Python and is designed to be straightforward and efficient.

## Main Function

The main function provided by this software is `how_many_times`, which takes two string arguments:

- `string`: The original string in which you want to search for the substring.
- `substring`: The substring you want to count within the original string.

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

To use this software, you need to have Python installed on your system. The function does not require any additional dependencies, so you can directly use it in your Python environment.

### Quick Install

1. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the function.

3. **Run the function**: You can use the function in your Python scripts or interactive shell.

## How to Use

1. **Import the function**: If you have the `main.py` file in your working directory, you can import the function using:

   ```python
   from main import how_many_times
   ```

2. **Call the function**: Use the function by passing the required arguments:

   ```python
   result = how_many_times('your_string_here', 'your_substring_here')
   print(result)
   ```

This utility is particularly useful for text processing tasks where counting overlapping occurrences of substrings is necessary.

## Documentation

For further information and examples, refer to the docstring within the `main.py` file. The docstring provides examples and a brief explanation of the function's behavior.

Feel free to modify and integrate this function into your projects as needed.
```