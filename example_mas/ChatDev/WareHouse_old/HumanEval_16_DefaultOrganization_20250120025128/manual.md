manual.md

```
# Distinct Character Counter

This software provides a simple utility to count the number of distinct characters in a given string, ignoring case sensitivity. It is implemented in Python and is designed to be lightweight and easy to use.

## Main Functionality

The core functionality of this software is encapsulated in the `count_distinct_characters` function. This function takes a string as input and returns the number of distinct characters in that string, regardless of their case. For example:

- `count_distinct_characters('xyzXYZ')` will return `3`.
- `count_distinct_characters('Jerry')` will return `4`.

## Quick Install

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Prerequisites

- Python 3.x

### Installation

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change your directory to the project folder:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the actual directory name.

3. **Run the Code:**

   You can run the code directly using Python:

   ```bash
   python main.py
   ```

   Ensure that you have navigated to the directory containing `main.py`.

## Usage

To use the `count_distinct_characters` function, you can either import it into another Python script or use it directly in an interactive Python session.

### Example Usage

```python
from main import count_distinct_characters

# Example strings
string1 = 'xyzXYZ'
string2 = 'Jerry'

# Count distinct characters
result1 = count_distinct_characters(string1)
result2 = count_distinct_characters(string2)

print(f"Distinct characters in '{string1}': {result1}")
print(f"Distinct characters in '{string2}': {result2}")
```

### Running Tests

You can test the function using the provided examples in the docstring. Simply run the function with different inputs to verify its correctness.

## Documentation

The function is documented with examples in the docstring. You can view this documentation by accessing the function's `__doc__` attribute in Python.

```python
print(count_distinct_characters.__doc__)
```

This will display the function's purpose and usage examples.

## Support

For any issues or questions, please contact the development team at ChatDev. We are committed to providing support and ensuring the software meets your needs.

```