manual.md

```
# Get Closest Vowel

This software provides a function to find the closest vowel that stands between two consonants from the right side of a given word. The function is designed to handle case-sensitive inputs and excludes vowels at the beginning and end of the word.

## Main Function

### `get_closest_vowel(word)`

- **Description**: This function takes a word as input and returns the closest vowel that stands between two consonants from the right side of the word. If no such vowel exists, it returns an empty string.

- **Parameters**: 
  - `word` (str): The input word containing only English letters.

- **Returns**: 
  - (str): The closest vowel between two consonants from the right side of the word, or an empty string if no such vowel exists.

- **Examples**:
  - `get_closest_vowel("yogurt")` returns `"u"`
  - `get_closest_vowel("FULL")` returns `"U"`
  - `get_closest_vowel("quick")` returns `""`
  - `get_closest_vowel("ab")` returns `""`

## Installation

This software does not have any external dependencies, so no installation of additional packages is required. Simply ensure that you have Python installed on your system.

## Usage

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Script**: Execute the script using Python to test the function with example inputs. You can modify the example usage section in the script to test with different words.

   ```bash
   python main.py
   ```

4. **Integrate into Your Project**: You can copy the `get_closest_vowel` function into your own Python project and use it as needed.

## Notes

- The function assumes that the input string contains only English letters.
- The function is case-sensitive, meaning it distinguishes between uppercase and lowercase vowels.
- Vowels at the beginning and end of the word are not considered for the purpose of this function.

Feel free to modify the code to suit your specific needs or to integrate it into larger projects.
```