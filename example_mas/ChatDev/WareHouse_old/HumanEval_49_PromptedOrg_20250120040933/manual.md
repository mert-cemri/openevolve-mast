# ModP Function User Manual

## Introduction

The `modp` function is a simple Python utility designed to compute the result of \(2^n \mod p\). This function is particularly useful in scenarios involving modular arithmetic, such as cryptography and number theory.

## Main Functionality

The primary function provided by this software is:

- `modp(n: int, p: int) -> int`: This function takes two integer arguments, `n` and `p`, and returns the result of \(2^n \mod p\).

### Example Usage

```python
result = modp(3, 5)
print(result)  # Output: 3
```

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

### Quick Install

1. **Clone the Repository**: If the code is hosted on a version control system like GitHub, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can directly run the `main.py` file using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you are using this function in another Python script, ensure you import it correctly.

   ```python
   from main import modp
   ```

2. **Call the Function**: Use the function by passing the required parameters.

   ```python
   result = modp(1101, 101)
   print(result)  # Output: 2
   ```

## Documentation

The function is documented with examples in the docstring. You can view these examples by inspecting the function in your preferred Python IDE or text editor.

## Support

For any issues or questions regarding the usage of this software, please contact our support team at support@chatdev.com.

## License

This software is provided under the MIT License. Please refer to the LICENSE file for more details.