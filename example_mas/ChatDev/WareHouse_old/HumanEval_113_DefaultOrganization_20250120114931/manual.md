# Odd Count Software User Manual

Welcome to the Odd Count Software! This software is designed to process a list of strings, where each string consists of only digits, and return a list with a specific format. Each element in the output list describes the number of odd digits in the corresponding input string.

## Main Functions of the Software

The primary function of this software is `odd_count(lst)`, which takes a list of strings as input and returns a list of formatted strings. Each formatted string indicates the number of odd digits in the corresponding input string.

### Example Usage

```python
# Example usage
if __name__ == "__main__":
    print(odd_count(['1234567']))
    print(odd_count(['3', '11111111']))
```

The output for the above example will be:
```
["the number of odd elements 4n the str4ng 4 of the 4nput."]
["the number of odd elements 1n the str1ng 1 of the 1nput.",
 "the number of odd elements 8n the str8ng 8 of the 8nput."]
```

## Installation

To use this software, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly run the Python script.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the code.

3. **Run the script**: You can execute the script using a Python interpreter. Navigate to the directory containing `main.py` and run the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

## How to Use

1. **Prepare your input**: Create a list of strings where each string consists of only digits.

2. **Call the `odd_count` function**: Pass your list of strings to the `odd_count` function.

3. **Receive the output**: The function will return a list of strings formatted to indicate the number of odd digits in each input string.

## Documentation

This software is straightforward and does not require extensive documentation. The main focus is on the `odd_count` function, which is designed to be simple and efficient for processing lists of digit strings.

For any questions or further assistance, please feel free to reach out to our support team.

Thank you for using the Odd Count Software!