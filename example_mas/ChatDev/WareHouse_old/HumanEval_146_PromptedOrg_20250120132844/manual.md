# SpecialFilter User Manual

Welcome to the SpecialFilter software! This tool is designed to filter numbers based on specific criteria, providing a simple yet powerful way to analyze numerical data.

## Main Functionality

The core functionality of the SpecialFilter software is encapsulated in the `specialFilter` function. This function processes an array of numbers and returns the count of elements that meet the following criteria:

1. The number is greater than 10.
2. Both the first and last digits of the number are odd (1, 3, 5, 7, 9).

### Example Usage

- `specialFilter([15, -73, 14, -15])` returns `1`
- `specialFilter([33, -2, -3, 45, 21, 109])` returns `2`

## Installation

The SpecialFilter software is implemented in Python and does not require any external dependencies. You can run it in any Python environment. Here’s how you can set it up:

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

### Step 2: Set Up Your Environment

Since there are no external dependencies, you can directly use the Python environment to run the software. If you prefer using a virtual environment, you can set it up as follows:

1. Create a virtual environment:
   ```bash
   python -m venv myenv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source myenv/bin/activate
     ```

### Step 3: Run the Software

You can run the `specialFilter` function by executing the `main.py` file. Make sure your Python environment is active, and then run:

```bash
python main.py
```

## How to Use

To use the `specialFilter` function, simply call it with a list of numbers as the argument. The function will return the count of numbers that satisfy the specified conditions.

### Example Code

Here is an example of how you can use the function in your Python script:

```python
from main import specialFilter

numbers = [15, -73, 14, -15]
result = specialFilter(numbers)
print(f"The count of numbers meeting the criteria is: {result}")
```

## Conclusion

The SpecialFilter software provides a straightforward way to filter and analyze numbers based on specific criteria. With no external dependencies, it is easy to set up and use in any Python environment. Enjoy using SpecialFilter to enhance your data analysis tasks!