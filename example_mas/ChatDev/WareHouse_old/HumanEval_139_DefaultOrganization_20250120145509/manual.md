Here is the `manual.md` file for the software:

```
# Special Factorial Calculator

This software calculates the Brazilian factorial of a given integer. The Brazilian factorial is defined as the product of all factorials from n! to 1!.

## Main Functionality

The main functionality of this software is to compute the Brazilian factorial of a given integer `n`. The Brazilian factorial is calculated as follows:

\[ \text{brazilian\_factorial}(n) = n! \times (n-1)! \times (n-2)! \times \ldots \times 1! \]

For example, for `n = 4`, the Brazilian factorial is calculated as:

\[ 4! \times 3! \times 2! \times 1! = 24 \times 6 \times 2 \times 1 = 288 \]

## Quick Install

To use this software, you need to have Python installed on your system. The software requires Python version 3.6 or higher. You can install the necessary environment dependencies using the following command:

```bash
pip install -r requirements.txt
```

This will ensure that your Python environment is set up correctly to run the software.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the repository is cloned.

3. **Run the Software**: Execute the `main.py` file to calculate the Brazilian factorial of a given integer. You can do this by running the following command in your terminal:

   ```bash
   python main.py
   ```

4. **Input the Integer**: The function `special_factorial(n)` is defined in the `main.py` file. You can call this function with the desired integer `n` to get the Brazilian factorial.

   Example usage in a Python script:

   ```python
   from main import special_factorial

   result = special_factorial(4)
   print(result)  # Output will be 288
   ```

## Documentation

For further details on how the software works, please refer to the comments in the `main.py` file. The code is well-documented to help you understand the logic behind the Brazilian factorial calculation.

If you encounter any issues or have questions, feel free to reach out for support.

```