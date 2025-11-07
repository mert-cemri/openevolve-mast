# Prime Factorization Software

This software provides a simple utility to factorize an integer into its prime factors. The prime factors are returned in a list, ordered from smallest to largest, with each factor appearing as many times as it divides the number.

## Main Functionality

The main function of this software is:

- **factorize(n: int) -> List[int]**: This function takes an integer `n` as input and returns a list of its prime factors. Each factor is listed the number of times it appears in the factorization of `n`.

### Example Usage

```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```

## Installation

This software does not require any external dependencies beyond the standard Python library. To use the software, ensure you have Python installed on your system.

### Steps to Install

1. **Install Python**: If you do not have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone or download the repository containing the `main.py` file to your local machine.

3. **Run the Software**: Navigate to the directory containing `main.py` and run the script using Python.

```bash
python main.py
```

## How to Use

1. **Open a Python Environment**: You can use any Python environment such as IDLE, Jupyter Notebook, or a Python shell.

2. **Import the Function**: Import the `factorize` function from the `main.py` file.

```python
from main import factorize
```

3. **Call the Function**: Pass an integer to the `factorize` function to get its prime factors.

```python
result = factorize(56)
print(result)  # Output: [2, 2, 2, 7]
```

## Documentation

The function is documented with a docstring that explains its purpose and provides examples of its usage. You can access this documentation within a Python environment using the `help` function.

```python
help(factorize)
```

This will display the docstring, which includes a description of the function and example usage.

## Support

For any issues or questions regarding the software, please contact the development team at ChatDev. We are committed to providing support and assistance to ensure the software meets your needs.