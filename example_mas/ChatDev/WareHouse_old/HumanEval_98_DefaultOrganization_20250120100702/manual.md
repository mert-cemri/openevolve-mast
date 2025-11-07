# Count Uppercase Vowels in Even Indices

This software provides a simple function to count the number of uppercase vowels located at even indices within a given string. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The primary function of this software is:

- **`count_upper(s)`**: This function takes a single argument, a string `s`, and returns the count of uppercase vowels ('A', 'E', 'I', 'O', 'U') that appear at even indices in the string.

### Example Usage

- `count_upper('aBCdEf')` returns `1`
- `count_upper('abcdefg')` returns `0`
- `count_upper('dBBE')` returns `0`

## Installation

Since this software does not require any external dependencies, installation is straightforward. Simply ensure you have Python installed on your system.

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Move into the directory containing the `main.py` file:

   ```bash
   cd <directory-name>
   ```

3. **Run the Code**: You can directly run the `main.py` file using Python:

   ```bash
   python main.py
   ```

## How to Use

To utilize the `count_upper` function, you can either import it into your own Python script or run it directly from the command line.

### Importing into a Python Script

If you wish to use the function in your own script, you can import it as follows:

```python
from main import count_upper

result = count_upper('YourStringHere')
print(result)
```

### Running from the Command Line

You can also test the function directly by modifying the `main.py` file to include test cases or by using an interactive Python shell.

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is well-documented with a docstring explaining its purpose and usage.

## Support

For any issues or questions, please contact our support team or refer to the documentation within the code. We are committed to providing assistance and ensuring the software meets your needs.