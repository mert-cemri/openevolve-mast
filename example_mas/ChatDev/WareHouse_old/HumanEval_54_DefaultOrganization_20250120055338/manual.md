manual.md

```
# Same Characters Checker

This software provides a simple utility function to check if two words have the same characters. It is implemented in Python and is designed to be lightweight and easy to use.

## Main Functionality

The main function provided by this software is `same_chars`, which checks if two given strings contain the same set of characters, regardless of the order or frequency of those characters. This can be useful in various applications where character composition is more important than character order.

### Function Definition

```python
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
```

### Example Usage

```python
>>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
True
>>> same_chars('abcd', 'dddddddabc')
True
>>> same_chars('dddddddabc', 'abcd')
True
>>> same_chars('eabcd', 'dddddddabc')
False
>>> same_chars('abcd', 'dddddddabce')
False
>>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
False
```

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Step-by-Step Installation

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can directly run the `main.py` file to test the function:
   ```bash
   python main.py
   ```

## Usage

To use the `same_chars` function in your own projects, you can import it from the `main.py` file and call it with your desired string inputs.

### Example

```python
from main import same_chars

result = same_chars('hello', 'olelh')
print(result)  # Output: True
```

## Documentation

For further details on how the function works, you can refer to the docstring within the `main.py` file. The docstring includes examples and a brief description of the function's purpose.

## Support

If you encounter any issues or have questions about using this software, please contact our support team at support@chatdev.com.

```