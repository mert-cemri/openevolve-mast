# get_closest_vowel User Manual

Welcome to the `get_closest_vowel` function user manual. This document will guide you through the main functionalities of the software, how to set up the environment, and how to use the function effectively.

## Overview

The `get_closest_vowel` function is designed to identify the closest vowel that stands between two consonants from the right side of a given word. The function is case-sensitive and only considers vowels that are not at the beginning or end of the word. If no such vowel is found, the function returns an empty string.

### Main Functionality

- **Function Name**: `get_closest_vowel`
- **Input**: A single word (string) containing English letters only.
- **Output**: The closest vowel (string) that stands between two consonants from the right side of the word, or an empty string if no such vowel exists.

### Examples

- `get_closest_vowel("yogurt")` returns `"u"`
- `get_closest_vowel("FULL")` returns `"U"`
- `get_closest_vowel("quick")` returns `""`
- `get_closest_vowel("ab")` returns `""`

## Installation

### Environment Setup

This function does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Python Installation

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

## Usage

To use the `get_closest_vowel` function, follow these steps:

1. **Create a Python File**: Open your preferred text editor or IDE and create a new Python file, e.g., `main.py`.

2. **Copy the Function Code**: Copy the following code into your `main.py` file:

    ```python
    def get_closest_vowel(word):
        vowels = "AEIOUaeiou"
        length = len(word)
        # Start from the second last character and move to the second character
        for i in range(length - 2, 0, -1):
            if word[i] in vowels:
                if word[i - 1] not in vowels and word[i + 1] not in vowels:
                    return word[i]
        return ""
    
    # Example usage
    print(get_closest_vowel("yogurt"))  # Output: "u"
    print(get_closest_vowel("FULL"))    # Output: "U"
    print(get_closest_vowel("quick"))   # Output: ""
    print(get_closest_vowel("ab"))      # Output: ""
    ```

3. **Run the Code**: Execute the `main.py` file using a Python interpreter. You can do this by opening a terminal or command prompt, navigating to the directory containing `main.py`, and running the command:

    ```bash
    python main.py
    ```

4. **Observe the Output**: The function will print the results of the example usages provided in the code.

## Conclusion

The `get_closest_vowel` function is a simple yet effective tool for identifying vowels between consonants in a word. With no external dependencies required, it is easy to integrate into any Python project. For any further questions or support, please feel free to reach out.