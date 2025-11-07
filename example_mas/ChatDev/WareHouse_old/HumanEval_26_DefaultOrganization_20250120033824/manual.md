# Remove Duplicates Software

This software provides a simple utility function to remove duplicates from a list of integers, keeping only the elements that occur once and maintaining their original order.

## Main Functionality

The main function of this software is:

- **remove_duplicates(numbers: List[int]) -> List[int]**: This function takes a list of integers as input and returns a new list with all elements that occur more than once removed. The order of the remaining elements is preserved as in the input list.

### Example Usage

```python
from main import remove_duplicates

# Example usage
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. You only need a Python environment to run the code.

### Setting Up the Environment

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

   ```bash
   cd path/to/directory
   ```

4. **Run the Code**: You can execute the code using a Python interpreter.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: Import the `remove_duplicates` function from the `main.py` file in your Python script.

2. **Pass a List of Integers**: Call the function with a list of integers as an argument.

3. **Get the Result**: The function will return a new list with duplicates removed, preserving the order of the elements that appear only once.

## Conclusion

This software provides a simple yet effective solution for removing duplicates from a list of integers. It is easy to integrate into any Python project and does not require any additional setup beyond having Python installed.