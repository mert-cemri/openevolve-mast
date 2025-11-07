# Select Words User Manual

## Introduction

The `select_words` function is a Python utility designed to extract words from a given string that contain a specific number of consonants. This function is particularly useful for text analysis tasks where identifying words based on their consonant count is required.

## Main Functionality

- **Function Name**: `select_words`
- **Purpose**: To return a list of words from a string that contain exactly `n` consonants.
- **Input**: 
  - `s`: A string containing words separated by spaces.
  - `n`: A natural number representing the exact number of consonants a word must have to be included in the result.
- **Output**: A list of words from the input string `s` that contain exactly `n` consonants.

### Example Usage

```python
select_words("Mary had a little lamb", 4)  # Returns: ["little"]
select_words("Mary had a little lamb", 3)  # Returns: ["Mary", "lamb"]
select_words("simple white space", 2)     # Returns: []
select_words("Hello world", 4)            # Returns: ["world"]
select_words("Uncle sam", 3)              # Returns: ["Uncle"]
```

## Installation

This project does not require any external dependencies, so no additional installation steps are necessary beyond having Python installed on your system.

### Python Installation

Ensure you have Python installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your working directory to where the `main.py` file is located.

   ```bash
   cd <project-directory>
   ```

3. **Run the Function**: You can use the function by importing it into your Python script or interactive session.

   ```python
   from main import select_words

   # Example usage
   result = select_words("Mary had a little lamb", 4)
   print(result)  # Output: ["little"]
   ```

## Documentation

The function is self-contained and does not require additional documentation beyond the provided docstring. The docstring within the `main.py` file provides a detailed explanation of the function's purpose, inputs, and outputs.

## Support

For any issues or questions regarding the usage of the `select_words` function, please contact our support team at support@chatdev.com.

---

This manual provides all necessary information to effectively use the `select_words` function for extracting words based on consonant count from a given string.