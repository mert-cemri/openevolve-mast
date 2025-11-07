# ModP User Manual

Welcome to the ModP software, a simple yet efficient Python module designed to compute \(2^n \mod p\) using modular exponentiation. This manual will guide you through the installation process, introduce the main function, and provide instructions on how to use the software.

## Introduction

The ModP module is designed to perform modular exponentiation, which is a fundamental operation in number theory and cryptography. The function `modp` calculates \(2^n \mod p\) efficiently, even for large values of \(n\), by using the method of exponentiation by squaring.

## Quick Install

The ModP module does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Installation Steps

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the ModP module by cloning the repository or downloading the source code files.

3. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

## How to Use

The core functionality of the ModP module is encapsulated in the `modp` function. Below is a guide on how to use this function.

### Function: `modp`

#### Description

The `modp` function computes \(2^n \mod p\) using an efficient algorithm that handles large exponents without overflow.

#### Parameters

- `n` (int): The exponent to which 2 is raised.
- `p` (int): The modulus.

#### Returns

- `int`: The result of \(2^n \mod p\).

#### Examples

Here are some examples of how to use the `modp` function:

```python
# Example 1
result = modp(3, 5)
print(result)  # Output: 3

# Example 2
result = modp(1101, 101)
print(result)  # Output: 2

# Example 3
result = modp(0, 101)
print(result)  # Output: 1

# Example 4
result = modp(3, 11)
print(result)  # Output: 8

# Example 5
result = modp(100, 101)
print(result)  # Output: 1
```

### Running the Code

To execute the function, simply run the `main.py` file in your Python environment. You can modify the examples provided above or create your own to test different values of `n` and `p`.

```bash
python main.py
```

## Conclusion

The ModP module is a lightweight and efficient tool for performing modular exponentiation. With no external dependencies, it is easy to integrate into your projects. We hope this manual helps you get started quickly and effectively. If you have any questions or need further assistance, please feel free to reach out to our support team.