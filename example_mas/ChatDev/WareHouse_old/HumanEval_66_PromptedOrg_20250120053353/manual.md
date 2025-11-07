# DigitSum User Manual

## Introduction

The `digitSum` function is a simple Python utility designed to calculate the sum of ASCII values of uppercase characters in a given string. This function is useful for applications where you need to process strings and extract information based on character properties, specifically focusing on uppercase letters.

## Main Function

### digitSum

- **Purpose**: To compute the sum of ASCII values of all uppercase characters in a given string.
- **Input**: A string `s`.
- **Output**: An integer representing the sum of ASCII values of uppercase characters.

#### Examples

- `digitSum("")` returns `0`
- `digitSum("abAB")` returns `131`
- `digitSum("abcCd")` returns `67`
- `digitSum("helloE")` returns `69`
- `digitSum("woArBld")` returns `131`
- `digitSum("aAaaaXa")` returns `153`

## Installation

### Environment Setup

This project does not require any external dependencies, making it straightforward to set up and run. Ensure you have Python installed on your system.

### Steps

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

3. **Run the Code**: You can directly run the `main.py` file to test the function.
   ```bash
   python main.py
   ```

## Usage

To use the `digitSum` function, simply call it with a string argument. The function will return the sum of ASCII values of all uppercase characters in the string.

### Example Usage

```python
# Import the function from the module
from main import digitSum

# Example strings
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
```

## Documentation

For further documentation and examples, refer to the comments within the `main.py` file. The function is well-documented with examples to help you understand its usage and expected outputs.

## Support

For any issues or questions, please contact the development team or refer to the project's repository for further assistance.