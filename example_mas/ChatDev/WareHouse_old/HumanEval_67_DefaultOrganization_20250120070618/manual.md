manual.md

```
# Fruit Distribution Software

This software provides a simple function to calculate the number of mangoes in a basket of fruits, given a string that specifies the number of apples and oranges, and an integer that represents the total number of fruits in the basket.

## Main Functionality

The main function of this software is `fruit_distribution`, which takes two inputs:
- A string `s` that contains the number of apples and oranges in the format "X apples and Y oranges".
- An integer `n` that represents the total number of fruits in the basket.

The function returns the number of mangoes in the basket by subtracting the number of apples and oranges from the total number of fruits.

### Example Usage

```python
# Example 1
result = fruit_distribution("5 apples and 6 oranges", 19)
print(result)  # Output: 8

# Example 2
result = fruit_distribution("0 apples and 1 oranges", 3)
print(result)  # Output: 2

# Example 3
result = fruit_distribution("2 apples and 3 oranges", 100)
print(result)  # Output: 95

# Example 4
result = fruit_distribution("100 apples and 1 oranges", 120)
print(result)  # Output: 19
```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted on a repository, clone it to your local machine using:
   ```
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change into the directory containing the `main.py` file:
   ```
   cd <directory-name>
   ```

4. **Run the Code**: You can run the code directly using Python:
   ```
   python main.py
   ```

## How to Use

1. **Open the `main.py` File**: Open the `main.py` file in your preferred code editor.

2. **Modify or Use the Function**: You can modify the function call with your own inputs or use the examples provided to test the functionality.

3. **Execute the Script**: Run the script using Python to see the results.

## Support

For any issues or questions regarding the software, please contact our support team at support@chatdev.com.

```
