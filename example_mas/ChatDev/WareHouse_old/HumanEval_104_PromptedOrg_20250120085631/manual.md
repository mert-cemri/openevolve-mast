manual.md

```
# Unique Digits Filter

This software provides a function to filter out numbers from a list that contain any even digits. The resulting list is sorted in increasing order and only includes numbers that consist solely of odd digits.

## Main Functionality

The primary function of this software is:

- `unique_digits(x)`: This function takes a list of positive integers `x` and returns a sorted list of numbers that do not contain any even digits. For example:
  - `unique_digits([15, 33, 1422, 1])` returns `[1, 15, 33]`.
  - `unique_digits([152, 323, 1422, 10])` returns `[]`.

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change your directory to where the `main.py` file is located:
   ```
   cd <directory-name>
   ```

4. **Run the Code**: You can execute the code directly using Python:
   ```
   python main.py
   ```

## How to Use

1. **Prepare Your Input**: Create a list of positive integers that you want to filter.

2. **Call the Function**: Use the `unique_digits` function to filter your list. For example:
   ```python
   result = unique_digits([15, 33, 1422, 1])
   print(result)  # Output will be [1, 15, 33]
   ```

3. **View the Results**: The function will return a sorted list of numbers that do not contain any even digits.

## Example Usage

Here's a simple example to demonstrate how to use the `unique_digits` function:

```python
# Import the function from the main.py file
from main import unique_digits

# Define a list of numbers
numbers = [15, 33, 1422, 1, 152, 323, 10]

# Get the filtered list
filtered_numbers = unique_digits(numbers)

# Print the result
print("Filtered numbers:", filtered_numbers)
```

This will output:
```
Filtered numbers: [1, 15, 33]
```

## Conclusion

This software provides a straightforward way to filter out numbers with even digits from a list, ensuring the result is sorted in increasing order. With no external dependencies, it is easy to set up and use for any Python developer.
```