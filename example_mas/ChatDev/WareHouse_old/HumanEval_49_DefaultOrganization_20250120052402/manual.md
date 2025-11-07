manual.md

```
# ModP Calculator

A simple Python module to compute \(2^n \mod p\) using efficient modular exponentiation.

## Overview

The ModP Calculator is a lightweight Python module designed to calculate the result of \(2^n \mod p\) efficiently. This is particularly useful in fields such as cryptography and number theory where modular arithmetic is frequently used.

## Main Function

The core function of this module is `modp(n: int, p: int) -> int`, which computes \(2^n \mod p\). The function is implemented using an efficient algorithm known as modular exponentiation, which reduces the computational complexity compared to naive methods.

### Function Signature

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p using efficient modular exponentiation.
    """
```

### Example Usage

```python
print(modp(3, 5))    # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))  # Output: 1
```

## Installation

This module does not require any external dependencies, making it easy to integrate into any Python project.

### Quick Install

To use the ModP Calculator, simply download the `main.py` file and include it in your project directory. You can then import the `modp` function into your Python scripts.

```bash
# No installation of external packages is required
```

## How to Use

1. **Download the `main.py` file**: Ensure that the `main.py` file is in your project directory.

2. **Import the function**: In your Python script, import the `modp` function.

    ```python
    from main import modp
    ```

3. **Call the function**: Use the `modp` function by passing the desired values of `n` and `p`.

    ```python
    result = modp(3, 5)
    print(result)  # Output: 3
    ```

## Documentation

For further details on how the function works, please refer to the docstring provided in the `main.py` file. The function is well-documented with examples to guide you through its usage.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to help you with any inquiries or technical support you may need.

```