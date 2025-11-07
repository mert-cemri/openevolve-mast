manual.md

```
# Truncate Number Application

This application provides a simple utility function to extract the decimal part of a given positive floating point number. The function is designed to be straightforward and efficient, making it a useful tool for various numerical computations where only the fractional part of a number is needed.

## Main Functionality

The core functionality of this application is encapsulated in the `truncate_number` function. This function takes a single argument, a positive floating point number, and returns the decimal part of that number. For example, if the input is `3.5`, the function will return `0.5`.

### Function Definition

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
```

## Installation

This application does not require any external dependencies, making it easy to set up and use. Simply ensure that you have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed:**
   - You can download and install Python from the official website: [Python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository:**
   - You can clone the repository using Git or download the source code directly.

3. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

## Usage

To use the `truncate_number` function, you can run the `main.py` file directly or import the function into your own Python scripts.

### Running Directly

1. Open a terminal or command prompt.
2. Navigate to the directory containing `main.py`.
3. Run the script using Python:

   ```bash
   python main.py
   ```

   This will execute the example usage within the script, printing the decimal part of `3.5`, which is `0.5`.

### Importing into Other Scripts

You can also import the `truncate_number` function into your own Python scripts:

```python
from main import truncate_number

# Example usage
result = truncate_number(7.25)
print(result)  # Output will be 0.25
```

## Conclusion

This application provides a simple yet effective way to extract the decimal part of a floating point number. With no external dependencies, it is easy to integrate into existing projects or use as a standalone utility. Enjoy using the `truncate_number` function for your numerical computations!
```