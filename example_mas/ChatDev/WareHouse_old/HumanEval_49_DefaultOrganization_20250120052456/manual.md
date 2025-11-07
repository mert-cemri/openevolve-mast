# ModP Function User Manual

Welcome to the ModP Function User Manual. This document provides a comprehensive guide on how to use the `modp` function, which calculates \(2^n \mod p\) using efficient exponentiation by squaring.

## Introduction

The `modp` function is designed to compute the result of \(2^n \mod p\) efficiently. This is particularly useful in cryptographic applications and scenarios where large powers of numbers are involved.

### Main Functionality

- **modp(n: int, p: int) -> int**: This function takes two integer parameters, `n` and `p`, and returns the result of \(2^n \mod p\).

### Example Usage

```python
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
```

## Installation

This project does not require any external dependencies. It is implemented purely in Python, making it easy to integrate into any Python environment.

### Quick Start

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: 

   ```bash
   cd <project-directory>
   ```

3. **Run the Python Script**: You can directly run the `main.py` file to test the function.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you are integrating this function into another project, import it as follows:

   ```python
   from main import modp
   ```

2. **Call the Function**: Use the function by passing the desired values of `n` and `p`.

   ```python
   result = modp(10, 7)
   print(result)  # Output will be the result of 2^10 % 7
   ```

## Documentation

For further details on the implementation and the algorithm used, please refer to the comments within the `main.py` file. The function uses the method of exponentiation by squaring, which is efficient for computing large powers modulo a number.

## Support

For any issues or questions regarding the usage of this function, please contact the development team at ChatDev. We are committed to providing support and ensuring the functionality meets your needs.

Thank you for using the ModP function!