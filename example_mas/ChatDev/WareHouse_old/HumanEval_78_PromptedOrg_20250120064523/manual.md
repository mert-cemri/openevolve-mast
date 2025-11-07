# HexKey User Manual

Welcome to the HexKey software, a simple Python application designed to count the number of prime hexadecimal digits in a given string. This manual will guide you through the installation process, introduce the main function of the software, and provide instructions on how to use it.

## Introduction

HexKey is a Python function that processes a string representing a hexadecimal number and counts the number of digits that are prime numbers. In the context of hexadecimal digits, the prime numbers are 2, 3, 5, 7, B (11 in decimal), and D (13 in decimal).

## Quick Install

HexKey does not require any external dependencies, making it easy to set up and use. You only need Python installed on your system.

### Step 1: Install Python

Ensure that Python is installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

### Step 2: Clone or Download the Repository

You can clone the repository using Git or download the files directly.

To clone the repository, use the following command:
```bash
git clone <repository-url>
```

Alternatively, download the ZIP file from the repository page and extract it to your desired location.

## Main Function

The core functionality of HexKey is provided by the `hex_key` function. This function takes a single argument, a string representing a hexadecimal number, and returns the count of prime hexadecimal digits present in the string.

### Function Signature

```python
def hex_key(num: str) -> int:
```

### Parameters

- `num` (str): A string representing a hexadecimal number. The string may contain digits 0-9 and letters A-F (uppercase).

### Returns

- `int`: The count of prime hexadecimal digits in the input string.

### Examples

- `hex_key("AB")` returns `1`.
- `hex_key("1077E")` returns `2`.
- `hex_key("ABED1A33")` returns `4`.
- `hex_key("123456789ABCDEF0")` returns `6`.
- `hex_key("2020")` returns `2`.

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located.
3. Run the Python interpreter or a script that imports and uses the `hex_key` function.

Example usage in a Python script:

```python
from main import hex_key

# Example usage
result = hex_key("ABED1A33")
print(f"The number of prime hexadecimal digits is: {result}")
```

## Conclusion

HexKey is a straightforward tool for counting prime hexadecimal digits in a string. With no external dependencies, it is easy to set up and use in any Python environment. We hope this manual helps you get started with HexKey and utilize its functionality effectively. If you have any questions or need further assistance, please feel free to reach out.