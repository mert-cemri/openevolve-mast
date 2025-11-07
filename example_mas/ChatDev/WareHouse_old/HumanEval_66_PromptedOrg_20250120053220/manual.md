# DigitSum Application

This application provides a simple function to calculate the sum of ASCII values of uppercase characters in a given string. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this application is encapsulated in the `digitSum` function. This function takes a string as input and returns the sum of the ASCII values of all uppercase characters in that string.

### Function Definition

```python
def digitSum(s):
    return sum(ord(char) for char in s if char.isupper())
```

### Examples

- `digitSum("")` returns `0`
- `digitSum("abAB")` returns `131`
- `digitSum("abcCd")` returns `67`
- `digitSum("helloE")` returns `69`
- `digitSum("woArBld")` returns `131`
- `digitSum("aAaaaXa")` returns `153`

## Installation

This application does not require any external dependencies, making it easy to set up and use. Simply ensure that you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine. Otherwise, copy the code into a file named `main.py`.

2. **Set Up Python Environment**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

3. **Run the Code**: You can run the code directly using Python. Open a terminal and navigate to the directory containing `main.py`, then execute:

   ```bash
   python main.py
   ```

## Usage

To use the `digitSum` function, simply import it into your Python script or interactive session and call it with the desired string input.

### Example Usage

```python
from main import digitSum

result = digitSum("abAB")
print(result)  # Output: 131
```

## Documentation

The `digitSum` function is straightforward and does not require additional configuration or setup. For further information or assistance, please refer to the comments within the code or contact the development team.

This application is designed to be simple and efficient, providing a quick solution for calculating the sum of ASCII values of uppercase characters in a string. Enjoy using the DigitSum application!