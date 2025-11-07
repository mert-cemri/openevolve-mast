# How Many Times

This software module provides a function to count the number of times a given substring appears in a string, including overlapping occurrences. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function provided by this module is `how_many_times(string: str, substring: str) -> int`. This function takes two arguments:

- `string`: The original string in which you want to search for the substring.
- `substring`: The substring you want to count within the original string.

The function returns an integer representing the number of times the substring appears in the string, including overlapping occurrences.

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

This module does not require any external dependencies, so you can use it directly in your Python environment. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file from the repository where this module is hosted.

2. **Run the Function**: You can use the function by importing it into your Python script or interactive session. Here is an example of how to use it:

    ```python
    from main import how_many_times

    result = how_many_times('aaaa', 'aa')
    print(result)  # Output: 3
    ```

3. **Testing**: You can test the function with different strings and substrings to ensure it works as expected.

## Documentation

For further details on the implementation and usage of the function, please refer to the docstring provided within the `main.py` file. The docstring includes example usage and expected outputs for various input cases.

This module is designed to be simple and efficient, providing a straightforward solution for counting overlapping substrings in a string.