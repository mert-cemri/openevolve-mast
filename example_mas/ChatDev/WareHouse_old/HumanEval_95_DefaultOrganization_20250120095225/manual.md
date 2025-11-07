# CheckDictCase User Manual

Welcome to the CheckDictCase software! This tool is designed to help you determine if all keys in a given dictionary are either all lowercase strings or all uppercase strings. This manual will guide you through the main functions of the software, how to set up your environment, and how to use the tool effectively.

## Main Functions

The primary function of this software is `check_dict_case`. This function takes a dictionary as input and returns a boolean value based on the following criteria:

- **True**: If all keys in the dictionary are strings and are either all lowercase or all uppercase.
- **False**: If the dictionary is empty, contains non-string keys, or if the keys are a mix of lowercase and uppercase strings.

### Examples

- `check_dict_case({"a": "apple", "b": "banana"})` returns `True`.
- `check_dict_case({"a": "apple", "A": "banana", "B": "banana"})` returns `False`.
- `check_dict_case({"a": "apple", 8: "banana", "a": "apple"})` returns `False`.
- `check_dict_case({"Name": "John", "Age": "36", "City": "Houston"})` returns `False`.
- `check_dict_case({"STATE": "NC", "ZIP": "12345"})` returns `True`.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Follow the steps below to get started:

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```

### Step 2: Navigate to the Project Directory

Change your directory to the project folder:

```bash
cd <project-directory>
```

### Step 3: Verify Python Environment

Ensure you have Python installed on your system. You can verify this by running:

```bash
python --version
```

This software is compatible with Python 3.x versions.

## Usage

To use the `check_dict_case` function, follow these steps:

1. Open the `main.py` file in your preferred Python editor.
2. Call the `check_dict_case` function with a dictionary as an argument.
3. Run the script to see the output.

### Example Usage

```python
from main import check_dict_case

# Example dictionary
example_dict = {"a": "apple", "b": "banana"}

# Check if all keys are either all lowercase or all uppercase
result = check_dict_case(example_dict)

# Print the result
print(result)  # Output: True
```

## Conclusion

The CheckDictCase software is a simple yet effective tool for validating the case consistency of dictionary keys. With no external dependencies, it is easy to set up and use. We hope this manual helps you get the most out of the software. If you have any questions or need further assistance, please feel free to reach out.