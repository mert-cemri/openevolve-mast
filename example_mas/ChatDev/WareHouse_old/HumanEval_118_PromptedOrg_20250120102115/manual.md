# get_closest_vowel User Manual

Welcome to the `get_closest_vowel` function user manual. This document will guide you through the main functionalities of the software, how to install the necessary environment dependencies, and how to use the function effectively.

## Overview

The `get_closest_vowel` function is designed to identify the closest vowel in a given word that stands between two consonants, starting from the right side of the word. The function is case-sensitive and does not consider vowels at the beginning or end of the word. If no such vowel is found, the function returns an empty string.

### Main Functionality

- **Function Name:** `get_closest_vowel`
- **Input:** A single word (string) containing English letters only.
- **Output:** The closest vowel (string) that stands between two consonants from the right side of the word. Returns an empty string if no such vowel exists.

### Example Usage

```python
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))    # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))      # Output: ""
```

## Installation

### Environment Setup

To use the `get_closest_vowel` function, you need to have Python installed on your system. The function does not require any additional libraries or dependencies, so you can directly use it in your Python environment.

### Quick Install

1. **Ensure Python is installed:** You can download and install Python from the official website: [python.org](https://www.python.org/).

2. **Clone or download the script:** Save the `main.py` file containing the `get_closest_vowel` function to your local machine.

3. **Run the script:** You can execute the script using a Python interpreter. Open a terminal or command prompt and navigate to the directory where `main.py` is located. Run the following command:

   ```bash
   python main.py
   ```

## How to Use

1. **Open the script:** Open the `main.py` file in a text editor or an integrated development environment (IDE) of your choice.

2. **Call the function:** Use the `get_closest_vowel` function by passing a word as an argument. You can modify the script to include different words and test the function's output.

3. **View the results:** The function will return the closest vowel that meets the specified conditions. You can print the result to the console or use it in further computations.

## Conclusion

The `get_closest_vowel` function is a simple yet effective tool for identifying vowels in specific positions within a word. With no additional dependencies required, it is easy to integrate into any Python-based project. Feel free to explore and modify the function to suit your needs.