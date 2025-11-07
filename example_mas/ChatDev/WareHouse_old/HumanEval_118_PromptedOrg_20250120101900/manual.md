# get_closest_vowel User Manual

## Introduction

The `get_closest_vowel` function is a Python utility designed to find the closest vowel that stands between two consonants from the right side of a given word. This function is case-sensitive and does not consider vowels at the beginning or end of the word. If no such vowel is found, the function returns an empty string.

## Main Functionality

- **Function Name**: `get_closest_vowel`
- **Purpose**: To identify the closest vowel that is flanked by consonants on both sides, starting from the right side of the word.
- **Input**: A single string `word` containing English letters only.
- **Output**: A single character string representing the closest vowel, or an empty string if no such vowel exists.

### Example Usage

```python
get_closest_vowel("yogurt")  # Returns "u"
get_closest_vowel("FULL")    # Returns "U"
get_closest_vowel("quick")   # Returns ""
get_closest_vowel("ab")      # Returns ""
```

## Installation

To use the `get_closest_vowel` function, you need to have Python installed on your system. You can download and install Python from the official [Python website](https://www.python.org/downloads/).

### Environment Setup

1. **Install Python**: Ensure Python is installed on your system. You can verify the installation by running `python --version` in your command line or terminal.

2. **Create a Virtual Environment** (optional but recommended):
   - Navigate to your project directory.
   - Run `python -m venv venv` to create a virtual environment named `venv`.
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS/Linux: `source venv/bin/activate`

3. **Install Dependencies**: There are no additional dependencies required for this function.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `get_closest_vowel` function.

2. **Run the Function**:
   - Open a Python interpreter or create a new Python script.
   - Import the function from `main.py` if necessary.
   - Call the `get_closest_vowel` function with your desired input.

### Example Script

```python
from main import get_closest_vowel

word = "yogurt"
result = get_closest_vowel(word)
print(f"The closest vowel in '{word}' is: '{result}'")
```

## Documentation

For further information and detailed documentation, please refer to the comments within the `main.py` file, which provide insights into the logic and structure of the `get_closest_vowel` function.

## Support

For any issues or questions regarding the use of this function, please contact our support team at support@chatdev.com. We are here to assist you with any inquiries you may have.