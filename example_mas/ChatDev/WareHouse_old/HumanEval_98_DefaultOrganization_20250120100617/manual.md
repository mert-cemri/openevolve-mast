# Count Uppercase Vowels in Even Indices

This software provides a simple function to count the number of uppercase vowels located at even indices in a given string. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The core function of this software is `count_upper(s)`, which takes a string `s` as input and returns the count of uppercase vowels ('A', 'E', 'I', 'O', 'U') that are located at even indices of the string.

### Example Usage

```python
# Example usage of the count_upper function
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))    # Output: 0
```

## Installation

Since this software does not require any external libraries, there is no need to install additional dependencies. You only need Python installed on your system.

### Python Installation

Ensure you have Python installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

## How to Use

1. **Clone or Download the Repository:**

   You can clone the repository using Git or download the ZIP file and extract it.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Open a terminal and navigate to the directory where the `main.py` file is located.

   ```bash
   cd path/to/directory
   ```

3. **Run the Script:**

   Execute the `main.py` script using Python to see the example outputs or modify the script to test with different strings.

   ```bash
   python main.py
   ```

4. **Modify for Custom Input:**

   You can modify the `main.py` file to test the `count_upper` function with different strings by changing the arguments passed to the function in the example usage section.

## Documentation

The function is straightforward and does not require extensive documentation. The logic is implemented in a single function `count_upper(s)` which iterates over the string `s`, checking only the even indices for uppercase vowels and counting them.

For any further questions or support, please contact our support team or refer to the comments within the code for guidance on how the function operates.