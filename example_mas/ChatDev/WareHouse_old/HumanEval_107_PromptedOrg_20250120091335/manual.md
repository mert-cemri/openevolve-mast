# Even Odd Palindrome Counter

This software provides a function to calculate the number of even and odd integer palindromes within a given range. It is a simple Python application that does not require any external dependencies.

## Main Function

The main function of this software is `even_odd_palindrome(n)`, which takes a positive integer `n` as input and returns a tuple containing the number of even and odd integer palindromes within the range from 1 to `n`, inclusive.

### Example Usage

- **Input:** `3`
  - **Output:** `(1, 2)`
  - **Explanation:** The integer palindromes are 1, 2, 3. One of them is even, and two of them are odd.

- **Input:** `12`
  - **Output:** `(4, 6)`
  - **Explanation:** The integer palindromes are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. Four of them are even, and six of them are odd.

## Installation

This project does not require any external dependencies, so you can run it with a standard Python environment. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** or download the `main.py` file to your local machine.

2. **Navigate to the directory** containing the `main.py` file.

3. **Run the script** using Python. You can test the function by calling it with different values of `n`.

```bash
python main.py
```

## How to Use

1. **Import the function** into your Python script or interactive shell.

```python
from main import even_odd_palindrome
```

2. **Call the function** with a positive integer `n` to get the count of even and odd palindromes.

```python
result = even_odd_palindrome(12)
print(result)  # Output: (4, 6)
```

## Documentation

This software is straightforward and does not require additional documentation beyond this manual. The function is designed to be simple and efficient, handling inputs up to `n = 1000` as specified in the task requirements.

For any questions or further assistance, please contact the development team at ChatDev.