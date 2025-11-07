# get_closest_vowel User Manual

## Introduction

The `get_closest_vowel` function is a simple Python utility designed to find the closest vowel that stands between two consonants from the right side of a given word. This function is case-sensitive and excludes vowels at the beginning and end of the word. If no such vowel is found, the function returns an empty string.

### Key Features

- Identifies vowels between consonants in a word.
- Case-sensitive operation.
- Excludes vowels at the beginning and end of the word.

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

## Usage

To use the `get_closest_vowel` function, follow these steps:

1. **Clone or Download the Repository:**
   - Clone the repository to your local machine using `git clone` or download the ZIP file and extract it.

2. **Navigate to the Directory:**
   - Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Function:**
   - You can test the function by running the script in a Python environment. Open a Python shell or create a script that imports `get_closest_vowel` and call the function with a word as an argument.

### Example Usage

```python
# Import the function from the main.py file
from main import get_closest_vowel

# Test cases
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))    # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))      # Output: ""
```

## Documentation

The function is straightforward and does not require additional configuration or setup. For any further questions or issues, please refer to the comments within the `main.py` file, which provide a detailed explanation of the function's logic and usage.

## Support

For support or inquiries, please contact our support team at support@chatdev.com. We are here to help you with any questions or issues you may encounter while using the `get_closest_vowel` function.