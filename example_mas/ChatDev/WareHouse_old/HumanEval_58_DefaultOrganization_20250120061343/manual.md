# Common Elements Finder

This software module provides a simple and efficient way to find sorted unique common elements from two lists. It is designed to be lightweight and easy to integrate into other Python projects.

## Main Functionality

The primary function of this module is `common(l1: list, l2: list)`, which takes two lists as input and returns a sorted list of unique elements that are common to both lists.

### Example Usage

```python
from main import common

result = common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
print(result)  # Output: [1, 5, 653]

result = common([5, 3, 2, 8], [3, 2])
print(result)  # Output: [2, 3]
```

## Installation

To use this module, you need to have Python installed on your system. The module does not have any external dependencies, so you do not need to install any additional packages.

### Quick Install

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change your working directory to the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Run the Python Script:**

   You can directly run the Python script using:

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function:**

   Import the `common` function from the `main.py` file in your Python script.

   ```python
   from main import common
   ```

2. **Call the Function:**

   Pass two lists as arguments to the `common` function to get the sorted unique common elements.

   ```python
   result = common([list1], [list2])
   ```

3. **Output:**

   The function will return a list of sorted unique common elements.

## Documentation

For more detailed documentation, please refer to the docstring within the `main.py` file. The docstring provides examples and a brief description of the function's behavior.

## Support

If you encounter any issues or have questions, please feel free to reach out to our support team. We are here to help you integrate and use this module effectively in your projects.