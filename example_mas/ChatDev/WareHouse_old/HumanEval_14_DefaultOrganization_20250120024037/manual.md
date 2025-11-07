manual.md

```
# All Prefixes Generator

This software provides a simple utility function to generate all prefixes of a given string. It is designed to be lightweight and efficient, requiring no external dependencies.

## Quick Install

Since this software does not require any external dependencies, you can simply download the `main.py` file to your local environment to get started.

## 🤔 What is this?

The All Prefixes Generator is a Python-based utility that allows users to obtain all possible prefixes of a given string, ordered from shortest to longest. This can be particularly useful in applications involving string manipulation, text processing, or any scenario where prefix analysis is required.

### Main Function

- **`all_prefixes(string: str) -> List[str]`**: This function takes a single string as input and returns a list of all prefixes of that string. For example, if the input string is `'abc'`, the function will return `['a', 'ab', 'abc']`.

## 📖 How to Use

1. **Download the Code**: Ensure you have the `main.py` file in your working directory.

2. **Run the Function**: You can use the function by importing it into your Python script or interactive session. Here is an example of how to use it:

    ```python
    from main import all_prefixes

    # Example usage
    prefixes = all_prefixes('abc')
    print(prefixes)  # Output: ['a', 'ab', 'abc']
    ```

3. **Testing**: You can test the function using Python's built-in `doctest` module to ensure it works as expected. Simply run the following command in your terminal:

    ```bash
    python -m doctest main.py
    ```

    This will execute the example provided in the function's docstring and verify its correctness.

## Additional Information

- **No External Dependencies**: This software does not require any additional packages or libraries, making it easy to integrate into existing projects.

- **Lightweight and Efficient**: The function is implemented using a list comprehension, ensuring both readability and performance.

Feel free to reach out if you have any questions or need further assistance with the All Prefixes Generator.
```