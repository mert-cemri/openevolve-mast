manual.md

```
# Carrot Consumption Calculator

A simple Python application to calculate the total number of carrots eaten by a rabbit and the number of carrots left after the rabbit attempts to eat a specified number of carrots.

## Quick Install

This application does not require any external dependencies, so you can run it directly with Python. Ensure you have Python installed on your system.

## 🤔 What is this?

The Carrot Consumption Calculator is a straightforward utility designed to help you determine how many carrots a rabbit has eaten and how many are left after a meal. This is particularly useful for scenarios where you need to manage carrot consumption efficiently.

## Main Functionality

The core functionality of this application is encapsulated in the `eat` function. This function takes three parameters:

- `number`: The number of carrots that have already been eaten by the rabbit.
- `need`: The number of additional carrots the rabbit needs to eat to complete its meal.
- `remaining`: The number of carrots currently available.

The function returns an array with two elements:
1. The total number of carrots eaten after the meal.
2. The number of carrots left after the meal.

### Example Usage

```python
from main import eat

# Example 1
result = eat(5, 6, 10)
print(result)  # Output: [11, 4]

# Example 2
result = eat(4, 8, 9)
print(result)  # Output: [12, 1]

# Example 3
result = eat(1, 10, 10)
print(result)  # Output: [11, 0]

# Example 4
result = eat(2, 11, 5)
print(result)  # Output: [7, 0]
```

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Script**: Use Python to run the script and test the `eat` function with different inputs as shown in the example usage.

```bash
python main.py
```

## 📖 Documentation

The `eat` function is well-documented within the code itself, providing detailed explanations of its parameters and return values. You can refer to the docstring in the `main.py` file for more information.

This application is designed to be simple and does not require any additional setup or dependencies beyond a standard Python installation.

Enjoy calculating your carrot consumption!
```