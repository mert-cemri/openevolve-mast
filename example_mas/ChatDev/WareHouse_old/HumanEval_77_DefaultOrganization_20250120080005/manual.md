# Cube Checker

This software provides a simple utility function to determine if a given integer is a perfect cube of another integer. It is designed to be lightweight and efficient, requiring no external dependencies.

## Main Functionality

The core functionality of this software is encapsulated in the `iscube` function. This function takes an integer as input and returns a boolean value indicating whether the integer is a perfect cube.

### Function: `iscube(a)`

- **Input**: An integer `a`.
- **Output**: Returns `True` if `a` is a perfect cube of some integer, otherwise returns `False`.

#### Examples:

- `iscube(1)` returns `True` because 1 is 1^3.
- `iscube(2)` returns `False` because 2 is not a perfect cube.
- `iscube(-1)` returns `True` because -1 is (-1)^3.
- `iscube(64)` returns `True` because 64 is 4^3.
- `iscube(0)` returns `True` because 0 is 0^3.
- `iscube(180)` returns `False` because 180 is not a perfect cube.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the code**: You can execute the `main.py` file directly to test the `iscube` function.

## Usage

To use the `iscube` function, simply import it into your Python script and call it with the desired integer as an argument.

```python
from main import iscube

# Example usage
print(iscube(27))  # Output: True
print(iscube(10))  # Output: False
```

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is straightforward and designed to be easily integrated into larger projects where checking for perfect cubes is necessary.

This software is ideal for educational purposes, mathematical computations, or any application requiring verification of perfect cubes.