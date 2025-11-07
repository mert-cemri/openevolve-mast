# SpecialFilter User Manual

Welcome to the SpecialFilter software! This tool is designed to filter numbers based on specific criteria: numbers greater than 10 with both the first and last digits being odd. This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it effectively.

## Quick Install

The SpecialFilter software does not require any external dependencies, making the installation process straightforward. You only need to have Python installed on your system.

### Step-by-Step Installation Guide

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **Clone the Repository:**
   - Clone the repository containing the SpecialFilter code to your local machine.

3. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory where the project is located.

4. **Run the Code:**
   - You can directly run the `main.py` file using Python to test the function.

## Main Functionality

### SpecialFilter Function

The core functionality of this software is encapsulated in the `specialFilter` function. This function takes an array of numbers as input and returns the count of numbers that meet the following criteria:
- The number is greater than 10.
- Both the first and last digits of the number are odd (1, 3, 5, 7, 9).

#### Example Usage

```python
from main import specialFilter

# Example 1
result1 = specialFilter([15, -73, 14, -15])
print(result1)  # Output: 1

# Example 2
result2 = specialFilter([33, -2, -3, 45, 21, 109])
print(result2)  # Output: 2
```

## How to Use

1. **Prepare Your Input:**
   - Create a list of numbers that you want to filter using the `specialFilter` function.

2. **Call the Function:**
   - Pass the list of numbers to the `specialFilter` function and store the result.

3. **Interpret the Result:**
   - The function will return an integer representing the count of numbers that satisfy the filtering criteria.

## Conclusion

The SpecialFilter software is a simple yet powerful tool for filtering numbers based on specific criteria. With no external dependencies required, it is easy to set up and use. We hope this manual helps you get the most out of the SpecialFilter function. If you have any questions or need further assistance, please feel free to reach out to our support team.