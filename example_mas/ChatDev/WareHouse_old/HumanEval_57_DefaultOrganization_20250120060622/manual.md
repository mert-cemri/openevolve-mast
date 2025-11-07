# Monotonic List Checker

This software provides a simple utility function to determine if a list of numbers is monotonically increasing or decreasing. It is implemented in Python and does not require any external dependencies.

## Main Function

The core function of this software is `monotonic(l: list) -> bool`, which checks if the elements of a given list are either monotonically increasing or decreasing.

### Function Definition

```python
def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
```

### How It Works

- **Monotonically Increasing:** A list is considered monotonically increasing if each element is greater than or equal to the previous element.
- **Monotonically Decreasing:** A list is considered monotonically decreasing if each element is less than or equal to the previous element.
- The function returns `True` if the list is either monotonically increasing or decreasing, otherwise it returns `False`.

## Installation

This software does not require any external libraries or dependencies. You only need Python installed on your system.

### Python Installation

Ensure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

## Usage

To use the `monotonic` function, follow these steps:

1. **Clone or Download the Repository:**
   - Clone the repository using Git:
     ```bash
     git clone <repository-url>
     ```
   - Or download the ZIP file and extract it.

2. **Navigate to the Directory:**
   - Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Function:**
   - You can test the function by running the Python script and passing a list to the `monotonic` function.
   - Example usage in a Python shell or script:
     ```python
     from main import monotonic

     print(monotonic([1, 2, 4, 20]))  # Output: True
     print(monotonic([1, 20, 4, 10])) # Output: False
     print(monotonic([4, 1, 0, -10])) # Output: True
     ```

## Documentation

For further details and examples, refer to the docstring provided in the `monotonic` function within the `main.py` file. The examples included demonstrate typical use cases and expected outputs.

Feel free to modify and extend the function as needed for your specific applications.