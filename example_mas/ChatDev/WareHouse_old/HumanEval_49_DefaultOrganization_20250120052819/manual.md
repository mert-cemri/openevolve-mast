# ModP Function User Manual

Welcome to the ModP Function User Manual. This document will guide you through the installation, usage, and understanding of the ModP function, which is designed to compute \(2^n \mod p\) efficiently using the method of exponentiation by squaring.

## Overview

The ModP function is a Python-based utility that calculates the result of \(2^n \mod p\). This is particularly useful in fields such as cryptography, where modular arithmetic is a common operation.

## Main Function

### `modp(n: int, p: int) -> int`

- **Description**: Computes \(2^n \mod p\) using an efficient algorithm known as exponentiation by squaring.
- **Parameters**:
  - `n` (int): The exponent to which 2 is raised.
  - `p` (int): The modulus.
- **Returns**: The result of \(2^n \mod p\).

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

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository**: 
   - Clone the repository containing the `main.py` file to your local machine.

2. **Set Up Environment**:
   - Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

3. **Install Dependencies**:
   - There are no additional dependencies required for this function. Simply ensure Python is installed.

## How to Use

1. **Navigate to the Directory**:
   - Open a terminal or command prompt and navigate to the directory where `main.py` is located.

2. **Run the Script**:
   - Execute the script using Python. For example:
     ```bash
     python main.py
     ```

3. **Integrate into Your Project**:
   - You can import the `modp` function into your own Python projects by including the `main.py` file and using:
     ```python
     from main import modp
     ```

## Additional Information

- **Efficiency**: The function uses exponentiation by squaring, which is efficient for large values of `n`.
- **Use Cases**: Ideal for applications in cryptography, computer science, and any domain requiring modular arithmetic.

For further assistance or inquiries, please contact our support team. We are committed to helping you make the most out of our software solutions.