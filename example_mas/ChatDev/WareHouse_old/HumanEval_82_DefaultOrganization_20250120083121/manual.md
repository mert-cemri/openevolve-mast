# Prime Length Checker

This software provides a simple utility to check if the length of a given string is a prime number. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main functionality of this software is encapsulated in the `prime_length` function. This function takes a string as input and returns `True` if the length of the string is a prime number, and `False` otherwise.

### Functions

1. **is_prime(n)**: 
   - This helper function checks if a given number `n` is a prime number.
   - It returns `True` if `n` is prime, and `False` otherwise.

2. **prime_length(string)**:
   - This function calculates the length of the input string and uses the `is_prime` function to determine if the length is a prime number.
   - It returns `True` if the length is prime, and `False` otherwise.

## Installation

Since this software does not require any external dependencies, you can directly run the Python script without any additional installation steps.

## Usage

To use the `prime_length` function, follow these steps:

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Save the provided code into a file named `main.py`.

3. Open a terminal or command prompt and navigate to the directory where `main.py` is located.

4. Run the Python script using the following command:

   ```bash
   python main.py
   ```

5. You can test the `prime_length` function by calling it with different string inputs. For example:

   ```python
   print(prime_length('Hello'))    # Output: True
   print(prime_length('abcdcba'))  # Output: True
   print(prime_length('kittens'))  # Output: True
   print(prime_length('orange'))   # Output: False
   ```

## Example

Here is an example of how you can use the `prime_length` function in your code:

```python
def main():
    test_strings = ['Hello', 'abcdcba', 'kittens', 'orange']
    for s in test_strings:
        result = prime_length(s)
        print(f"The length of '{s}' is {'a prime number' if result else 'not a prime number'}.")

if __name__ == "__main__":
    main()
```

This example will output whether the length of each test string is a prime number or not.

## Conclusion

This software provides a straightforward utility for checking if the length of a string is a prime number. It is easy to use and does not require any additional setup beyond having Python installed.