# Fruit Distribution Software

This software is designed to calculate the number of mango fruits in a basket given a description of the number of apples and oranges, along with the total number of fruits in the basket.

## Main Functionality

The main function of this software is:

- **fruit_distribution(s: str, n: int) -> int**: This function takes a string `s` that describes the number of apples and oranges, and an integer `n` that represents the total number of fruits in the basket. It returns the number of mango fruits in the basket.

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

This software does not require any external dependencies. You can run it using a standard Python environment.

### Setting Up the Environment

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Clone the repository**: If the code is hosted in a repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:

   ```bash
   cd <project-directory>
   ```

4. **Run the code**: You can execute the script using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Open the `main.py` file**: This file contains the `fruit_distribution` function.

2. **Modify the input**: You can change the input string and integer in the function call to test different scenarios.

3. **Run the script**: Execute the script to see the output, which will be the number of mango fruits in the basket.

## Documentation

For further details on how the function works, refer to the docstring within the `main.py` file. It provides a clear explanation of the parameters and the return value of the function.

This software is simple and straightforward, designed to solve a specific problem without the need for additional libraries or complex setup.