# get_closest_vowel User Manual

Welcome to the `get_closest_vowel` function manual. This document will guide you through the purpose, installation, and usage of the software.

## Overview

The `get_closest_vowel` function is a Python utility designed to find the closest vowel that stands between two consonants from the right side of a given word. The function is case-sensitive and does not consider vowels at the beginning or end of the word. If no such vowel is found, the function returns an empty string.

### Key Features

- **Case-Sensitive:** The function distinguishes between uppercase and lowercase vowels.
- **Consonant Check:** Only returns vowels that are flanked by consonants.
- **Right-to-Left Search:** The search for the vowel starts from the right side of the word.

### Example Usage

- `get_closest_vowel("yogurt")` returns `"u"`.
- `get_closest_vowel("FULL")` returns `"U"`.
- `get_closest_vowel("quick")` returns `""`.
- `get_closest_vowel("ab")` returns `""`.

## Installation

This function does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Python Installation:** Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository:** If the function is part of a larger project, clone the repository using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory:**
   ```bash
   cd <project-directory>
   ```

## Usage

To use the `get_closest_vowel` function, follow these steps:

1. **Open a Python Environment:** You can use any Python environment like IDLE, PyCharm, or VSCode.

2. **Import the Function:** If the function is part of a module, import it using:
   ```python
   from main import get_closest_vowel
   ```

3. **Call the Function:** Pass a word as an argument to the function:
   ```python
   result = get_closest_vowel("yogurt")
   print(result)  # Output: "u"
   ```

## Documentation

For further details, refer to the function's docstring or comments within the code. The function is straightforward and designed to be easily integrated into larger projects.

## Support

For any issues or questions, please contact our support team or refer to the project's repository for more information.

Thank you for using the `get_closest_vowel` function!