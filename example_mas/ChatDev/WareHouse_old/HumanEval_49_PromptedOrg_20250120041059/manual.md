# ModP Function User Manual

This manual provides detailed instructions on how to use the `modp` function, which calculates \(2^n \mod p\). This function is implemented in Python and does not require any external dependencies.

## Main Functionality

The `modp` function computes the result of \(2^n \mod p\) efficiently using the method of exponentiation by squaring. This method is particularly useful for handling large values of \(n\) without encountering overflow issues.

### Function Signature

```python
def modp(n: int, p: int) -> int:
```

- **Parameters:**
  - `n` (int): The exponent to which 2 is raised.
  - `p` (int): The modulus.

- **Returns:**
  - An integer representing \(2^n \mod p\).

### Example Usage

```python
print(modp(3, 5))    # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))  # Output: 1
```

## Installation

### Environment Setup

This function is implemented in Python and does not require any external libraries or dependencies. Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Running the Code

1. **Clone the Repository:**

   If the code is hosted in a repository, clone it using:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   ```bash
   cd <repository-directory>
   ```

3. **Run the Script:**

   Execute the script using Python:

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function:**

   If you are using this function in another script, ensure you import it correctly:

   ```python
   from main import modp
   ```

2. **Call the Function:**

   Use the function by passing the desired values for `n` and `p`:

   ```python
   result = modp(10, 3)
   print(result)  # Output will be the result of 2^10 % 3
   ```

## Conclusion

The `modp` function is a simple yet powerful tool for computing modular exponentiation. It is designed to handle large exponents efficiently, making it suitable for various applications in cryptography and number theory. With no external dependencies, it is easy to integrate into any Python project.