# Get Positive Numbers

This software provides a simple utility function to filter and return only the positive numbers from a given list. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function of this software is:

- **get_positive(l: list):** This function takes a list of numbers as input and returns a new list containing only the positive numbers from the input list.

### Example Usage

```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]

>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

## Installation

This software does not require any external libraries or dependencies. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed:**
   - You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository:**
   - Clone the repository using Git:
     ```bash
     git clone <repository-url>
     ```
   - Or download the ZIP file and extract it.

3. **Navigate to the project directory:**
   ```bash
   cd <project-directory>
   ```

## How to Use

1. **Run the script:**
   - You can run the script directly using Python:
     ```bash
     python main.py
     ```

2. **Use the function in your own scripts:**
   - Import the `get_positive` function into your own Python script:
     ```python
     from main import get_positive

     # Example usage
     positive_numbers = get_positive([-1, 2, -4, 5, 6])
     print(positive_numbers)  # Output: [2, 5, 6]
     ```

## Documentation

For further details and examples, refer to the docstring within the `main.py` file. The function is straightforward and designed to be easily integrated into other Python projects.

Feel free to modify and extend the functionality as needed for your specific use case.