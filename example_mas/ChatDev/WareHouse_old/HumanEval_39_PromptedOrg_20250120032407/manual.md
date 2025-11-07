# Prime Fibonacci Finder

This software provides a function to find the n-th Fibonacci number that is also a prime number. It is implemented in Python and does not require any external dependencies.

## Quick Install

Since there are no external dependencies required for this software, you can directly use the Python standard library to run the code. Ensure you have Python installed on your system.

## 🤔 What is this?

The Prime Fibonacci Finder is a Python function that calculates the n-th Fibonacci number which is also a prime number. Fibonacci numbers are a sequence where each number is the sum of the two preceding ones, starting from 0 and 1. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

This function can be useful in mathematical computations and applications where both Fibonacci and prime numbers are of interest.

## 📖 Documentation

### Main Functions

- **`is_prime(num: int) -> bool`**: A helper function to check if a given number is prime.

- **`fibonacci_generator()`**: A generator function that yields Fibonacci numbers indefinitely.

- **`prime_fib(n: int) -> int`**: The main function that returns the n-th Fibonacci number which is also a prime number.

### How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Run the Code**: Open the `main.py` file and execute it in a Python environment. You can use the function `prime_fib(n)` to find the n-th prime Fibonacci number.

3. **Example Usage**:
    ```python
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
    ```

### Installation of Python

If you do not have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/). Follow the installation instructions for your operating system.

### Running the Code

To run the code, navigate to the directory containing `main.py` in your terminal or command prompt and execute the following command:

```bash
python main.py
```

This will run the script and you can call the `prime_fib` function with your desired input to get the corresponding prime Fibonacci number.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the repository.