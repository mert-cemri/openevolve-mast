# Count Uppercase Vowels at Even Indices

This software provides a function to count the number of uppercase vowels located at even indices in a given string. It is a simple utility function written in Python.

## Main Functionality

The main function of this software is `count_upper(s)`, which takes a string `s` as input and returns the count of uppercase vowels ('A', 'E', 'I', 'O', 'U') that appear at even indices in the string.

### Example Usage

- `count_upper('aBCdEf')` returns `1`
- `count_upper('abcdefg')` returns `0`
- `count_upper('dBBE')` returns `0`

## Installation

This software does not require any external dependencies beyond Python itself. To use the function, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

## How to Use

1. **Clone the Repository:**
   - Download or clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory:**
   - Open a terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Python Script:**
   - You can use the function in a Python script or an interactive Python session. Here’s how you can use it in an interactive session:

   ```bash
   python
   ```

   ```python
   from main import count_upper

   # Test the function with a sample input
   result = count_upper('aBCdEf')
   print(result)  # Output: 1
   ```

4. **Integrate into Your Project:**
   - You can also import the `count_upper` function into your own Python projects and use it as needed.

## Additional Information

- **No External Dependencies:** This software does not require any additional Python packages to function.
- **Python Version:** Ensure you are using Python 3.x for compatibility.

This utility is designed to be simple and efficient for counting uppercase vowels at even indices in strings, making it a useful tool for text processing tasks.