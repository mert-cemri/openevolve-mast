# Odd Count Software

This software is designed to process a list of strings, where each string consists of only digits, and return a list of formatted strings. Each formatted string indicates the number of odd digits in the corresponding input string.

## Main Functionality

The main function of this software is `odd_count(lst)`, which takes a list of strings as input and returns a list of formatted strings. Each formatted string describes the number of odd digits in the corresponding input string.

### Example Usage

```python
>>> odd_count(['1234567'])
["the number of odd elements 4n the str4ng 1 of the 4nput."]
>>> odd_count(['3', "11111111"])
["the number of odd elements 1n the str1ng 1 of the 1nput.",
 "the number of odd elements 8n the str8ng 2 of the 8nput."]
```

## Installation

This software does not require any external dependencies, so no additional installation steps are necessary beyond having Python installed on your system.

### Requirements

- Python 3.x

## How to Use

1. **Clone the Repository**: Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Software**: You can run the software by executing the `main.py` file in a Python environment.

   ```bash
   python main.py
   ```

4. **Use the Function**: You can use the `odd_count` function by importing it into your Python scripts or interactive environment.

   ```python
   from main import odd_count

   result = odd_count(['1234567', '3', '11111111'])
   print(result)
   ```

## Documentation

For further details on how to use the software, please refer to the inline documentation provided in the `main.py` file. The function is well-documented with examples to guide you through its usage.

## Support

If you encounter any issues or have questions about using this software, please feel free to reach out to our support team. We are here to help you make the most of this tool.