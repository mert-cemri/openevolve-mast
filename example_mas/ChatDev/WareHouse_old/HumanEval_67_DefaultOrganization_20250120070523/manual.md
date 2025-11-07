manual.md

```
# Fruit Distribution Calculator

This software calculates the number of mangoes in a basket given a string describing the number of apples and oranges, and an integer representing the total number of fruits.

## Main Functionality

The main function of this software is to determine the number of mangoes in a fruit basket. It takes two inputs:
- A string that specifies the number of apples and oranges in the format "X apples and Y oranges".
- An integer that represents the total number of fruits in the basket.

The function will return the number of mangoes by subtracting the number of apples and oranges from the total number of fruits.

### Example Usage

```python
fruit_distribution("5 apples and 6 oranges", 19)  # Returns 8
fruit_distribution("0 apples and 1 oranges", 3)   # Returns 2
fruit_distribution("2 apples and 3 oranges", 100) # Returns 95
fruit_distribution("100 apples and 1 oranges", 120) # Returns 19
```

## Installation

To use this software, you need to have Python installed on your system. Follow these steps to set up your environment:

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

3. **Set Up Environment**: Navigate to the directory containing `main.py`.

4. **Install Dependencies**: There are no additional dependencies required for this software. Ensure your Python environment is active.

## How to Use

1. **Open a Terminal**: Navigate to the directory where `main.py` is located.

2. **Run the Script**: Use the Python interpreter to run the script. You can test the function by calling it with different inputs.

   ```bash
   python -c "from main import fruit_distribution; print(fruit_distribution('5 apples and 6 oranges', 19))"
   ```

3. **Modify Inputs**: You can modify the inputs directly in the terminal command to test different scenarios.

## Documentation

For further details on Python usage and string manipulation, refer to the official [Python documentation](https://docs.python.org/3/).

This software is designed to be simple and efficient, focusing solely on the task of calculating the number of mangoes in a fruit basket based on the provided inputs.
```