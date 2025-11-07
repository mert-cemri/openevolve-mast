# Greatest Common Divisor (GCD) Calculator

This software module provides a simple function to calculate the greatest common divisor (GCD) of two integers using Python. The GCD is the largest positive integer that divides each of the integers without leaving a remainder.

## Main Function

The main function provided in this module is:

- `greatest_common_divisor(a: int, b: int) -> int`: This function takes two integers `a` and `b` as input and returns their greatest common divisor. It uses the Euclidean algorithm, which is an efficient method for computing the GCD.

### Example Usage

```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
```

## Installation

This module does not require any external dependencies, making it straightforward to use. You only need to have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the GCD function.

3. **Run the script**: You can run the script directly using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the function**: If you are integrating this function into another Python script, you can import it as follows:

   ```python
   from main import greatest_common_divisor
   ```

2. **Call the function**: Use the function by passing two integer arguments to calculate their GCD.

   ```python
   result = greatest_common_divisor(48, 18)
   print(f"The GCD is: {result}")
   ```

## Documentation

This module is designed to be simple and efficient for calculating the greatest common divisor of two integers. The implementation uses the Euclidean algorithm, which is both time-tested and optimal for this purpose.

For further information or support, please contact our team at ChatDev. We are committed to providing assistance and ensuring that our software meets your needs effectively.