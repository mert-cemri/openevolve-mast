# Filter by Prefix

This software module provides a simple utility function to filter a list of strings by a given prefix. It is designed to be lightweight and efficient, requiring no external dependencies.

## Quick Install

Since this module does not require any external libraries, you can use it directly in your Python environment. Ensure you have Python installed on your system.

## 🤔 What is this?

The `filter_by_prefix` function is a utility that allows you to filter an input list of strings, returning only those strings that start with a specified prefix. This can be particularly useful in applications where you need to process or analyze data based on specific starting patterns.

### Main Function

- **`filter_by_prefix(strings: List[str], prefix: str) -> List[str]`**

  This function takes two arguments:
  - `strings`: A list of strings that you want to filter.
  - `prefix`: The prefix string to filter the list by.

  **Returns**: A list of strings from the input list that start with the specified prefix.

  **Example Usage**:
  ```python
  from main import filter_by_prefix

  result = filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
  print(result)  # Output: ['abc', 'array']
  ```

## 📖 Documentation

### Getting Started

1. **Installation**: No installation of external packages is required. Ensure you have Python installed on your machine.

2. **Usage**: You can directly use the `filter_by_prefix` function in your Python scripts. Simply import the function from the `main.py` file and call it with your desired list and prefix.

### How-To Examples

- **Filtering an Empty List**:
  ```python
  result = filter_by_prefix([], 'a')
  print(result)  # Output: []
  ```

- **Filtering with a Non-Matching Prefix**:
  ```python
  result = filter_by_prefix(['abc', 'bcd', 'cde'], 'z')
  print(result)  # Output: []
  ```

- **Filtering with a Matching Prefix**:
  ```python
  result = filter_by_prefix(['apple', 'banana', 'apricot', 'berry'], 'ap')
  print(result)  # Output: ['apple', 'apricot']
  ```

This module is designed to be simple and efficient, making it easy to integrate into larger projects or use for quick data processing tasks.