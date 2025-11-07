manual.md

```
# Select Words by Consonant Count

This software provides a function to extract words from a given string that contain a specified number of consonants. It's a simple utility function that can be used in various text processing applications.

## Main Functionality

The main function provided by this software is `select_words(s, n)`, which performs the following tasks:

- Takes a string `s` and a natural number `n` as inputs.
- Returns a list of words from the string `s` that contain exactly `n` consonants.
- If the input string `s` is empty, the function returns an empty list.
- The function assumes that the input string contains only letters and spaces.

### Example Usage

```python
# Example usage:
print(select_words("Mary had a little lamb", 4))  # Output: ["little"]
print(select_words("Mary had a little lamb", 3))  # Output: ["Mary", "lamb"]
print(select_words("simple white space", 2))      # Output: []
print(select_words("Hello world", 4))             # Output: ["world"]
print(select_words("Uncle sam", 3))               # Output: ["Uncle"]
```

## Installation

### Environment Setup

To use this software, you need to have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/downloads/).

### Dependencies

This software does not require any external Python packages beyond the standard library, so no additional dependencies need to be installed.

## How to Use

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change your working directory to the location where you cloned the repository:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Script:**

   You can run the script using Python by executing the following command:

   ```bash
   python main.py
   ```

   This will allow you to test the function with the example usage provided in the script.

## Documentation

For further details on how the function works, you can refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the function.

## Support

If you encounter any issues or have questions about using this software, please feel free to contact our support team at support@chatdev.com.

```