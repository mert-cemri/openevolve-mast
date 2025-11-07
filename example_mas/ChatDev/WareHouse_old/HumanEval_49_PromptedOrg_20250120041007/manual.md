# ModP Function User Manual

This user manual provides detailed instructions on how to use the `modp` function, which calculates \(2^n \mod p\) using the method of exponentiation by squaring. This function is implemented in Python and does not require any external dependencies.

## Introduction

The `modp` function is designed to compute the result of \(2^n \mod p\) efficiently, even for large values of \(n\). This is achieved through the use of exponentiation by squaring, which reduces the number of multiplications needed compared to the naive approach.

## Main Functionality

- **Function Name:** `modp`
- **Parameters:**
  - `n` (int): The exponent to which 2 is raised.
  - `p` (int): The modulus.
- **Returns:** The result of \(2^n \mod p\).

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

### Environment Setup

Since the `modp` function does not require any external libraries, setting up the environment is straightforward. You only need to have Python installed on your system.

### Installing Python

If Python is not already installed on your system, you can download and install it from the official Python website: [python.org](https://www.python.org/).

### Verifying Python Installation

After installing Python, you can verify the installation by running the following command in your terminal or command prompt:

```bash
python --version
```

This should display the version of Python installed on your system.

## How to Use

1. **Create a Python File:**

   Create a new Python file, e.g., `main.py`, and copy the `modp` function implementation into this file.

2. **Run the Function:**

   You can call the `modp` function with the desired values of `n` and `p` to compute \(2^n \mod p\).

3. **Execute the Script:**

   Run the script using the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

   This will execute the script and display the results of the `modp` function calls.

## Conclusion

The `modp` function is a simple yet powerful tool for computing \(2^n \mod p\) efficiently. With no external dependencies required, it is easy to integrate into any Python project. By following this manual, you should be able to set up your environment and use the function effectively.