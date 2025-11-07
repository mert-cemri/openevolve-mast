# Fizz Buzz Digit Counter

This software provides a function to count the occurrences of the digit '7' in numbers less than a given integer `n` that are divisible by either 11 or 13. This is a simple Python application that demonstrates basic programming concepts such as loops, conditionals, and string manipulation.

## Main Functionality

The main functionality of this software is encapsulated in the `fizz_buzz` function. This function takes an integer `n` as input and returns the number of times the digit '7' appears in integers less than `n` that are divisible by 11 or 13.

### Function Signature

```python
def fizz_buzz(n: int) -> int:
```

### Example Usage

```python
>>> fizz_buzz(50)
0
>>> fizz_buzz(78)
2
>>> fizz_buzz(79)
3
```

## Installation

This project does not require any external dependencies, so setting up the environment is straightforward. You only need to have Python installed on your system.

### Step-by-Step Installation Guide

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it using Git. Otherwise, you can simply copy the `main.py` file to your working directory.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: If you cloned the repository, navigate to the project directory.

   ```bash
   cd <project-directory>
   ```

4. **Run the Script**: You can run the script directly using Python.

   ```bash
   python main.py
   ```

## How to Use

To use the `fizz_buzz` function, you can either import it into another Python script or run it directly in an interactive Python session.

### Using in a Script

1. **Import the Function**: Import the `fizz_buzz` function from the `main.py` file.

   ```python
   from main import fizz_buzz
   ```

2. **Call the Function**: Call the function with the desired integer value.

   ```python
   result = fizz_buzz(100)
   print(result)
   ```

### Using in an Interactive Session

1. **Open Python Interactive Shell**: Open your terminal or command prompt and type `python` to start the interactive shell.

2. **Define the Function**: Copy and paste the `fizz_buzz` function definition into the shell.

3. **Call the Function**: Use the function with your desired input.

   ```python
   >>> fizz_buzz(100)
   ```

## Conclusion

This software provides a simple yet effective way to count specific digit occurrences in a range of numbers based on divisibility criteria. It is a great example for those learning Python and looking to understand basic programming constructs.