# Greatest Common Divisor (GCD) Calculator

This software module provides a function to calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The GCD is the largest positive integer that divides each of the integers without leaving a remainder.

## Main Function

The main function provided by this module is `greatest_common_divisor(a: int, b: int) -> int`. It takes two integers, `a` and `b`, as input and returns their greatest common divisor.

### Example Usage

```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
```

## Installation

This project does not require any external dependencies, so you can use it directly without installing additional packages. However, you need to have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: If the code is hosted in a repository, clone it to your local machine. For example:
   ```bash
   git clone https://github.com/yourusername/gcd-calculator.git
   ```

3. **Navigate to the project directory**:
   ```bash
   cd gcd-calculator
   ```

4. **Run the code**: You can directly run the `main.py` file to use the function.
   ```bash
   python main.py
   ```

## How to Use

1. **Open the `main.py` file**: You can open the `main.py` file in any Python-compatible IDE or text editor.

2. **Call the function**: Use the `greatest_common_divisor` function by passing two integers as arguments. For example:
   ```python
   result = greatest_common_divisor(48, 18)
   print(f"The GCD of 48 and 18 is {result}")
   ```

3. **Run the script**: Execute the script to see the result of the GCD calculation.

## Documentation

For more information on the Euclidean algorithm and its implementation, you can refer to the following resources:

- [Euclidean Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [Python Official Documentation](https://docs.python.org/3/)

This user manual provides a comprehensive guide to using the GCD calculator module, ensuring you can easily integrate it into your projects or use it for educational purposes.