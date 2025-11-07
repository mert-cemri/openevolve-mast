# Prime Factorization Software

This software provides a simple function to factorize a given integer into its prime factors. It returns a list of prime factors in ascending order, with each factor repeated according to its multiplicity in the factorization.

## Main Functionality

The main function provided by this software is `factorize(n: int) -> List[int]`. This function takes an integer `n` as input and returns a list of its prime factors. The factors are listed from smallest to largest, and each factor appears as many times as it divides the number.

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

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Directory**: Change into the directory where the code is located:
   ```bash
   cd <directory-name>
   ```
   Replace `<directory-name>` with the name of the directory containing the code.

3. **Run the Code**: You can run the code directly using Python:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: Import the `factorize` function from the module where it is defined.
   ```python
   from main import factorize
   ```

2. **Call the Function**: Use the `factorize` function by passing an integer as an argument.
   ```python
   factors = factorize(56)
   print(factors)  # Output: [2, 2, 2, 7]
   ```

## Documentation

The function is documented with a docstring that includes a description of its behavior and example usage. You can access this documentation in an interactive Python session using the `help` function:
```python
help(factorize)
```

## Conclusion

This software provides a straightforward and efficient way to factorize integers into their prime components. With no external dependencies, it is easy to install and use in any Python environment.