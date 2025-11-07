# ModP Software User Manual

Welcome to the ModP software, a simple yet powerful tool for computing the result of \(2^n \mod p\). This software is designed to efficiently handle large numbers using modular exponentiation, ensuring accurate results even with high values of \(n\).

## Main Functionality

The core function of this software is `modp`, which calculates \(2^n \mod p\). This function is particularly useful in fields such as cryptography, number theory, and computer science where modular arithmetic is frequently applied.

### Function Signature

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.
    """
```

### Example Usage

Here are some examples of how the `modp` function works:

- `modp(3, 5)` returns `3`
- `modp(1101, 101)` returns `2`
- `modp(0, 101)` returns `1`
- `modp(3, 11)` returns `8`
- `modp(100, 101)` returns `1`

## Installation

To use the ModP software, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly run it with Python.

### Quick Install

1. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `modp` function.

3. **Run the script**: You can execute the script using Python by navigating to the directory containing `main.py` and running:

   ```bash
   python main.py
   ```

## How to Use

1. **Open your terminal or command prompt**.

2. **Navigate to the directory containing `main.py`**.

3. **Run Python interactive mode**:

   ```bash
   python
   ```

4. **Import the function**:

   ```python
   from main import modp
   ```

5. **Call the function with desired parameters**:

   ```python
   result = modp(3, 5)
   print(result)  # Output: 3
   ```

## Documentation

The `modp` function is implemented using modular exponentiation, which is an efficient method for computing large powers modulo a number. This method reduces the computational complexity significantly, making it feasible to work with large numbers.

For further details on modular arithmetic and its applications, you may refer to resources in number theory and cryptography.

Thank you for using ModP software. We hope it meets your computational needs effectively!