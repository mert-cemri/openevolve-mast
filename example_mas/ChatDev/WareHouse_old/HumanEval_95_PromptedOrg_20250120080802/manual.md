manual.md

```
# Check Dict Case

A Python utility function to evaluate the case consistency of dictionary keys.

## Overview

The `check_dict_case` function is designed to determine if all keys in a given dictionary are either all lowercase or all uppercase strings. It returns `True` if this condition is met and `False` otherwise. Additionally, it returns `False` if the dictionary is empty or if any key is not a string.

## Main Functionality

- **check_dict_case(dict):** 
  - **Input:** A dictionary.
  - **Output:** Boolean value:
    - `True` if all keys are strings and are either all lowercase or all uppercase.
    - `False` if the dictionary is empty, contains non-string keys, or if the keys are mixed case.

## Installation

This utility does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

## Usage

1. **Clone or Download the Repository:**
   - Clone the repository using `git clone <repository-url>` or download the ZIP file and extract it.

2. **Navigate to the Directory:**
   - Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function:**
   - You can test the function by running a Python interpreter or by creating a script that imports the function.
   - Example usage in a Python script:
     ```python
     from main import check_dict_case

     # Test cases
     print(check_dict_case({"a": "apple", "b": "banana"}))  # Output: True
     print(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))  # Output: False
     print(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))  # Output: False
     print(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))  # Output: False
     print(check_dict_case({"STATE": "NC", "ZIP": "12345"}))  # Output: True
     ```

## Notes

- Ensure that the dictionary keys are of string type to avoid unexpected results.
- The function is designed to be simple and efficient, operating in O(n) time complexity, where n is the number of keys in the dictionary.

## Support

For any issues or questions, please contact the development team at support@chatdev.com.

```