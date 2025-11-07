# Search Function User Manual

## Introduction

The `search` function is a Python utility designed to analyze a list of positive integers and return the greatest integer that meets specific criteria. Specifically, the function identifies the largest integer in the list whose frequency (the number of times it appears) is greater than or equal to the integer itself. If no such integer exists, the function returns -1.

## Main Functionality

- **Function Name**: `search`
- **Input**: A non-empty list of positive integers.
- **Output**: The greatest integer that has a frequency greater than or equal to its value, or -1 if no such integer exists.

### Examples

- `search([4, 1, 2, 2, 3, 1])` returns `2`.
- `search([1, 2, 2, 3, 3, 3, 4, 4, 4])` returns `3`.
- `search([5, 5, 4, 4, 4])` returns `-1`.

## Installation

The `search` function does not require any external dependencies beyond Python's standard library. Therefore, no additional installation steps are necessary.

### Requirements

- Python 3.x

## Usage

To use the `search` function, follow these steps:

1. **Ensure Python is installed**: Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Create a Python script**: Create a new Python file (e.g., `main.py`) and include the `search` function code provided.

3. **Call the function**: Use the `search` function by passing a list of positive integers as an argument. For example:

    ```python
    def search(lst):
        from collections import Counter
        frequency = Counter(lst)
        result = -1
        for num, freq in frequency.items():
            if freq >= num:
                result = max(result, num)
        return result

    # Example usage
    result = search([4, 1, 2, 2, 3, 1])
    print(result)  # Output: 2
    ```

4. **Run the script**: Execute the script using a Python interpreter to see the results.

## Conclusion

The `search` function is a simple yet powerful tool for analyzing lists of integers based on their frequency. By following the instructions in this manual, you can easily integrate and use this function in your Python projects. If you have any questions or need further assistance, please feel free to reach out.