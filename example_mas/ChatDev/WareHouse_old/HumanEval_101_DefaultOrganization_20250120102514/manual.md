# Words String Splitter

This software provides a simple function to split a string of words separated by commas or spaces into a list of words. It is designed to be straightforward and efficient, making it easy to integrate into larger projects or use as a standalone utility.

## Main Functionality

The primary function of this software is `words_string(s)`, which takes a single string input and returns a list of words. The function handles strings where words are separated by either commas or spaces, ensuring that the output is a clean list of words without any punctuation.

### Example Usage

```python
from main import words_string

# Example 1
result1 = words_string("Hi, my name is John")
print(result1)  # Output: ['Hi', 'my', 'name', 'is', 'John']

# Example 2
result2 = words_string("One, two, three, four, five, six")
print(result2)  # Output: ['One', 'two', 'three', 'four', 'five', 'six']
```

## Installation

### Environment Setup

To use this software, you need to have Python installed on your system. The function itself does not require any additional dependencies, making it lightweight and easy to use.

1. **Install Python**: If you haven't already, download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change into the directory where the repository is cloned:
   ```bash
   cd <repository-directory>
   ```

### Running the Code

Once you have set up your environment, you can run the code directly using Python.

```bash
python main.py
```

## How to Use

1. **Import the Function**: Import the `words_string` function from the `main.py` file into your Python script or interactive shell.

2. **Call the Function**: Pass a string of words separated by commas or spaces to the function and receive a list of words as the output.

3. **Integrate into Projects**: You can integrate this function into larger projects where text processing is required.

## Documentation

For more detailed documentation and examples, please refer to the source code comments in `main.py`. The function is well-documented with examples to help you understand its usage quickly.

## Support

For any issues or questions, please contact our support team or open an issue in the repository. We are committed to providing assistance and improving the software based on user feedback.