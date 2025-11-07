manual.md

```
# Distinct Character Counter

This software provides a simple function to count the number of distinct characters in a given string, ignoring case sensitivity. It is implemented in Python and is designed to be straightforward and efficient.

## Main Functionality

The core functionality of this software is encapsulated in the `count_distinct_characters` function. This function takes a single string as input and returns the number of distinct characters present in the string, regardless of their case.

### Function Signature

```python
def count_distinct_characters(string: str) -> int:
```

### Example Usage

```python
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
```

## Installation

There are no external dependencies required for this software, making it easy to set up and use. You only need to have Python installed on your system.

### Step-by-Step Installation Guide

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository:**
   - Clone the repository or download the source code files to your local machine.

3. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory where the source code is located.

4. **Run the Code:**
   - You can directly run the `main.py` file to test the function. Use a Python interpreter to execute the script.

## How to Use

1. **Open a Python Environment:**
   - You can use any Python environment such as IDLE, PyCharm, or a simple terminal.

2. **Import the Function:**
   - If you are using the function in another script, import it using:
     ```python
     from main import count_distinct_characters
     ```

3. **Call the Function:**
   - Pass a string to the function and receive the count of distinct characters:
     ```python
     result = count_distinct_characters('YourStringHere')
     print(result)
     ```

## Additional Information

- **Case Insensitivity:** The function automatically converts all characters to lowercase to ensure case insensitivity.
- **Efficiency:** The use of a set to store characters ensures that the function runs efficiently even for longer strings.

This software is designed to be simple and effective for counting distinct characters in any given string. Enjoy using it for your text processing needs!
```