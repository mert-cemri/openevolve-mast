manual.md

```
# Select Words by Consonant Count

This software provides a utility function to extract words from a given string based on the number of consonants they contain. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function provided by this software is `select_words(s, n)`. This function takes two parameters:
- `s`: A string containing words separated by spaces.
- `n`: A natural number representing the exact number of consonants a word must have to be included in the result.

The function returns a list of words from the string `s` that contain exactly `n` consonants, preserving the order in which they appear in the string. If the input string `s` is empty, the function returns an empty list.

### Examples

- `select_words("Mary had a little lamb", 4)` returns `["little"]`
- `select_words("Mary had a little lamb", 3)` returns `["Mary", "lamb"]`
- `select_words("simple white space", 2)` returns `[]`
- `select_words("Hello world", 4)` returns `["world"]`
- `select_words("Uncle sam", 3)` returns `["Uncle"]`

## Installation

This software does not require any external libraries or dependencies. It is implemented in pure Python, and you can use it directly in your Python environment.

### Quick Start

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to the cloned repository:
   ```
   cd <repository-directory>
   ```

3. **Run the Code**: You can use the function directly in your Python scripts or interactive environment. Simply import the function and call it with the desired parameters.

## Usage

To use the `select_words` function, follow these steps:

1. **Import the Function**: Ensure that the `select_words` function is accessible in your Python environment. You can do this by placing the `main.py` file in your working directory or by importing it from the module where it is defined.

2. **Call the Function**: Use the function by passing a string and a natural number as arguments. For example:
   ```python
   from main import select_words

   result = select_words("Mary had a little lamb", 4)
   print(result)  # Output: ["little"]
   ```

3. **Interpret the Results**: The function will return a list of words that match the specified number of consonants.

## Documentation

For further details on the implementation and usage examples, refer to the comments within the `main.py` file. The function is designed to be intuitive and straightforward, making it easy to integrate into larger projects or use as a standalone utility.

```