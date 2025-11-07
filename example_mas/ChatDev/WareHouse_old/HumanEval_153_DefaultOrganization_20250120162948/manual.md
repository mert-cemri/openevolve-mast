manual.md

```
# Strongest Extension Finder

This software provides a function to determine the strongest extension for a given class name based on the strength calculated from the number of uppercase and lowercase letters in the extension names.

## Main Functionality

The main function of this software is `Strongest_Extension`, which takes a class name and a list of extensions as input and returns the strongest extension in the format `ClassName.StrongestExtensionName`.

### How It Works

- **Input**: 
  - `class_name`: A string representing the name of the class.
  - `extensions`: A list of strings representing the extensions.

- **Output**: 
  - A string in the format `ClassName.StrongestExtensionName`, where `StrongestExtensionName` is the extension with the highest strength.

- **Strength Calculation**: 
  - The strength of an extension is calculated as the difference between the number of uppercase letters (CAP) and the number of lowercase letters (SM) in the extension's name.
  - Strength = CAP - SM
  - If two or more extensions have the same strength, the one that appears first in the list is chosen.

## Installation

This software does not require any external dependencies. You can simply download the `main.py` file and run it using Python.

### Prerequisites

- Python 3.x

### Installation Steps

1. **Download the Code**: 
   - Download the `main.py` file to your local machine.

2. **Run the Code**: 
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the following command:
     ```
     python main.py
     ```

## Usage

To use the `Strongest_Extension` function, you can either run the `main.py` script directly or import the function into your own Python script.

### Example Usage

```python
from main import Strongest_Extension

# Example 1
result1 = Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])
print(result1)  # Output: Slices.SErviNGSliCes

# Example 2
result2 = Strongest_Extension('my_class', ['AA', 'Be', 'CC'])
print(result2)  # Output: my_class.AA
```

## Documentation

For further details on the implementation and usage of the `Strongest_Extension` function, please refer to the comments within the `main.py` file.

```