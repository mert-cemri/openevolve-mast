# Select Words User Manual

## Introduction

The `select_words` function is a Python utility designed to extract words from a given string that contain a specified number of consonants. This function is particularly useful for text analysis tasks where consonant count is a criterion for word selection.

## Main Functionality

The primary function of this software is:

- **select_words(s, n):** This function takes a string `s` and a natural number `n` as input. It returns a list of words from the string `s` that contain exactly `n` consonants. The words are returned in the order they appear in the string. If the input string is empty, the function returns an empty list.

### Example Usage

```python
select_words("Mary had a little lamb", 4)  # Returns: ["little"]
select_words("Mary had a little lamb", 3)  # Returns: ["Mary", "lamb"]
select_words("simple white space", 2)     # Returns: []
select_words("Hello world", 4)            # Returns: ["world"]
select_words("Uncle sam", 3)              # Returns: ["Uncle"]
```

## Installation

To use the `select_words` function, you need to have Python installed on your system. The function does not require any additional dependencies beyond the standard Python library.

### Step-by-Step Installation

1. **Install Python:**
   - Download and install Python from the official website: [python.org](https://www.python.org/).
   - Follow the installation instructions for your operating system.

2. **Clone or Download the Script:**
   - You can clone the repository or download the `main.py` file containing the `select_words` function.

3. **Run the Script:**
   - Navigate to the directory containing `main.py` in your terminal or command prompt.
   - Run the script using Python:
     ```bash
     python main.py
     ```

## Usage

To use the `select_words` function in your own projects:

1. **Import the Function:**
   - Ensure that `main.py` is in your project directory.
   - Import the function at the beginning of your script:
     ```python
     from main import select_words
     ```

2. **Call the Function:**
   - Use the function by passing a string and a natural number as arguments:
     ```python
     result = select_words("Your input string here", 3)
     print(result)
     ```

## Documentation

For further details on how the function works, refer to the comments within the `main.py` file. The function is straightforward and does not require any additional libraries or frameworks.

## Support

If you encounter any issues or have questions regarding the `select_words` function, please reach out to our support team through our official website or contact us via email.

---

This manual provides all necessary information to effectively use the `select_words` function for your text processing needs.