# Histogram Function User Manual

## Introduction

The Histogram function is a Python-based utility designed to analyze a string of space-separated lowercase letters and return a dictionary containing the letter(s) with the highest frequency of occurrence along with their respective counts. This tool is particularly useful for text analysis and frequency distribution tasks.

## Main Functionality

The primary function provided by this software is:

- `histogram(test)`: This function takes a single string input, `test`, which consists of space-separated lowercase letters. It returns a dictionary where the keys are the letters with the highest frequency, and the values are their respective counts. If multiple letters have the same maximum frequency, all such letters are included in the dictionary.

### Example Usage

```python
# Example usage of the histogram function
result = histogram('a b c a b')
print(result)  # Output: {'a': 2, 'b': 2}
```

## Installation

### Environment Setup

This project does not require any external dependencies, making it straightforward to set up and use. You only need to have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository containing the `main.py` file, clone it to your local machine.

3. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where `main.py` is located.

## How to Use

1. **Open the Python Environment**: You can use any Python environment, such as IDLE, PyCharm, or simply the command line.

2. **Import the Function**: If you have the `main.py` file in your project directory, you can import the `histogram` function.

   ```python
   from main import histogram
   ```

3. **Call the Function**: Use the `histogram` function by passing a string of space-separated lowercase letters.

   ```python
   result = histogram('a b b a')
   print(result)  # Output: {'a': 2, 'b': 2}
   ```

4. **Interpret the Results**: The function will return a dictionary with the letter(s) that have the highest frequency and their counts.

## Conclusion

The Histogram function is a simple yet powerful tool for analyzing the frequency of letters in a string. With no external dependencies, it is easy to integrate into any Python project. Whether you are conducting text analysis or simply exploring letter distributions, this function provides a quick and efficient solution.