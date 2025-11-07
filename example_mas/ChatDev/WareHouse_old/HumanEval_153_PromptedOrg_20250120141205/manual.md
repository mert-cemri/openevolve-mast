# Strongest Extension User Manual

Welcome to the Strongest Extension software! This tool is designed to help you determine the strongest extension for a given class name based on the number of uppercase and lowercase letters in the extension's name.

## Main Functionality

The core functionality of this software is encapsulated in the `Strongest_Extension` function. This function takes two inputs:
- `class_name`: A string representing the name of the class.
- `extensions`: A list of strings, where each string is an extension name.

The function calculates the "strength" of each extension based on the difference between the number of uppercase letters (CAP) and lowercase letters (SM) in the extension's name. The extension with the highest strength is considered the strongest. If multiple extensions have the same strength, the one that appears first in the list is chosen. The function returns a string in the format `ClassName.StrongestExtensionName`.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.
2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where `main.py` is located.

## How to Use

1. **Open the Terminal**: Open your terminal or command prompt.
2. **Run Python**: Execute the Python script by running the following command:
   ```bash
   python main.py
   ```
3. **Use the Function**: You can call the `Strongest_Extension` function within the script or import it into another Python script to use it with your desired class name and extensions list.

### Example Usage

Here's an example of how to use the `Strongest_Extension` function:

```python
# Example usage of the Strongest_Extension function
class_name = "Slices"
extensions = ['SErviNGSliCes', 'Cheese', 'StuFfed']
result = Strongest_Extension(class_name, extensions)
print(result)  # Output: Slices.SErviNGSliCes
```

## Documentation

For further details on the function and its implementation, please refer to the comments within the `main.py` file. The function is well-documented to help you understand its logic and usage.

Thank you for using the Strongest Extension software! If you have any questions or need further assistance, feel free to reach out.