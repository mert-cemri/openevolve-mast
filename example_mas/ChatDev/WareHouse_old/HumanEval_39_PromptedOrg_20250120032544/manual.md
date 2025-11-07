# Prime Fibonacci Finder

This software provides a function to find the n-th Fibonacci number that is also a prime number. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function of this software is `prime_fib(n: int)`, which returns the n-th Fibonacci number that is also a prime number. 

### Example Usage

```python
>>> prime_fib(1)
2
>>> prime_fib(2)
3
>>> prime_fib(3)
5
>>> prime_fib(4)
13
>>> prime_fib(5)
89
```

## Installation

Since this software does not require any external dependencies, you can use it directly in your Python environment. Ensure you have Python installed on your system.

### Steps to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file from the repository.

2. **Run the Code**: You can run the code directly in your Python environment. Open a Python interpreter or a script and import the `prime_fib` function from `main.py`.

3. **Call the Function**: Use the `prime_fib(n)` function to find the n-th prime Fibonacci number.

## How to Use

1. **Open a Python Environment**: You can use any Python environment like IDLE, PyCharm, VSCode, or a simple command line.

2. **Import the Function**: If you are using a script, make sure to import the `prime_fib` function.

   ```python
   from main import prime_fib
   ```

3. **Call the Function**: Pass the desired integer `n` to the `prime_fib` function to get the n-th prime Fibonacci number.

   ```python
   result = prime_fib(5)
   print(result)  # Output will be 89
   ```

## Additional Information

- **Fibonacci Numbers**: A sequence where each number is the sum of the two preceding ones, starting from 0 and 1.

- **Prime Numbers**: A natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.

This software efficiently combines these two mathematical concepts to provide a useful tool for finding prime Fibonacci numbers. Enjoy exploring the fascinating world of numbers!