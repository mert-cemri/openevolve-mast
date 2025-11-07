# Count Distinct Characters

This software provides a simple function to count the number of distinct characters in a given string, regardless of case. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function provided by this software is `count_distinct_characters`. This function takes a string as input and returns the number of distinct characters present in the string, ignoring case differences.

### Function Definition

```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
```

## Installation

Since this software does not require any external dependencies, you can use it directly without installing any additional packages. Simply ensure you have Python installed on your system.

### Python Installation

If you do not have Python installed, you can download and install it from the [official Python website](https://www.python.org/downloads/).

## Usage

To use the `count_distinct_characters` function, follow these steps:

1. **Open a Python Environment**: You can use any Python environment such as IDLE, PyCharm, or a simple command-line interface.

2. **Copy the Function Code**: Copy the function code provided above into your Python environment.

3. **Call the Function**: Use the function by passing a string as an argument. For example:

    ```python
    result = count_distinct_characters('HelloWorld')
    print(result)  # Output will be 7
    ```

4. **Test with Different Inputs**: You can test the function with different strings to see how it counts distinct characters.

### Example Usage

```python
# Example 1
print(count_distinct_characters('xyzXYZ'))  # Output: 3

# Example 2
print(count_distinct_characters('Jerry'))   # Output: 4

# Example 3
print(count_distinct_characters('HelloWorld'))  # Output: 7
```

## Conclusion

This software provides a straightforward way to count distinct characters in a string, ignoring case. It is easy to use and does not require any additional setup beyond having Python installed. Feel free to integrate this function into your projects where you need to analyze the distinct character count of strings.