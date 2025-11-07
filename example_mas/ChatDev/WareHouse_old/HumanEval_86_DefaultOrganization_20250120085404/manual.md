manual.md

```
# Anti-Shuffle Application

This application provides a simple function to reorder the characters of each word in a given string in ascending ASCII order, while maintaining the original order of words and spaces. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The core functionality of this application is encapsulated in the `anti_shuffle` function. This function takes a string as input and returns a new string where each word's characters are sorted in ascending order based on their ASCII values. The function preserves the order of words and spaces in the input string.

### Example Usage

- `anti_shuffle('Hi')` returns `'Hi'`
- `anti_shuffle('hello')` returns `'ehllo'`
- `anti_shuffle('Hello World!!!')` returns `'Hello !!!Wdlor'`

## Installation

Since this application does not require any external libraries, setting up the environment is straightforward. You only need to have Python installed on your system.

### Step-by-Step Installation Guide

1. **Install Python**: Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have the code in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change into the directory where the `main.py` file is located:
   ```bash
   cd <project-directory>
   ```

4. **Run the Script**: Execute the script using Python to see the function in action:
   ```bash
   python main.py
   ```

## How to Use

To use the `anti_shuffle` function in your own projects, follow these steps:

1. **Import the Function**: Copy the `anti_shuffle` function from `main.py` into your own Python script or import it if you have the module available.

2. **Call the Function**: Pass a string to the `anti_shuffle` function and capture the returned ordered string.

```python
from main import anti_shuffle

result = anti_shuffle('Hello World!!!')
print(result)  # Output: 'Hello !!!Wdlor'
```

## Documentation

For further details on how the `anti_shuffle` function works, refer to the docstring provided within the `main.py` file. It includes a description of the function's purpose, input parameters, and example outputs.

This application is designed to be simple and efficient, making it easy to integrate into larger projects or use as a standalone utility for text processing tasks.
```
