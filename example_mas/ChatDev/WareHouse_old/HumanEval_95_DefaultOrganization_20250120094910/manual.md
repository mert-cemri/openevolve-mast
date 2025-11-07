manual.md

```
# CheckDictCase

A simple Python utility to verify the case consistency of dictionary keys.

## Overview

The `check_dict_case` function is designed to evaluate a dictionary and determine if all keys are either in lowercase or uppercase. It returns `True` if all keys meet one of these conditions and `False` otherwise. The function also returns `False` if the dictionary is empty or if any key is not a string.

## Main Functionality

- **check_dict_case(d):** 
  - **Parameters:** 
    - `d` (dict): The dictionary to be evaluated.
  - **Returns:** 
    - `True` if all keys are strings in either all lowercase or all uppercase.
    - `False` if the dictionary is empty, contains non-string keys, or if the keys are mixed in case.

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. Ensure you have Python installed on your system.

### Steps to Install

1. **Clone the Repository:**
   - If the code is hosted on a repository, clone it using:
     ```
     git clone <repository-url>
     ```
   - Navigate to the project directory:
     ```
     cd <project-directory>
     ```

2. **Set Up Environment:**
   - It's recommended to use a virtual environment to manage dependencies:
     ```
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

3. **Install Python:**
   - Ensure Python is installed. You can download it from [python.org](https://www.python.org/downloads/).

4. **Install Dependencies:**
   - There are no external dependencies for this project, so you can skip this step.

## Usage

To use the `check_dict_case` function, simply import it into your Python script and pass a dictionary as an argument.

### Example

```python
from main import check_dict_case

# Example dictionaries
dict1 = {"a": "apple", "b": "banana"}
dict2 = {"Name": "John", "Age": "36", "City": "Houston"}

# Check dictionary cases
print(check_dict_case(dict1))  # Output: True
print(check_dict_case(dict2))  # Output: False
```

## Testing

You can test the function by running the script with various dictionaries to ensure it behaves as expected. Modify the examples in the script or add new ones to validate different scenarios.

## Documentation

For further details and updates, please refer to the project repository or contact the development team.

```

This manual provides a comprehensive guide for users to understand, install, and utilize the `check_dict_case` function effectively.