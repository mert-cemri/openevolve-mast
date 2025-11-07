# DigitSum User Manual

Welcome to the DigitSum software! This application is designed to calculate the sum of ASCII values of uppercase characters in a given string. This document will guide you through the installation process, introduce the main function of the software, and provide instructions on how to use it.

## Main Function

The primary function of this software is `digitSum`, which takes a string as input and returns the sum of the ASCII values of all uppercase characters in that string. If there are no uppercase characters, the function returns 0.

### Function Signature

```python
def digitSum(s: str) -> int:
```

### Examples

- `digitSum("")` returns `0`
- `digitSum("abAB")` returns `131`
- `digitSum("abcCd")` returns `67`
- `digitSum("helloE")` returns `69`
- `digitSum("woArBld")` returns `131`
- `digitSum("aAaaaXa")` returns `153`

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Step-by-Step Installation

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Download the Code**: Obtain the `main.py` file containing the `digitSum` function.

3. **Run the Code**: You can execute the code using a Python interpreter. Open a terminal or command prompt, navigate to the directory containing `main.py`, and run:

   ```bash
   python main.py
   ```

## How to Use

To use the `digitSum` function, you can either call it directly within the `main.py` file or import it into another Python script.

### Example Usage

Here is how you can use the `digitSum` function in a Python script:

```python
# Import the function if using from another script
# from main import digitSum

# Example usage
result = digitSum("abAB")
print(result)  # Output: 131

result = digitSum("helloE")
print(result)  # Output: 69
```

## Conclusion

The DigitSum software is a simple yet effective tool for calculating the sum of ASCII values of uppercase characters in a string. With no external dependencies, it is easy to set up and use. We hope this manual helps you get started quickly and efficiently. If you have any questions or need further assistance, please feel free to reach out.