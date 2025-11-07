manual.md

```
# Get Closest Vowel

This software provides a simple utility function `get_closest_vowel` that identifies the closest vowel standing between two consonants from the right side of a given word. This function is case-sensitive and excludes vowels at the beginning and end of the word.

## Main Functionality

The main function of this software is:

- **get_closest_vowel(word):** This function takes a single argument, `word`, which is a string containing English letters only. It returns the closest vowel that stands between two consonants from the right side of the word. If no such vowel is found, it returns an empty string.

### Example Usage

```python
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))    # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))      # Output: ""
```

## Installation

This software is implemented in Python. To use it, ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change your current directory to the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies:**

   This project does not have any external dependencies listed in `requirements.txt`. However, ensure your Python environment is set up correctly.

## How to Use

1. **Run the Script:**

   You can run the script directly to test the function with example inputs:

   ```bash
   python main.py
   ```

   This will execute the example usage code and print the results to the console.

2. **Integrate into Your Project:**

   To use the `get_closest_vowel` function in your own project, simply import it from `main.py`:

   ```python
   from main import get_closest_vowel

   # Use the function in your code
   result = get_closest_vowel("example")
   print(result)
   ```

## Documentation

For further details on how the function works, refer to the docstring provided within the `main.py` file. The docstring includes a description of the function, its parameters, and example usage.

Feel free to modify and extend the code to suit your specific needs. If you encounter any issues or have questions, please reach out to our support team.
```