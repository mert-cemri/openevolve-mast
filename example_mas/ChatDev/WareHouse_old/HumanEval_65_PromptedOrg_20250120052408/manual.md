manual.md

```
# Circular Shift Application

This application provides a function to perform a circular shift on the digits of an integer. The function shifts the digits of the integer to the right by a specified number of positions and returns the result as a string. If the shift value is greater than the number of digits in the integer, the function returns the digits in reverse order.

## Main Function

### `circular_shift(x, shift)`

- **Description**: Circularly shifts the digits of the integer `x` to the right by `shift` positions. If `shift` is greater than the number of digits, the digits are reversed.
- **Parameters**:
  - `x` (int): The integer whose digits are to be shifted.
  - `shift` (int): The number of positions to shift the digits.
- **Returns**: A string representing the shifted digits.
- **Examples**:
  - `circular_shift(12, 1)` returns `"21"`
  - `circular_shift(12, 2)` returns `"12"`

## Installation

This application does not require any external dependencies. You can use it directly in your Python environment.

### Quick Install

1. Ensure you have Python installed on your system.
2. Clone or download the repository containing the `main.py` file.

## Usage

1. Open your terminal or command prompt.
2. Navigate to the directory containing the `main.py` file.
3. Run a Python interpreter or script and import the `circular_shift` function from `main.py`.
4. Use the function by passing the desired integer and shift value as arguments.

### Example

```python
from main import circular_shift

result = circular_shift(12345, 2)
print(result)  # Output: "45123"
```

## Documentation

For further details on how the function works, refer to the docstring provided within the `main.py` file. The docstring includes a description of the function, its parameters, return values, and examples of usage.

```