manual.md

```
# get_closest_vowel Function

## Introduction

The `get_closest_vowel` function is a Python utility designed to identify the closest vowel that stands between two consonants from the right side of a given word. This function is case-sensitive and excludes vowels at the beginning and end of the word. If no such vowel is found, the function returns an empty string.

## Main Functionality

- **Function Name:** `get_closest_vowel`
- **Input:** A single string `word` containing English letters only.
- **Output:** A single character representing the closest vowel between two consonants or an empty string if no such vowel exists.

### Example Usage

```python
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))    # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))      # Output: ""
```

## Installation

### Environment Setup

To use the `get_closest_vowel` function, ensure you have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/downloads/).

### Dependencies

This function does not require any external Python packages, so there is no need for a `requirements.txt` file or additional installations.

## How to Use

1. **Clone or Download the Repository:**

   You can clone the repository or download the `main.py` file containing the `get_closest_vowel` function.

2. **Run the Function:**

   Open a terminal or command prompt, navigate to the directory containing the `main.py` file, and run the Python script using the following command:

   ```bash
   python main.py
   ```

3. **Modify the Code:**

   You can modify the `main.py` file to test the function with different words by changing the input to the `get_closest_vowel` function.

## Additional Information

- The function iterates through the word from the second last character to the second character, checking for vowels that are flanked by consonants.
- The function is designed to handle both uppercase and lowercase letters, ensuring case sensitivity is maintained.

For further assistance or inquiries, please contact our support team at support@chatdev.com.
```