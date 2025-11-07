# Words in Sentence Filter

This software module is designed to filter words from a given sentence based on the length of the words being prime numbers. It provides a simple and efficient way to extract words whose lengths are prime numbers, maintaining the order of the words as they appear in the original sentence.

## Main Functions

### `words_in_sentence(sentence)`

- **Description**: This function takes a string representing a sentence and returns a string containing only the words whose lengths are prime numbers.
- **Parameters**: 
  - `sentence` (str): A string containing words separated by spaces.
- **Returns**: 
  - A string with words from the original sentence whose lengths are prime numbers, separated by spaces.

### `is_prime(n)`

- **Description**: A helper function to determine if a given integer is a prime number.
- **Parameters**: 
  - `n` (int): The integer to check for primality.
- **Returns**: 
  - `True` if `n` is a prime number, `False` otherwise.

## Quick Install

This software does not require any external dependencies, so installation is straightforward. Ensure you have Python installed on your system.

1. **Clone the Repository**: Clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the Directory**: Change into the directory containing the code.
   ```bash
   cd <repository-directory>
   ```

## How to Use

1. **Open the `main.py` file**: This file contains the implementation of the `words_in_sentence` function.
2. **Run the Function**: You can test the function by calling it with a sentence as an argument. For example:
   ```python
   print(words_in_sentence("This is a test"))  # Output: "is"
   print(words_in_sentence("lets go for swimming"))  # Output: "go for"
   ```
3. **Modify as Needed**: You can modify the `main.py` file to include more test cases or integrate it into a larger application.

## Example Usage

Here's a simple example of how to use the `words_in_sentence` function:

```python
# Example usage:
sentence = "This is a test"
result = words_in_sentence(sentence)
print(result)  # Output: "is"

sentence = "lets go for swimming"
result = words_in_sentence(sentence)
print(result)  # Output: "go for"
```

## Documentation

For further information and documentation, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the functions.

Feel free to reach out for support or contribute to the project by submitting issues or pull requests.