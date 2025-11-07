# modp Function User Manual

## Introduction

The `modp` function is a Python utility designed to compute the result of \(2^n \mod p\) using efficient modular exponentiation. This function is particularly useful in scenarios where you need to handle large exponents and require the result modulo a given number.

## Main Functionality

The primary function provided by this software is:

- `modp(n: int, p: int) -> int`: Computes \(2^n \mod p\).

### Example Usage

```python
result = modp(3, 5)
print(result)  # Output: 3

result = modp(1101, 101)
print(result)  # Output: 2

result = modp(0, 101)
print(result)  # Output: 1

result = modp(3, 11)
print(result)  # Output: 8

result = modp(100, 101)
print(result)  # Output: 1
```

## Installation

This project does not require any external dependencies, making it straightforward to set up and run. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine. Alternatively, you can directly copy the code into a Python file.

3. **Run the Code**: Save the code in a file named `main.py` and execute it using Python.

```bash
python main.py
```

## How to Use

1. **Import the Function**: If you have saved the function in a module, you can import it into your Python script.

   ```python
   from main import modp
   ```

2. **Call the Function**: Use the `modp` function by passing the desired values of `n` and `p`.

   ```python
   result = modp(n, p)
   print(result)
   ```

3. **Test with Examples**: You can test the function with various inputs to ensure it behaves as expected.

## Documentation

For further details on the implementation and examples, refer to the docstring within the `modp` function in the `main.py` file. The docstring provides example usages and expected outputs for different inputs.

## Support

For any issues or questions regarding the usage of the `modp` function, please contact our support team or refer to the documentation provided within the code.