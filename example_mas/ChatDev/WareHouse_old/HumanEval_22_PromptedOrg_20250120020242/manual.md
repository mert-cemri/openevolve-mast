# Filter Integers

This software module provides a simple utility function to filter integers from a list containing various Python data types.

## Main Functionality

The primary function of this module is `filter_integers`, which takes a list of any Python values and returns a new list containing only the integer values from the original list.

### Function: `filter_integers`

- **Input**: A list of values of any data type (`List[Any]`).
- **Output**: A list of integers (`List[int]`).

#### Example Usage

```python
from main import filter_integers

# Example 1
result1 = filter_integers(['a', 3.14, 5])
print(result1)  # Output: [5]

# Example 2
result2 = filter_integers([1, 2, 3, 'abc', {}, []])
print(result2)  # Output: [1, 2, 3]
```

## Installation

This module does not require any external dependencies beyond the standard Python library. Therefore, no additional installation steps are necessary.

### Quick Start

1. **Clone the Repository**: Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Move into the directory containing the `main.py` file.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can directly run the Python script or import the function into your own scripts.

   ```bash
   python main.py
   ```

## How to Use

- Import the `filter_integers` function from the `main.py` file.
- Pass a list of mixed data types to the function.
- The function will return a list containing only the integer values.

## Documentation

For further information and examples, refer to the docstring within the `main.py` file. The docstring provides inline documentation and examples of how to use the `filter_integers` function effectively.

This module is designed to be simple and efficient, making it easy to integrate into larger projects where filtering integer values from a list is required.