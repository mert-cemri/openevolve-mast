manual.md

```
# Even Odd Digit Counter

This software provides a simple utility function to count the number of even and odd digits in a given integer. It is designed to be straightforward and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this software is encapsulated in the `even_odd_count` function. This function takes an integer as input and returns a tuple containing the count of even digits and odd digits in that integer.

### Function Signature

```python
def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.
    Args:
        num (int): The integer to be analyzed.
    Returns:
        tuple: A tuple containing the count of even digits and odd digits.
    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
```

### Example Usage

```python
# Example 1
result = even_odd_count(-12)
print(result)  # Output: (1, 1)

# Example 2
result = even_odd_count(123)
print(result)  # Output: (1, 2)
```

## Installation

### Environment Setup

This software does not require any external dependencies, making it easy to integrate into any Python environment. Simply ensure that you have Python installed on your system.

### Installation Steps

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**: Change your directory to the location where the code is stored.
   ```bash
   cd <project-directory>
   ```
   Replace `<project-directory>` with the actual directory name.

3. **Run the Code**: You can directly run the `main.py` file to test the function.
   ```bash
   python main.py
   ```

## Usage

To use the `even_odd_count` function, simply import it into your Python script and call it with the desired integer input.

```python
from main import even_odd_count

# Use the function with any integer
result = even_odd_count(4567)
print(result)  # Output will be (2, 2) as there are two even digits (4, 6) and two odd digits (5, 7)
```

## Documentation

For further details on the function and its implementation, refer to the comments within the `main.py` file. The function is well-documented to provide clarity on its usage and expected behavior.

```