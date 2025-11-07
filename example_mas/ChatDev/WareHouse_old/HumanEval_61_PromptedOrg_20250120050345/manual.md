# Correct Bracketing

This software provides a simple utility function to check if a string of brackets is correctly bracketed. It ensures that every opening bracket has a corresponding closing bracket.

## Main Function

### `correct_bracketing`

- **Purpose**: To determine if a string of brackets is correctly bracketed.
- **Input**: A string consisting of the characters `(` and `)`.
- **Output**: Returns `True` if every opening bracket has a corresponding closing bracket and they are correctly nested. Returns `False` otherwise.

#### Examples

```python
correct_bracketing("(")        # Output: False
correct_bracketing("()")       # Output: True
correct_bracketing("(()())")   # Output: True
correct_bracketing(")(()")     # Output: False
```

## Installation

This project does not require any external dependencies. You can run the code using Python without any additional installations.

### Quick Start

1. **Clone the Repository**: Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Move into the project directory.

   ```bash
   cd <project-directory>
   ```

3. **Run the Code**: You can directly run the `main.py` file to test the function.

   ```bash
   python main.py
   ```

## Usage

To use the `correct_bracketing` function, you can import it into your Python script and pass a string of brackets to it. The function will return `True` or `False` based on whether the brackets are correctly matched and nested.

```python
from main import correct_bracketing

result = correct_bracketing("(()())")
print(result)  # Output: True
```

## Documentation

This function is straightforward and does not require additional documentation beyond the examples provided. It is designed to be a utility function that can be easily integrated into larger projects where bracket validation is necessary.

For any further questions or support, please contact our support team.