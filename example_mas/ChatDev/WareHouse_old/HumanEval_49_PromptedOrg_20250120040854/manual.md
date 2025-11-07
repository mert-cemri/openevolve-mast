# ModP Function User Manual

## Introduction

The `modp` function is a Python utility designed to compute the result of \(2^n \mod p\). This function is particularly useful in scenarios involving large numbers and modular arithmetic, such as cryptography and number theory.

### Main Functionality

- **modp(n: int, p: int) -> int**: This function takes two integer arguments, `n` and `p`, and returns the result of \(2^n \mod p\).

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

### Environment Setup

This function does not require any external dependencies, making it straightforward to use in any Python environment. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Running the Code

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `modp` function.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run Python Interpreter**: You can test the function directly in the Python interpreter or by creating a script that imports and uses the function.

### Example

To test the function in a Python shell:

```bash
python
```

Then, in the Python shell:

```python
from main import modp

print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
```

## Usage

To use the `modp` function in your own projects, simply import it from the `main.py` file and call it with the desired parameters.

### Example Script

```python
from main import modp

def main():
    n = 1101
    p = 101
    result = modp(n, p)
    print(f"The result of 2^{n} modulo {p} is {result}")

if __name__ == "__main__":
    main()
```

## Conclusion

The `modp` function is a simple yet powerful tool for performing modular exponentiation with a base of 2. Its implementation is efficient and does not require any additional libraries, making it easy to integrate into various Python projects.