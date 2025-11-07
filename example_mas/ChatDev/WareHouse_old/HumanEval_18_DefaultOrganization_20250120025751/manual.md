manual.md

```
# How Many Times

A Python application to count the number of times a given substring can be found in the original string, including overlapping occurrences.

## Quick Install

This application does not have any external dependencies, so you can directly use it with Python installed on your system.

## 🤔 What is this?

The `how_many_times` function is designed to find how many times a given substring appears in a string, including overlapping cases. This can be useful in text analysis, data processing, and other applications where pattern matching is required.

### Main Function

- **how_many_times(string: str, substring: str) -> int**: This function takes two parameters:
  - `string`: The original string in which to search for the substring.
  - `substring`: The substring to search for within the original string.

  It returns an integer representing the number of times the substring is found in the string, counting overlapping occurrences.

### Example Usage

```python
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
```

## 📖 Documentation

### Getting Started

1. **Installation**: Ensure you have Python installed on your system. No additional packages are required.

2. **Usage**: You can use the function by importing it into your Python script or by running it directly in a Python interpreter.

### How-To Examples

- **Basic Example**: To find how many times 'a' appears in 'aaa', including overlaps:
  ```python
  result = how_many_times('aaa', 'a')
  print(result)  # Output: 3
  ```

- **Overlapping Example**: To find how many times 'aa' appears in 'aaaa', including overlaps:
  ```python
  result = how_many_times('aaaa', 'aa')
  print(result)  # Output: 3
  ```

This function is simple yet powerful for text processing tasks where pattern matching is required. Feel free to integrate it into larger applications or use it for standalone tasks.
```