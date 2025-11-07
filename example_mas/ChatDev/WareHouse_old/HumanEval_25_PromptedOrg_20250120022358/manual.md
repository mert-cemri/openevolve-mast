# Prime Factorization Software

This software provides a simple function to compute the prime factors of a given integer. The function returns a list of prime factors in ascending order, with each factor repeated according to its multiplicity in the factorization.

## Main Function

### `factorize(n: int) -> List[int]`

- **Description**: This function takes an integer `n` as input and returns a list of its prime factors in ascending order. Each factor is repeated according to how many times it appears in the factorization.

- **Parameters**: 
  - `n` (int): The integer to be factorized.

- **Returns**: 
  - `List[int]`: A list of prime factors of `n`.

- **Example Usage**:
  ```python
  >>> factorize(8)
  [2, 2, 2]
  >>> factorize(25)
  [5, 5]
  >>> factorize(70)
  [2, 5, 7]
  ```

## Installation

This software does not require any external dependencies. It is implemented purely in Python, making it easy to integrate into any Python environment.

### Quick Install

1. **Clone the Repository**: 
   - You can clone the repository to your local machine using the following command:
     ```bash
     git clone <repository-url>
     ```

2. **Navigate to the Directory**:
   - Change into the directory where the repository is cloned:
     ```bash
     cd <repository-directory>
     ```

3. **Run the Code**:
   - You can run the `main.py` file directly to test the function:
     ```bash
     python main.py
     ```

## Usage

To use the `factorize` function in your own projects, you can import it from the `main.py` file. Here is an example of how to use it:

```python
from main import factorize

# Example usage
number = 56
factors = factorize(number)
print(f"The prime factors of {number} are: {factors}")
```

This will output:
```
The prime factors of 56 are: [2, 2, 2, 7]
```

## Documentation

For further documentation and examples, please refer to the inline comments and docstrings within the `main.py` file. The code is designed to be straightforward and easy to understand, with examples provided in the docstring of the `factorize` function.