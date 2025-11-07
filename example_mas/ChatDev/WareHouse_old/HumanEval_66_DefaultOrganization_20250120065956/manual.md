# DigitSum Application

This application provides a simple function to calculate the sum of ASCII values of uppercase characters in a given string. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The primary function of this application is `digitSum`, which takes a string as input and returns the sum of the ASCII values of the uppercase characters only. This can be useful in scenarios where you need to process strings and extract information based on character case.

### Function Definition

```python
def digitSum(s):
    """
    Takes a string as input and returns the sum of the ASCII values of the uppercase characters only.
    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum(ord(char) for char in s if char.isupper())
```

## Installation

Since this project does not require any external dependencies, you can simply download the `main.py` file and use it in your Python environment.

### Quick Setup

1. **Download the Code**: Obtain the `main.py` file containing the `digitSum` function.

2. **Run the Code**: Use any Python environment to execute the function. Ensure you have Python installed on your system.

## Usage

To use the `digitSum` function, follow these steps:

1. **Import the Function**: If you are using this in a larger project, import the function from `main.py`.

   ```python
   from main import digitSum
   ```

2. **Call the Function**: Pass a string to the `digitSum` function and receive the sum of ASCII values of uppercase characters.

   ```python
   result = digitSum("abAB")
   print(result)  # Output: 131
   ```

## Examples

Here are some examples of how the `digitSum` function can be used:

- `digitSum("")` returns `0` because there are no uppercase characters.
- `digitSum("abAB")` returns `131` because the ASCII values of 'A' and 'B' are 65 and 66, respectively.
- `digitSum("abcCd")` returns `67` because the ASCII value of 'C' is 67.
- `digitSum("helloE")` returns `69` because the ASCII value of 'E' is 69.
- `digitSum("woArBld")` returns `131` because the ASCII values of 'A' and 'B' are 65 and 66, respectively.
- `digitSum("aAaaaXa")` returns `153` because the ASCII values of 'A' and 'X' are 65 and 88, respectively.

## Conclusion

The `digitSum` function is a straightforward utility for summing the ASCII values of uppercase characters in a string. It is easy to integrate into any Python project and requires no additional setup. Enjoy using this simple yet effective tool!