# Fizz Buzz Digit Counter

This software provides a function to count the occurrences of the digit '7' in numbers less than a given integer `n` that are divisible by either 11 or 13. This can be useful for various mathematical and programming exercises or challenges.

## Main Functionality

The main function provided by this software is `fizz_buzz(n: int) -> int`. It calculates how many times the digit '7' appears in numbers less than `n` that are divisible by 11 or 13.

### Function Signature

```python
def fizz_buzz(n: int) -> int:
```

### Parameters

- `n` (int): The upper limit (exclusive) to check numbers against.

### Returns

- `int`: The count of digit '7' in numbers divisible by 11 or 13.

### Examples

```python
>>> fizz_buzz(50)
0
>>> fizz_buzz(78)
2
>>> fizz_buzz(79)
3
```

## Installation

To use this software, you need to have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Setting Up the Environment

1. **Clone the Repository**: Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Move into the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Although there are no external dependencies for this project, it is a good practice to create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install Required Packages**: If there were any dependencies, you would install them using:

   ```bash
   pip install -r requirements.txt
   ```

   Currently, the `requirements.txt` file is empty as there are no external dependencies.

## Usage

To use the `fizz_buzz` function, you can import it into your Python script or interactive session and call it with the desired integer `n`.

### Example Usage

```python
from main import fizz_buzz

result = fizz_buzz(100)
print(f"The digit '7' appears {result} times in numbers less than 100 that are divisible by 11 or 13.")
```

This will output the number of times the digit '7' appears in numbers less than 100 that are divisible by 11 or 13.

## Conclusion

This software provides a simple yet effective way to count specific digit occurrences in numbers divisible by certain integers. It is designed to be easy to use and integrate into larger projects or used standalone for specific tasks.