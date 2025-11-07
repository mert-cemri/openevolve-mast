# Sum to N Function

This software provides a simple Python function `sum_to_n` that calculates the sum of all integers from 1 to a given number `n`. It is a straightforward utility function that can be used in various applications where such a calculation is needed.

## Main Function

### `sum_to_n(n: int) -> int`

- **Description**: This function takes an integer `n` as input and returns the sum of all integers from 1 to `n`.
- **Usage**:
  ```python
  result = sum_to_n(10)
  print(result)  # Output: 55
  ```
- **Examples**:
  - `sum_to_n(30)` returns `465`
  - `sum_to_n(100)` returns `5050`
  - `sum_to_n(5)` returns `15`
  - `sum_to_n(10)` returns `55`
  - `sum_to_n(1)` returns `1`

## Installation

This software does not have any external dependencies, so you do not need to install any additional packages. It is implemented purely in Python and can be run in any standard Python environment.

## How to Use

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Code**: You can run the code directly in a Python environment. Open a Python shell or script and import the function:
   ```python
   from main import sum_to_n

   # Example usage
   print(sum_to_n(10))  # Output: 55
   ```

4. **Testing**: You can test the function using the provided examples in the docstring. Simply call the function with different values of `n` to verify its correctness.

## Additional Information

- **Python Version**: Ensure you have Python installed on your system. The function is compatible with Python 3.x.
- **No External Libraries**: This function does not require any external libraries or dependencies.

This utility is designed to be simple and efficient, making it easy to integrate into larger projects where summing a sequence of numbers is required.