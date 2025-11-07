manual.md

```
# Solution Function for Summing Odd Elements in Even Positions

This software provides a simple Python function that calculates the sum of all odd integers located at even indices in a given list. It is designed to be lightweight and does not require any external dependencies.

## Quick Install

Since this software does not require any external libraries, there is no need for installation of additional packages. You can directly use the function in your Python environment.

## 🤔 What is this?

The function `solution(lst)` is designed to solve a specific problem: given a non-empty list of integers, it returns the sum of all odd elements that are located at even positions (0-based index) in the list.

### Examples:

- `solution([5, 8, 7, 1])` returns `12` because the odd numbers at even indices are 5 (index 0) and 7 (index 2), and their sum is 12.
- `solution([3, 3, 3, 3, 3])` returns `9` because the odd numbers at even indices are 3 (index 0), 3 (index 2), and 3 (index 4), and their sum is 9.
- `solution([30, 13, 24, 321])` returns `0` because there are no odd numbers at even indices.

## 📖 How to Use

1. **Prepare Your Environment:**
   - Ensure you have Python installed on your system. This function is compatible with Python 3.x versions.

2. **Using the Function:**
   - Copy the function code into your Python script or interactive environment.
   - Call the function `solution(lst)` with your desired list of integers.

### Example Usage:

```python
def solution(lst):
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)

# Example call
result = solution([5, 8, 7, 1])
print(result)  # Output: 12
```

## Additional Information

- **No External Dependencies:** This software does not require any external Python packages, making it easy to integrate into any project.
- **Lightweight and Efficient:** The function is designed to be efficient, leveraging Python's list comprehensions for concise and fast execution.

Feel free to integrate this function into your projects where you need to perform similar calculations on lists of integers.
```