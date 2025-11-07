# Monotonic List Checker

This software provides a simple utility function to check if a list of numbers is monotonically increasing or decreasing. It is implemented in Python and does not require any external dependencies.

## Main Function

### `monotonic(l: list) -> bool`

This function takes a list of numbers as input and returns a boolean value indicating whether the list is monotonically increasing or decreasing.

- **Parameters:**
  - `l` (list): A list of numbers to be checked.

- **Returns:**
  - `bool`: `True` if the list is monotonically increasing or decreasing, `False` otherwise.

- **Examples:**
  ```python
  >>> monotonic([1, 2, 4, 20])
  True
  >>> monotonic([1, 20, 4, 10])
  False
  >>> monotonic([4, 1, 0, -10])
  True
  ```

## Installation

Since this software does not require any external libraries, you only need to have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

## Usage

1. **Clone the Repository:**
   - Clone the repository to your local machine using the following command:
     ```bash
     git clone <repository-url>
     ```

2. **Navigate to the Directory:**
   - Change into the directory where the `main.py` file is located:
     ```bash
     cd <repository-directory>
     ```

3. **Run the Script:**
   - You can run the script directly using Python to test the `monotonic` function:
     ```bash
     python main.py
     ```

4. **Using the Function:**
   - You can import the `monotonic` function into your own Python scripts and use it as needed:
     ```python
     from main import monotonic

     result = monotonic([1, 2, 3, 4])
     print(result)  # Output: True
     ```

## Documentation

For further details on how the function works, refer to the docstring provided in the `main.py` file. The function is designed to be straightforward and easy to integrate into larger projects where list monotonicity needs to be checked.