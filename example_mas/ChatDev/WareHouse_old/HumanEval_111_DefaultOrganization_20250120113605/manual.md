# Histogram Function User Manual

Welcome to the user manual for the Histogram Function. This document will guide you through the main functionalities of the software, how to set up your environment, and how to use the function effectively.

## Introduction

The Histogram Function is a simple Python utility designed to analyze a string of space-separated lowercase letters and return a dictionary of the letter(s) with the highest frequency, along with their corresponding count. This function is useful for text analysis tasks where identifying the most frequently occurring letters is required.

## Main Functionality

The main function provided by this software is:

- **histogram(test: str) -> dict**: This function takes a string input, splits it into individual letters, counts the frequency of each letter, and returns a dictionary containing the letter(s) with the highest frequency and their count.

### Example Usage

```python
# Example 1
result = histogram('a b c')
print(result)  # Output: {'a': 1, 'b': 1, 'c': 1}

# Example 2
result = histogram('a b b a')
print(result)  # Output: {'a': 2, 'b': 2}

# Example 3
result = histogram('b b b b a')
print(result)  # Output: {'b': 4}

# Example 4
result = histogram('')
print(result)  # Output: {}
```

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need to have Python installed on your system.

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

3. **Run the Code**: You can directly run the `main.py` file using Python:
   ```bash
   python main.py
   ```

## Usage

To use the histogram function, you can import it into your Python script or interactive session. Here's how you can do it:

```python
from main import histogram

# Use the function with your input string
result = histogram('your input string here')
print(result)
```

## Conclusion

The Histogram Function is a lightweight and efficient tool for counting letter frequencies in a string. With no external dependencies, it is easy to integrate into your projects. We hope this manual helps you get started quickly and effectively. If you have any questions or need further assistance, please feel free to reach out.