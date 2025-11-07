# Common Elements Finder

This software provides a simple utility function to find and return sorted unique common elements from two lists. It is designed to be lightweight and easy to use, with no external dependencies required.

## Main Functionality

The primary function of this software is:

- **common(l1: list, l2: list) -> list**: This function takes two lists as input and returns a sorted list of unique elements that are common to both lists.

### Example Usage

```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]

>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

## Installation

This software does not require any external libraries or dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the `main.py` file is located.

   ```bash
   cd <directory-name>
   ```

3. **Run the Code**: You can directly run the Python script using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you want to use the `common` function in your own scripts, you can import it from the `main.py` file.

   ```python
   from main import common
   ```

2. **Call the Function**: Pass two lists as arguments to the `common` function to get the sorted list of unique common elements.

   ```python
   result = common([1, 2, 3], [2, 3, 4])
   print(result)  # Output: [2, 3]
   ```

## Documentation

For further details on how the function works, refer to the docstring provided in the `main.py` file. The docstring includes example usage and expected output.

This software is designed to be straightforward and efficient, making it a handy tool for quickly finding common elements between two lists.