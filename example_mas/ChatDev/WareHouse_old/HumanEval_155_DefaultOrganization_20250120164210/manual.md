manual.md

```
# Even Odd Digit Counter

This software provides a simple function to count the number of even and odd digits in a given integer. It is designed to be straightforward and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this software is encapsulated in the `even_odd_count` function. This function takes an integer as input and returns a tuple containing two elements: the count of even digits and the count of odd digits in the integer.

### Example Usage

```python
from main import even_odd_count

# Example 1
result = even_odd_count(-12)
print(result)  # Output: (1, 1)

# Example 2
result = even_odd_count(123)
print(result)  # Output: (1, 2)
```

## Installation

### Environment Setup

Since this project does not require any external dependencies, setting up the environment is straightforward. You only need to have Python installed on your system.

1. **Install Python**: If you haven't already, download and install Python from the official [Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: 
   ```bash
   cd <project-directory>
   ```

## How to Use

1. **Open the Python Environment**: You can use any Python environment of your choice, such as IDLE, PyCharm, or VSCode.

2. **Import the Function**: In your Python script or interactive shell, import the `even_odd_count` function from the `main.py` file.

3. **Call the Function**: Pass an integer to the `even_odd_count` function and receive a tuple with the counts of even and odd digits.

4. **View the Output**: The function will return a tuple, which you can print or use in further computations.

## Additional Notes

- The function handles negative numbers by considering only the absolute value of the integer.
- The function is designed to work with integers only. Passing non-integer types will result in an error.

This software is designed to be simple and efficient, providing a quick way to analyze the composition of digits in an integer. Enjoy using the Even Odd Digit Counter!
```