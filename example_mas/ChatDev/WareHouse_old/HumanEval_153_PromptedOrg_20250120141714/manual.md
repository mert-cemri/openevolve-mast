# Strongest Extension

This software module provides a function to determine the strongest extension for a given class based on the strength calculated from the number of uppercase and lowercase letters in the extension names.

## Main Functionality

The main function of this software is `Strongest_Extension`, which takes in a class name and a list of extensions. It calculates the strength of each extension based on the difference between the number of uppercase and lowercase letters. The extension with the highest strength is considered the strongest. If there are multiple extensions with the same strength, the one that appears first in the list is chosen.

### Function Signature

```python
def Strongest_Extension(class_name, extensions):
    """
    Determines the strongest extension for a given class based on the strength
    calculated from the number of uppercase and lowercase letters in the extension names.
    Parameters:
    class_name (str): The name of the class.
    extensions (list of str): A list of extension names.
    Returns:
    str: The class name concatenated with the strongest extension in the format
         ClassName.StrongestExtensionName.
    """
```

## Installation

This project does not require any external dependencies, so there is no need to install additional packages. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: Start by cloning the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Move into the directory where the `main.py` file is located.

   ```bash
   cd <directory-name>
   ```

3. **Run the Function**: You can use the `Strongest_Extension` function by importing it into your Python script or interactive session.

   ```python
   from main import Strongest_Extension

   # Example usage
   result = Strongest_Extension('my_class', ['AA', 'Be', 'CC'])
   print(result)  # Output: my_class.AA
   ```

4. **Test with Different Inputs**: You can test the function with different class names and extension lists to see how it determines the strongest extension.

   ```python
   result = Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])
   print(result)  # Output: Slices.SErviNGSliCes
   ```

## Documentation

For further details on how the function works, refer to the docstring provided within the `main.py` file. The docstring explains the parameters, return values, and provides examples of usage.

## Support

If you encounter any issues or have questions about using this software, please contact our support team or refer to the documentation provided in the repository.