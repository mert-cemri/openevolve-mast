# Common Elements Finder

This software provides a simple utility function to find and return the sorted unique common elements from two lists. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function of this software is:

- **common(l1: list, l2: list)**: This function takes two lists as input and returns a sorted list of unique elements that are common to both lists.

### Example Usage

```python
# Example 1
result = common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
print(result)  # Output: [1, 5, 653]

# Example 2
result = common([5, 3, 2, 8], [3, 2])
print(result)  # Output: [2, 3]
```

## Installation

This software does not require any external libraries or dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

1. **Ensure you have Python installed**: This software requires Python to be installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: You can clone the repository using Git or download the ZIP file and extract it.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**: Change your current directory to the location where you have cloned or extracted the project.

   ```bash
   cd <project-directory>
   ```

4. **Run the script**: You can run the script directly using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Open the `main.py` file**: This file contains the `common` function.

2. **Modify the input lists**: You can change the input lists in the `common` function call to test with different data.

3. **Execute the script**: Run the script to see the output of the `common` function.

4. **View the results**: The output will display the sorted list of unique common elements from the two input lists.

## Documentation

For further information and examples, please refer to the inline comments and docstrings within the `main.py` file. These provide additional context and usage examples for the `common` function.

This software is designed to be simple and straightforward, making it easy to integrate into larger projects or use as a standalone utility.