manual.md

```
# Check Dictionary Case

This software provides a simple utility function to check the case of dictionary keys. It determines if all keys in a given dictionary are either all lowercase strings or all uppercase strings. If the dictionary is empty or contains keys that are neither all lowercase nor all uppercase, the function will return `False`.

## Main Function

### `check_dict_case(dict)`

- **Purpose**: To verify if all keys in a dictionary are either all lowercase strings or all uppercase strings.
- **Parameters**: 
  - `dict`: A dictionary whose keys are to be checked.
- **Returns**: 
  - `True` if all keys are strings in lower case or all keys are strings in upper case.
  - `False` if the dictionary is empty or if the keys are mixed case or non-string types.

### Examples

- `check_dict_case({"a": "apple", "b": "banana"})` returns `True`.
- `check_dict_case({"a": "apple", "A": "banana", "B": "banana"})` returns `False`.
- `check_dict_case({"a": "apple", 8: "banana", "a": "apple"})` returns `False`.
- `check_dict_case({"Name": "John", "Age": "36", "City": "Houston"})` returns `False`.
- `check_dict_case({"STATE": "NC", "ZIP": "12345"})` returns `True`.

## Installation

This project does not require any external dependencies. It is implemented purely in Python and can be run in any standard Python environment.

### Quick Install

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Clone the repository**: Download or clone the repository to your local machine.

3. **Navigate to the project directory**: Open your terminal or command prompt and navigate to the directory where the project files are located.

4. **Run the script**: You can directly run the `main.py` file to test the function with your own dictionaries.

## Usage

To use the `check_dict_case` function, simply import it into your Python script and call it with the dictionary you want to check. Here is an example:

```python
from main import check_dict_case

# Example dictionary
my_dict = {"a": "apple", "b": "banana"}

# Check if all keys are in the same case
result = check_dict_case(my_dict)
print(result)  # Output: True
```

This function is useful for validating dictionaries where key case consistency is required, such as configuration files or data processing tasks.

```