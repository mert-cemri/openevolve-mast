# How Many Times - User Manual

This software provides a simple utility function to count how many times a given substring appears in a string, including overlapping occurrences. This can be particularly useful for text analysis and pattern recognition tasks.

## Main Function

### `how_many_times(string: str, substring: str) -> int`

This function takes two parameters:
- `string`: The original string in which you want to search for the substring.
- `substring`: The substring you want to count within the original string.

The function returns an integer representing the number of times the `substring` appears in the `string`, including overlapping occurrences.

#### Example Usage

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

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone the repository** (if applicable) or download the `main.py` file to your local environment.

3. **Run the function**: You can directly run the function in a Python script or an interactive Python shell.

## How to Use

1. **Open your Python environment**: This could be a terminal, command prompt, or an IDE like PyCharm or VSCode.

2. **Load the function**: If you have the `main.py` file, you can import the function into your script or interactive session.

   ```python
   from main import how_many_times
   ```

3. **Call the function**: Provide the `string` and `substring` as arguments to the function.

   ```python
   result = how_many_times('aaaa', 'aa')
   print(result)  # Output: 3
   ```

## Documentation

For further details, you can refer to the docstring within the `main.py` file, which provides examples and a brief description of the function's behavior.

This software is designed to be simple and efficient, focusing solely on the task of counting substring occurrences, including overlaps, without any additional features or dependencies.