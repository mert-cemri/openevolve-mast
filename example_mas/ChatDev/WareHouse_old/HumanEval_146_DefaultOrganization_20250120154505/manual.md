# SpecialFilter User Manual

## Introduction

The `specialFilter` function is a Python utility designed to filter numbers from a list based on specific criteria. It identifies numbers that are greater than 10 and have both their first and last digits as odd numbers (1, 3, 5, 7, 9). This function is useful for data analysis tasks where such filtering criteria are needed.

## Main Functionality

- **Function Name**: `specialFilter`
- **Input**: A list of integers.
- **Output**: An integer representing the count of numbers that meet the specified criteria.

### Criteria for Filtering

1. The number must be greater than 10.
2. Both the first and last digits of the number must be odd.

### Example Usage

- `specialFilter([15, -73, 14, -15])` returns `1`
- `specialFilter([33, -2, -3, 45, 21, 109])` returns `2`

## Installation

### Environment Setup

This project does not require any external dependencies, making it simple to set up and run. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Running the Code

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

3. **Run the Python Script**: Execute the `main.py` file to test the `specialFilter` function.
   ```bash
   python main.py
   ```

## Usage

To use the `specialFilter` function, you can directly call it within your Python scripts or interactive Python sessions. Here is a simple example:

```python
from main import specialFilter

# Example list of numbers
numbers = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]

# Get the count of numbers meeting the criteria
result = specialFilter(numbers)

print(f"Count of numbers meeting the criteria: {result}")
```

## Conclusion

The `specialFilter` function is a straightforward utility for filtering numbers based on specific digit criteria. With no external dependencies, it is easy to integrate into existing Python projects. For any further questions or support, please contact our development team.