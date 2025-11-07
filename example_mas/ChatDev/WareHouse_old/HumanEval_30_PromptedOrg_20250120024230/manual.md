# Positive Number Filter

This software module provides a simple function to filter and return only positive numbers from a given list. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function provided by this software is `get_positive`, which takes a list of numbers as input and returns a new list containing only the positive numbers from the original list.

### Function Signature

```python
def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
```

### Example Usage

```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]

>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

## Installation

This module does not require any external libraries or dependencies. It is implemented using standard Python libraries, so you only need Python installed on your system to use it.

### Quick Install

Ensure you have Python installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

## How to Use

1. **Clone or Download the Repository:**
   - You can clone the repository using Git or download the ZIP file and extract it to your desired location.

2. **Navigate to the Directory:**
   - Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Python Script:**
   - You can test the function by running the Python script in an interactive Python shell or by writing a script that imports and uses the `get_positive` function.

4. **Example Script:**

   ```python
   from main import get_positive

   numbers = [-1, 2, -4, 5, 6]
   positive_numbers = get_positive(numbers)
   print(positive_numbers)  # Output: [2, 5, 6]
   ```

## Documentation

For further details on the function and its usage, refer to the docstring provided within the `main.py` file. The docstring includes example usages and expected outputs.

This module is designed to be simple and straightforward, making it easy to integrate into larger projects or use as a standalone utility for filtering positive numbers from a list.