manual.md

```
# By Length Function

This software provides a simple function to process an array of integers, specifically focusing on numbers between 1 and 9. The function sorts these numbers, reverses the order, and then replaces each number with its corresponding name in English.

## Main Functionality

The primary function of this software is `by_length`, which performs the following tasks:

1. **Filter**: It filters out numbers that are not between 1 and 9 inclusive.
2. **Sort and Reverse**: It sorts the filtered numbers in ascending order and then reverses the order.
3. **Map to Names**: It maps each number to its corresponding English name.

### Example Usage

- Input: `[2, 1, 1, 4, 5, 8, 2, 3]`
  - Process: Sort -> `[1, 1, 2, 2, 3, 4, 5, 8]`, Reverse -> `[8, 5, 4, 3, 2, 2, 1, 1]`
  - Output: `["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]`

- Input: `[]`
  - Output: `[]`

- Input: `[1, -1, 55]`
  - Output: `['One']`

## Installation

To use this software, ensure you have Python installed on your system. The function does not require any additional dependencies, so there is no need for a `requirements.txt` file.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.
2. **Navigate to the Directory**: Open your terminal and navigate to the directory containing `main.py`.

## How to Use

1. **Open the Terminal**: Navigate to the directory where `main.py` is located.
2. **Run Python**: Use the Python interpreter to run the script.

```bash
python main.py
```

3. **Call the Function**: You can call the `by_length` function with your desired array of integers.

```python
# Example usage
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # Output: ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
print(by_length([]))  # Output: []
print(by_length([1, -1, 55]))  # Output: ['One']
```

## Documentation

This function is straightforward and does not require additional documentation beyond this manual. If you have any questions or need further assistance, please contact our support team.

```