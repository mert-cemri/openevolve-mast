# Strongest Extension User Manual

Welcome to the Strongest Extension software! This tool is designed to help you determine the strongest extension for a given class name based on the strength of each extension. The strength is calculated by the difference between the number of uppercase and lowercase letters in the extension's name.

## Main Functionality

The primary function of this software is:

- **Strongest_Extension(class_name, extensions):** This function takes a class name and a list of extensions. It calculates the strength of each extension and returns the strongest one in the format: `ClassName.StrongestExtensionName`. If multiple extensions have the same strength, the one appearing first in the list is chosen.

## Installation

To use the Strongest Extension software, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly use it without installing any external packages.

### Quick Install

1. **Ensure Python is installed:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository:** Obtain the `main.py` file containing the Strongest Extension function.

## How to Use

1. **Prepare your environment:** Ensure you have Python installed and the `main.py` file available in your working directory.

2. **Run the function:**

   - Open a terminal or command prompt.
   - Navigate to the directory containing the `main.py` file.
   - Use a Python interpreter to run the script and call the `Strongest_Extension` function with your desired class name and list of extensions.

   Example usage:
   ```python
   # In your Python environment
   from main import Strongest_Extension

   # Example 1
   result1 = Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])
   print(result1)  # Output: 'Slices.SErviNGSliCes'

   # Example 2
   result2 = Strongest_Extension('my_class', ['AA', 'Be', 'CC'])
   print(result2)  # Output: 'my_class.AA'
   ```

3. **Interpret the results:** The function will return the strongest extension in the specified format. Use this result as needed in your application.

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The code is documented to help you understand the logic and usage of the function.

Thank you for using the Strongest Extension software! If you have any questions or need support, please feel free to reach out.