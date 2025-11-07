# Prime Length Checker

This software provides a simple function to determine if the length of a given string is a prime number. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main functionality of this software is encapsulated in the `prime_length` function. This function takes a string as input and returns `True` if the length of the string is a prime number, and `False` otherwise.

### Function Details

- **`prime_length(string)`**: 
  - **Input**: A string.
  - **Output**: A boolean value (`True` or `False`).
  - **Description**: Checks if the length of the input string is a prime number.

## Installation

Since this software does not require any external libraries, you only need to have Python installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

## Usage

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can use the function by importing it into your Python script or by running the `main.py` file directly.

   - **Importing into a Python Script**:

     ```python
     from main import prime_length

     # Example usage
     print(prime_length('Hello'))  # Output: True
     print(prime_length('orange')) # Output: False
     ```

   - **Running Directly**: You can also test the function by adding test cases in the `main.py` file and executing it.

     ```bash
     python main.py
     ```

## Example

Here is an example of how you can use the `prime_length` function:

```python
from main import prime_length

# Check if the length of the string is a prime number
print(prime_length('Hello'))    # Output: True
print(prime_length('abcdcba'))  # Output: True
print(prime_length('kittens'))  # Output: True
print(prime_length('orange'))   # Output: False
```

## Conclusion

This software provides a straightforward way to check if the length of a string is a prime number. It is easy to use and requires no additional setup beyond having Python installed. Feel free to integrate this function into your projects where such functionality is needed.