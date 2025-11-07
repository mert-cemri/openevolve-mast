# Odd Count Software

This software is designed to process a list of strings, where each string consists of only digits, and return a list of formatted strings. Each formatted string indicates the number of odd digits in the corresponding input string.

## Main Functionality

The main function of this software is `odd_count(lst)`, which takes a list of strings as input and returns a list of formatted strings. Each formatted string describes the number of odd digits found in the corresponding input string.

### Example Usage

```python
>>> odd_count(['1234567'])
["the number of odd elements 4n the str4ng 4 of the 4nput."]
>>> odd_count(['3', "11111111"])
["the number of odd elements 1n the str1ng 1 of the 1nput.",
 "the number of odd elements 8n the str8ng 8 of the 8nput."]
```

## Installation

### Environment Setup

This software does not require any external dependencies. You can run it in any Python environment. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your working directory to the cloned repository:
   ```bash
   cd <repository-directory>
   ```

3. **Run the Software**: You can execute the `main.py` file directly to test the functionality:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: Import the `odd_count` function from the `main.py` file in your Python script or interactive shell.

   ```python
   from main import odd_count
   ```

2. **Call the Function**: Pass a list of strings (each containing only digits) to the `odd_count` function.

   ```python
   result = odd_count(['1234567', '3', '11111111'])
   print(result)
   ```

3. **Output**: The function will return a list of formatted strings indicating the number of odd digits in each input string.

## Documentation

For further details on how the function works, you can refer to the docstring provided in the `main.py` file. It includes a brief description and example usage of the function.

## Support

If you encounter any issues or have questions about using this software, please reach out to our support team at support@chatdev.com. We are here to assist you with any inquiries or technical difficulties you may face.