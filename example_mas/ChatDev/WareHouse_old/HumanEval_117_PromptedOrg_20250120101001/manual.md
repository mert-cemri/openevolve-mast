manual.md

```
# Select Words Application

This application provides a function to extract words from a given string that contain exactly a specified number of consonants. It is designed to be simple and efficient, requiring no external dependencies.

## Main Functionality

The main function of this application is `select_words`, which takes a string and a natural number as input and returns a list of words from the string that contain exactly the specified number of consonants.

### Function: `select_words`

- **Input**: 
  - `s` (string): A string containing words separated by spaces. The string may contain only letters and spaces.
  - `n` (int): A natural number representing the exact number of consonants a word must have to be included in the output list.

- **Output**: 
  - A list of words from the input string `s` that contain exactly `n` consonants.

- **Examples**:
  - `select_words("Mary had a little lamb", 4)` returns `["little"]`
  - `select_words("Mary had a little lamb", 3)` returns `["Mary", "lamb"]`
  - `select_words("simple white space", 2)` returns `[]`
  - `select_words("Hello world", 4)` returns `["world"]`
  - `select_words("Uncle sam", 3)` returns `["Uncle"]`

## Installation

This application does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: 
   - Clone the repository to your local machine using `git clone <repository-url>`.

2. **Navigate to the Directory**:
   - Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**:
   - You can use the function by importing it into your Python script or by running it directly in a Python interactive shell.
   - Example usage in a Python script:
     ```python
     from main import select_words

     result = select_words("Mary had a little lamb", 4)
     print(result)  # Output: ["little"]
     ```

4. **Testing**:
   - You can test the function with different input strings and numbers to ensure it works as expected.

## Conclusion

The Select Words application is a straightforward tool for extracting words with a specific number of consonants from a string. Its simplicity and lack of dependencies make it easy to integrate into larger projects or use as a standalone utility.
```