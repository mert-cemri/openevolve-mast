# Fizz Buzz Digit Counter

This software provides a function to count the number of times the digit '7' appears in integers less than a given number `n`, which are divisible by either 11 or 13.

## Main Functionality

The main function provided by this software is `fizz_buzz(n: int) -> int`. This function takes an integer `n` as input and returns the count of the digit '7' in numbers less than `n` that are divisible by 11 or 13.

### Example Usage

```python
# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You can simply clone the repository and run the code using Python.

### Steps to Install

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**

   Change your current directory to the project directory:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the actual directory name.

3. **Run the Code**

   You can run the code using Python. Make sure you have Python installed on your machine.

   ```bash
   python main.py
   ```

## How to Use

To use the `fizz_buzz` function, you can either import it into your own Python scripts or run it directly from the `main.py` file.

### Importing into Your Script

If you want to use the function in your own script, you can import it as follows:

```python
from main import fizz_buzz

result = fizz_buzz(100)
print(result)
```

### Running Directly

You can also modify the `main.py` file to include your desired input and run it directly to see the output.

## Conclusion

This software provides a simple yet effective way to count occurrences of the digit '7' in numbers divisible by 11 or 13. With no external dependencies, it is easy to set up and integrate into your projects.