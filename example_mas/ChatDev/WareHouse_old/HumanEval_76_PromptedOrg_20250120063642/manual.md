# Simple Power Checker

This software provides a function to determine if a number \( x \) is a simple power of another number \( n \). A number \( x \) is considered a simple power of \( n \) if there exists an integer \( k \) such that \( n^k = x \).

## Main Functionality

The primary function of this software is:

- `is_simple_power(x, n)`: This function checks if the number \( x \) is a simple power of \( n \). It returns `True` if \( x \) is a simple power of \( n \), and `False` otherwise.

### Examples

- `is_simple_power(1, 4)` returns `True`
- `is_simple_power(2, 2)` returns `True`
- `is_simple_power(8, 2)` returns `True`
- `is_simple_power(3, 2)` returns `False`
- `is_simple_power(3, 1)` returns `False`
- `is_simple_power(5, 3)` returns `False`

## Installation

This software is implemented in Python. To use it, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Environment Setup

1. **Create a Virtual Environment (Optional but Recommended):**

   It is recommended to use a virtual environment to manage dependencies. You can create one using the following command:

   ```bash
   python -m venv myenv
   ```

   Activate the virtual environment:

   - On Windows:

     ```bash
     myenv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source myenv/bin/activate
     ```

2. **Install Dependencies:**

   This software does not have any external dependencies, so you can proceed to use it directly.

## Usage

To use the `is_simple_power` function, follow these steps:

1. **Clone the Repository:**

   Clone the repository to your local machine or download the `main.py` file.

2. **Run the Function:**

   You can use the function in your Python script or interactively in a Python shell. Here is an example of how to use it:

   ```python
   from main import is_simple_power

   result = is_simple_power(8, 2)
   print(result)  # Output: True
   ```

3. **Testing:**

   You can test the function with different values of \( x \) and \( n \) to verify its correctness.

## Conclusion

This software provides a simple yet effective way to determine if a number is a simple power of another. It is easy to integrate into larger projects or use as a standalone utility. If you have any questions or need further assistance, please feel free to reach out.