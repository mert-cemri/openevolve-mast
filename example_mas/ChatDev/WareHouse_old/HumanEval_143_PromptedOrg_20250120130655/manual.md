# Words in Sentence Filter

This software module provides a function to filter words from a sentence based on the prime length of the words. It is designed to help users extract words from a given sentence where the length of each word is a prime number.

## Main Functions

### `words_in_sentence(sentence)`

- **Description**: This function takes a sentence as input and returns a string containing words from the original sentence whose lengths are prime numbers. The order of the words in the new string is the same as in the original sentence.

- **Parameters**: 
  - `sentence` (str): The input sentence containing words separated by spaces.

- **Returns**: 
  - `str`: A string of words with prime lengths, separated by spaces.

- **Example Usage**:
  ```python
  print(words_in_sentence("This is a test"))  # Output: "is"
  print(words_in_sentence("lets go for swimming"))  # Output: "go for"
  ```

## Installation

To use this software, ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Script**: You can run the script using Python by executing the following command:
   ```bash
   python main.py
   ```

4. **Use the Function**: You can use the `words_in_sentence` function in your own scripts by importing it:
   ```python
   from main import words_in_sentence

   result = words_in_sentence("Your sentence here")
   print(result)
   ```

## Dependencies

This module does not require any external dependencies beyond the standard Python library.

## Documentation

For further information or questions, please refer to the comments within the `main.py` file, which provide detailed explanations of the functions and their usage. If you have any issues or need support, please contact our support team.