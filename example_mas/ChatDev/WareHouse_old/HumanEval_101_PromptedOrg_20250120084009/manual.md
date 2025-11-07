# Words String Splitter

This software provides a simple utility function to split a string of words separated by commas or spaces into an array of individual words. It is designed to handle strings with mixed delimiters and return a clean list of words.

## Main Functionality

The primary function provided by this software is `words_string(s)`, which takes a single string input and returns a list of words. The function processes the string by replacing commas with spaces, splitting the string by spaces, and filtering out any empty strings that may result from consecutive spaces or trailing spaces.

### Example Usage

```python
from main import words_string

# Example 1
result1 = words_string("Hi, my name is John")
print(result1)  # Output: ["Hi", "my", "name", "is", "John"]

# Example 2
result2 = words_string("One, two, three, four, five, six")
print(result2)  # Output: ["One", "two", "three", "four", "five", "six"]
```

## Installation

This software is implemented in Python and does not require any external dependencies beyond the standard Python library. To use this software, ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change to the directory where the repository is cloned:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code:**

   You can directly run the Python script using:

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function:**

   Import the `words_string` function from the `main.py` file in your Python script.

   ```python
   from main import words_string
   ```

2. **Call the Function:**

   Pass a string to the `words_string` function to get a list of words.

   ```python
   words = words_string("Your, example string here")
   print(words)
   ```

## Documentation

This software is straightforward and does not require extensive documentation. The function is designed to handle typical use cases of splitting strings into words based on spaces and commas. For any additional information or support, please refer to the comments within the code or contact the development team.

---

This manual provides all necessary information to install and use the software effectively. For any further assistance, feel free to reach out to our support team.