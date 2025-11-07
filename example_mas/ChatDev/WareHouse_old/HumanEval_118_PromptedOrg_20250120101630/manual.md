# ChatDev Vowel Finder

## Overview

The Vowel Finder is a Python-based utility that identifies the closest vowel in a given word that stands between two consonants from the right side of the word. This tool is designed to work with English letters and is case-sensitive. It excludes vowels at the beginning and end of the word from consideration.

## Main Function

### `get_closest_vowel(word)`

- **Purpose**: Finds the closest vowel that stands between two consonants from the right side of the word.
- **Parameters**: 
  - `word` (str): A string containing the word to be analyzed.
- **Returns**: 
  - A single character string representing the closest vowel found under the specified conditions.
  - Returns an empty string if no such vowel is found.

### Examples

- `get_closest_vowel("yogurt")` returns `"u"`
- `get_closest_vowel("FULL")` returns `"U"`
- `get_closest_vowel("quick")` returns `""`
- `get_closest_vowel("ab")` returns `""`

## Installation

### Environment Setup

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Quick Install

Since there are no external dependencies, you can directly use the provided Python script without any additional installation steps.

## Usage

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file to your local machine.

2. **Run the Script**: Execute the script using Python. You can test the function by calling it with different words.

   ```bash
   python main.py
   ```

3. **Example Usage**: You can modify the script to include test cases or use an interactive Python shell to test the function.

   ```python
   from main import get_closest_vowel

   print(get_closest_vowel("yogurt"))  # Output: "u"
   print(get_closest_vowel("FULL"))    # Output: "U"
   print(get_closest_vowel("quick"))   # Output: ""
   print(get_closest_vowel("ab"))      # Output: ""
   ```

## Documentation

For further information on how the function works, refer to the docstring within the `main.py` file. The function is well-documented to provide insights into its logic and usage.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to assist you with any inquiries or technical support you may need.