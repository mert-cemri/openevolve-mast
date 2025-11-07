manual.md

```
# Choose Num Function

This software provides a simple utility function `choose_num` that returns the largest even integer within a specified inclusive range [x, y]. If no even number exists within the range, it returns -1. This function is useful for applications where you need to identify the largest even number within a given range.

## Main Functionality

- **choose_num(x, y):** This function takes two positive integers, `x` and `y`, and returns the largest even integer within the inclusive range [x, y]. If no even number exists within the range, it returns -1.

### Example Usage

```python
# Example 1: Range with an even number
result = choose_num(12, 15)
print(result)  # Output: 14

# Example 2: Range without an even number
result = choose_num(13, 12)
print(result)  # Output: -1
```

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository:** Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory:**
   ```bash
   cd <repository-directory>
   ```

4. **Run the script:** You can directly run the `main.py` script to test the function.
   ```bash
   python main.py
   ```

## How to Use

1. **Import the function:** Import the `choose_num` function from the `main.py` file into your Python script.
   ```python
   from main import choose_num
   ```

2. **Call the function:** Use the function by passing two positive integers as arguments.
   ```python
   largest_even = choose_num(10, 20)
   print(largest_even)  # This will print the largest even number in the range [10, 20]
   ```

## Documentation

For further details and documentation, please refer to the comments within the `main.py` file. The function is self-contained and does not require additional libraries or dependencies.

```