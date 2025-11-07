# Fib4 Sequence Calculator

This software provides a function to compute the n-th element of the Fib4 number sequence, which is a variation of the Fibonacci sequence. The Fib4 sequence is defined as follows:

- fib4(0) -> 0
- fib4(1) -> 0
- fib4(2) -> 2
- fib4(3) -> 0
- fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

The function is implemented iteratively to ensure efficiency and avoid the pitfalls of recursion.

## Main Functionality

The main functionality of this software is to compute the n-th element of the Fib4 sequence using the `fib4` function. This function takes an integer `n` as input and returns the corresponding Fib4 number.

## Installation

This project does not require any external dependencies, so you can run it with a standard Python installation. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Usage

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Run the Code:**

   You can run the `main.py` file to use the `fib4` function. Open a terminal in the project directory and execute:

   ```bash
   python main.py
   ```

4. **Using the `fib4` Function:**

   You can use the `fib4` function within the `main.py` file or import it into another Python script. Here is an example of how to use it:

   ```python
   from main import fib4

   result = fib4(5)
   print(f"The 5th element of the Fib4 sequence is: {result}")
   ```

   This will output:

   ```
   The 5th element of the Fib4 sequence is: 4
   ```

## Documentation

For any further documentation or support, please refer to the comments within the `main.py` file, which provide detailed explanations of the function's logic and usage.

Feel free to reach out for support or to contribute to the project by submitting issues or pull requests on the project's repository.