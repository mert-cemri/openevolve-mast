# Choose_Num Function

This software provides a simple utility function, `choose_num`, which is designed to find the largest even integer within a specified range of two positive numbers. If no such even number exists within the range, the function will return -1.

## Main Functionality

The primary function of this software is:

- **choose_num(x, y):** This function takes two positive numbers, `x` and `y`, and returns the largest even integer within the inclusive range `[x, y]`. If there is no even integer in the range, it returns `-1`.

### Example Usage

- `choose_num(12, 15)` will return `14`.
- `choose_num(13, 12)` will return `-1`.

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed:** You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository:** You can clone the repository using Git or download the ZIP file and extract it.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory:**

   ```bash
   cd <project-directory>
   ```

4. **Run the script:** You can execute the script directly using Python.

   ```bash
   python main.py
   ```

## How to Use

To use the `choose_num` function, you can either import it into your own Python scripts or run it directly from the `main.py` file.

### Importing into Your Script

You can import the `choose_num` function into your own Python script as follows:

```python
from main import choose_num

result = choose_num(12, 15)
print(result)  # Output: 14
```

### Running Directly

You can also modify the `main.py` file to include test cases or directly call the function with desired inputs.

```python
if __name__ == "__main__":
    print(choose_num(12, 15))  # Output: 14
    print(choose_num(13, 12))  # Output: -1
```

## Documentation

For further details and documentation, please refer to the comments within the `main.py` file, which provide a comprehensive explanation of the function's logic and usage.

This software is designed to be simple and efficient, requiring no additional setup beyond having Python installed. Enjoy using the `choose_num` function to find the largest even numbers within your specified ranges!