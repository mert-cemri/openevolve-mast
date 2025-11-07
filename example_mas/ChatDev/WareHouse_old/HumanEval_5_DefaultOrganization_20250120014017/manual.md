# Intersperse Function User Manual

## Introduction

The `intersperse` function is a simple Python utility designed to insert a specified delimiter between every two consecutive elements of a list of integers. This function can be particularly useful in scenarios where you need to format or manipulate lists by adding separators.

## Main Function

### intersperse(numbers: List[int], delimiter: int) -> List[int]

- **Description**: This function takes a list of integers and a delimiter integer as input. It returns a new list where the delimiter is inserted between every two consecutive elements of the input list.

- **Parameters**:
  - `numbers`: A list of integers that you want to intersperse with the delimiter.
  - `delimiter`: An integer that will be inserted between every two consecutive elements of the `numbers` list.

- **Returns**: A new list of integers with the delimiter inserted between every two consecutive elements.

- **Example Usage**:
  ```python
  >>> intersperse([], 4)
  []
  >>> intersperse([1, 2, 3], 4)
  [1, 4, 2, 4, 3]
  ```

## Installation

To use the `intersperse` function, you need to have Python installed on your system. The function does not require any additional dependencies, so you can directly use it in your Python environment.

### Quick Install

1. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `intersperse` function.

3. **Run the function**: You can execute the function in any Python environment by importing it from the `main.py` file.

## Usage

1. **Open your Python environment**: This could be a Python shell, Jupyter Notebook, or any Python IDE.

2. **Import the function**:
   ```python
   from main import intersperse
   ```

3. **Call the function with your desired inputs**:
   ```python
   result = intersperse([1, 2, 3], 4)
   print(result)  # Output: [1, 4, 2, 4, 3]
   ```

## Documentation

For further details on how to use Python and its libraries, please refer to the official [Python documentation](https://docs.python.org/3/).

This manual provides a comprehensive guide to using the `intersperse` function effectively. If you encounter any issues or have questions, feel free to reach out for support.