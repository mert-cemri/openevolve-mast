manual.md

```
# Remove Vowels Application

This application provides a simple function to remove vowels from a given string. It is implemented in Python and can be used to process text by eliminating all vowels, both uppercase and lowercase.

## Main Functionality

The core functionality of this application is encapsulated in the `remove_vowels` function. This function takes a string as input and returns a new string with all vowels removed. The vowels considered are 'a', 'e', 'i', 'o', 'u' and their uppercase counterparts 'A', 'E', 'I', 'O', 'U'.

### Example Usage

```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in text if char not in vowels])

# Example usage
print(remove_vowels('abcdef'))  # Output: 'bcdf'
print(remove_vowels('aaBAA'))   # Output: 'B'
```

## Installation

To use this application, you need to have Python installed on your system. The application does not require any additional dependencies, so no external packages need to be installed.

### Installing Python

If you do not have Python installed, you can download it from the official website: [Python.org](https://www.python.org/). Follow the instructions on the website to install Python on your operating system.

## How to Use

1. **Clone the Repository**: First, clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Script**: Execute the script by running the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

   This will run the test cases included in the script and display the output for each case.

## Testing

The `main.py` file includes several test cases to demonstrate the functionality of the `remove_vowels` function. You can modify these test cases or add new ones to test the function with different inputs.

## Documentation

For further information on Python programming and string manipulation, you can refer to the official Python documentation: [Python Documentation](https://docs.python.org/3/).

This manual provides a comprehensive guide to using the Remove Vowels application. If you have any questions or encounter any issues, please feel free to reach out for support.
```