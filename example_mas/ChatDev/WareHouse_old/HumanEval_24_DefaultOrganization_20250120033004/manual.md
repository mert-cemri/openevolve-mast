manual.md

```
# Largest Divisor Finder

This software provides a simple utility to find the largest divisor of a given number `n` that is smaller than `n`. It is implemented in Python and does not require any external dependencies.

## Quick Install

Since there are no external dependencies required for this project, you can directly run the Python script without any additional installation steps.

## 🤔 What is this?

The Largest Divisor Finder is a straightforward Python function designed to determine the largest number that divides a given integer `n` evenly, which is also smaller than `n`. This can be useful in various mathematical computations and applications where such a divisor is needed.

## Main Function

The core functionality of this software is encapsulated in the `largest_divisor` function. Here is a brief overview:

- **Function Name:** `largest_divisor`
- **Input:** A single integer `n`
- **Output:** The largest integer that divides `n` evenly and is smaller than `n`

### Example Usage

```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
```

### Example

To find the largest divisor of 15:

```python
result = largest_divisor(15)
print(result)  # Output will be 5
```

## How to Use

1. **Ensure Python is Installed:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Run the Script:** You can run the `main.py` script directly using Python. Open your terminal or command prompt and navigate to the directory containing `main.py`.

3. **Execute the Script:**

   ```bash
   python main.py
   ```

   Replace `main.py` with the path to your script if it's located elsewhere.

## Documentation

For further details on Python programming and usage, you can refer to the [official Python documentation](https://docs.python.org/3/).

```