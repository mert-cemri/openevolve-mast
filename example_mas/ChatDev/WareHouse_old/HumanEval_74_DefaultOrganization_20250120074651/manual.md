# Total Match Function

This software provides a simple Python function called `total_match` that compares two lists of strings and returns the list with fewer total characters. If both lists have the same number of characters, it returns the first list.

## Main Functionality

The main function of this software is:

- **total_match(lst1, lst2):** This function accepts two lists of strings, calculates the total number of characters in each list, and returns the list with fewer characters. If both lists have the same number of characters, it returns the first list.

### Examples

- `total_match([], [])` ➞ `[]`
- `total_match(['hi', 'admin'], ['hI', 'Hi'])` ➞ `['hI', 'Hi']`
- `total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])` ➞ `['hi', 'admin']`
- `total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])` ➞ `['hI', 'hi', 'hi']`
- `total_match(['4'], ['1', '2', '3', '4', '5'])` ➞ `['4']`

## Installation

There are no external dependencies required for this software, so you can use it directly in any Python environment.

### Quick Start

1. **Clone the Repository:**
   - Clone the repository to your local machine.

2. **Navigate to the Directory:**
   - Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Code:**
   - You can run the code by executing the `main.py` file in a Python environment.

   ```bash
   python main.py
   ```

## Usage

To use the `total_match` function, you can import it into your Python script or interactive session. Here's an example of how to use it:

```python
from main import total_match

# Example usage
result = total_match(['hi', 'admin'], ['hI', 'Hi'])
print(result)  # Output: ['hI', 'Hi']
```

## Documentation

The function is straightforward and does not require additional documentation beyond the examples provided. For any further questions or issues, please refer to the comments within the code or contact support.

This manual provides all the necessary information to understand, install, and use the `total_match` function effectively.