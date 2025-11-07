# All Prefixes Function

This software module provides a simple function to generate all prefixes of a given string. It is designed to be lightweight and does not require any external dependencies.

## Quick Install

Since this module does not require any external libraries, you can use it directly in your Python environment. Ensure you have Python installed on your system.

## 🤔 What is this?

The `all_prefixes` function is a utility that returns a list of all prefixes of a given string, ordered from shortest to longest. This can be useful in various applications such as text processing, autocomplete features, and more.

### Main Function

- **`all_prefixes(string: str) -> List[str]`**

  This function takes a single string as input and returns a list of its prefixes. For example, given the input `'abc'`, it will return `['a', 'ab', 'abc']`.

## 📖 Usage

To use the `all_prefixes` function, follow these steps:

1. **Create a Python file** (e.g., `main.py`) and include the following code:

    ```python
    from typing import List

    def all_prefixes(string: str) -> List[str]:
        """ Return list of all prefixes from shortest to longest of the input string
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
        """
        return [string[:i] for i in range(1, len(string) + 1)]
    ```

2. **Call the function** with the desired string:

    ```python
    prefixes = all_prefixes('example')
    print(prefixes)  # Output: ['e', 'ex', 'exa', 'exam', 'examp', 'exampl', 'example']
    ```

## Requirements

This module does not require any external dependencies. It uses only standard Python libraries.

## Conclusion

The `all_prefixes` function is a simple yet powerful tool for generating string prefixes. It is easy to integrate into any Python project and can be used in a variety of applications. Enjoy using this utility in your projects!