# Greatest Common Divisor (GCD) Calculator

This software module provides a function to calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The GCD is the largest positive integer that divides each of the integers without leaving a remainder.

## Main Function

The main function provided by this module is:

- `greatest_common_divisor(a: int, b: int) -> int`: This function takes two integers `a` and `b` as input and returns their greatest common divisor.

### Example Usage

```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
```

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository or download the module**: You can clone the repository or download the `main.py` file containing the function.

3. **Run the module**: You can run the module directly in your Python environment.

## How to Use

1. **Open your Python environment**: You can use any Python IDE or the command line.

2. **Import the function**: If you have saved the function in a file named `main.py`, you can import it using:

   ```python
   from main import greatest_common_divisor
   ```

3. **Call the function**: Use the function by passing two integers as arguments to find their GCD.

   ```python
   result = greatest_common_divisor(48, 18)
   print(result)  # Output will be 6
   ```

## Documentation

This module is designed to be simple and efficient for calculating the GCD of two numbers. It uses the Euclidean algorithm, which is a well-known method for this purpose.

For more information on the Euclidean algorithm, you can refer to [Euclidean algorithm on Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm).

Feel free to modify and extend the module as needed for your specific use cases.