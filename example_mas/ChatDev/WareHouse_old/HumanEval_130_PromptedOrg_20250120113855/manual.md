# Tribonacci Sequence Generator

This software module provides a function to generate the Tribonacci sequence, a lesser-known sequence similar to the Fibonacci sequence, but with a unique recurrence relation. The function is implemented in Python and is designed to be simple and efficient.

## Main Functionality

The main function of this software is `tri(n)`, which generates the first `n + 1` numbers of the Tribonacci sequence. The Tribonacci sequence is defined by the following rules:

- `tri(1) = 3`
- `tri(n) = 1 + n / 2`, if `n` is even.
- `tri(n) = tri(n - 1) + tri(n - 2) + tri(n - 3)`, if `n` is odd.

### Example

For example, calling `tri(3)` will return `[1, 3, 2, 8]`.

## Installation

This project does not require any external dependencies, so you can use it directly with a standard Python installation. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Move into the directory where the `main.py` file is located.
   ```bash
   cd <project-directory>
   ```

3. **Run the Code**: You can run the code directly using Python.
   ```bash
   python main.py
   ```

## How to Use

To use the Tribonacci sequence generator, you can import the `tri` function from the `main.py` file into your own Python scripts or interactive sessions.

### Example Usage

```python
from main import tri

# Generate the first 4 numbers of the Tribonacci sequence
sequence = tri(3)
print(sequence)  # Output: [1, 3, 2, 8]
```

## Documentation

The function `tri(n)` is documented within the code. It includes a detailed docstring explaining the parameters and the return value.

- **Parameters**: 
  - `n` (int): A non-negative integer indicating the number of terms to generate.

- **Returns**: 
  - `list`: A list containing the first `n + 1` numbers of the Tribonacci sequence.

## Additional Information

This module is designed for educational purposes and to demonstrate the implementation of a custom sequence generator. It can be extended or modified to suit more complex requirements or integrated into larger projects.

For any questions or support, please contact the development team.