# Even Odd Count

This software provides a simple function to count the number of even and odd digits in a given integer. It is designed to be straightforward and efficient, making it easy to integrate into larger applications or use as a standalone utility.

## Main Functionality

The core functionality of this software is encapsulated in the `even_odd_count` function. This function takes an integer as input and returns a tuple containing the count of even and odd digits in the number.

### Example Usage

```python
from main import even_odd_count

# Example 1
result = even_odd_count(-12)
print(result)  # Output: (1, 1)

# Example 2
result = even_odd_count(123)
print(result)  # Output: (1, 2)
```

## Installation

This software is implemented in Python and does not require any external dependencies beyond the standard Python library. To use the software, ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory containing the `main.py` file.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can directly run the Python script or import the function into your own scripts.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: Import the `even_odd_count` function from the `main.py` file into your Python script.

   ```python
   from main import even_odd_count
   ```

2. **Call the Function**: Pass an integer to the `even_odd_count` function to get the count of even and odd digits.

   ```python
   result = even_odd_count(4567)
   print(result)  # Output: (2, 2)
   ```

## Documentation

The `even_odd_count` function is designed to be intuitive and easy to use. It handles both positive and negative integers by ignoring the sign and focusing solely on the digits.

- **Input**: An integer (e.g., `-123`, `456`)
- **Output**: A tuple with two integers representing the count of even and odd digits, respectively.

This software is ideal for applications that require digit analysis or preprocessing of numerical data for further computation.