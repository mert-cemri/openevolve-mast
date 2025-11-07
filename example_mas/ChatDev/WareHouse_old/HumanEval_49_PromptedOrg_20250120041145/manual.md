# ModP Function User Manual

## Introduction

The `modp` function is a simple yet powerful utility designed to compute the result of \(2^n \mod p\). This function is particularly useful in scenarios involving large numbers and modular arithmetic, such as cryptography and number theory.

### Main Functionality

- **modp(n: int, p: int) -> int**: This function takes two integer inputs, `n` and `p`, and returns the result of \(2^n \mod p\).

### Example Usage

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

## Installation

### Environment Setup

The `modp` function does not require any external dependencies, making it straightforward to integrate into any Python environment. Ensure you have Python installed on your system.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python scripts. Simply copy the function definition into your Python file.

## How to Use

1. **Copy the Function**: Copy the `modp` function definition into your Python script or interactive environment.

2. **Call the Function**: Use the function by passing the desired values of `n` and `p` as arguments.

3. **View the Result**: The function will return the result of \(2^n \mod p\), which you can print or use in further calculations.

## Additional Information

The `modp` function leverages Python's built-in `pow` function, which efficiently computes large powers with a modulus. This ensures that the function is both fast and capable of handling very large values of `n`.

For any questions or further assistance, please feel free to reach out to our support team. We are here to help you make the most of this utility in your projects.