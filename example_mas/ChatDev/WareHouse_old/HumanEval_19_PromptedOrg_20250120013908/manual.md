# Sort Numbers User Manual

Welcome to the Sort Numbers application! This software is designed to sort a space-delimited string of numerals from 'zero' to 'nine' in ascending order. This user manual will guide you through the main functions of the software, how to install it, and how to use it effectively.

## Main Functions

The primary function of this software is:

- **sort_numbers(numbers: str) -> str**: This function takes a space-delimited string of numerals (e.g., 'three one five') and returns a string with the numerals sorted in ascending order (e.g., 'one three five').

## Installation

### Environment Setup

This application is written in Python and does not require any external dependencies. To run the application, ensure you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

### Quick Install

Since there are no external dependencies, you don't need to install any additional packages. Simply ensure that Python is installed and you're ready to go!

## How to Use

1. **Clone or Download the Repository**: Obtain the source code for the Sort Numbers application. You can clone the repository using Git or download the files directly.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

3. **Run the Application**: Execute the Python script using the following command:
   ```bash
   python main.py
   ```

4. **Use the Function**: You can use the `sort_numbers` function by importing it into your own Python scripts or by calling it directly in an interactive Python session. Here's an example of how to use it:
   ```python
   from main import sort_numbers

   result = sort_numbers('three one five')
   print(result)  # Output: 'one three five'
   ```

## Example Usage

Here's a quick example to demonstrate how the function works:

```python
from main import sort_numbers

# Example input
input_string = 'nine zero two five'

# Sort the numerals
sorted_string = sort_numbers(input_string)

# Output the result
print(sorted_string)  # Output: 'zero two five nine'
```

## Conclusion

The Sort Numbers application is a simple yet effective tool for sorting numerals represented as words. With no external dependencies, it's easy to set up and use. We hope this user manual helps you get started quickly and efficiently. If you have any questions or need further assistance, please feel free to reach out. Happy sorting!