# Tribonacci Sequence Calculator

This software module provides a function to calculate the first `n + 1` numbers of a custom Tribonacci sequence based on specified rules. The Tribonacci sequence is a variation of the Fibonacci sequence with unique recurrence relations.

## Main Function

### `tri(n)`

- **Description**: This function calculates the first `n + 1` numbers of a custom Tribonacci sequence.
- **Parameters**: 
  - `n` (int): A non-negative integer representing the number of terms to calculate.
- **Returns**: 
  - `list`: A list containing the first `n + 1` numbers of the Tribonacci sequence.

The sequence is defined as follows:
- `tri(1) = 3`
- `tri(n) = 1 + n / 2`, if `n` is even
- `tri(n) = tri(n - 1) + tri(n - 2) + tri(n - 3)`, if `n` is odd

### Example Usage

```python
# Example usage of the tri function
print(tri(3))  # Output should be [1, 3, 2, 8]
```

## Installation

This module does not require any external dependencies beyond a standard Python environment. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the script**:
   - You can directly run the `main.py` file using Python:
     ```bash
     python main.py
     ```

## How to Use

1. **Import the Function**: If you want to use the `tri` function in another script, you can import it as follows:
   ```python
   from main import tri
   ```

2. **Call the Function**: Use the `tri` function by passing a non-negative integer `n` to get the first `n + 1` numbers of the Tribonacci sequence.
   ```python
   result = tri(5)
   print(result)  # This will print the first 6 numbers of the Tribonacci sequence
   ```

## Documentation

For further details and documentation, please refer to the comments within the `main.py` file, which explain the logic and implementation of the `tri` function.

This user manual provides all necessary information to understand, install, and use the Tribonacci sequence calculator effectively.