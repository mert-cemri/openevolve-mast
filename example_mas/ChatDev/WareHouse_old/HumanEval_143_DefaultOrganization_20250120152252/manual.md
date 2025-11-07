manual.md

```
# Prime Length Words Filter

This software module provides a function to filter words in a sentence based on the length of the words being prime numbers. It is a simple yet effective tool for processing text data where you need to extract words of prime lengths.

## Main Functionality

The main function provided by this module is `words_in_sentence(sentence)`. This function takes a sentence as input and returns a string containing only the words whose lengths are prime numbers. The order of the words in the returned string is the same as in the original sentence.

### Example Usage

```python
# Example usage:
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
```

## Installation

This module does not require any external dependencies, making it easy to integrate into your existing Python projects. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the code is located.
   ```
   cd <directory-name>
   ```

3. **Run the Code**: You can directly run the `main.py` file to test the function.
   ```
   python main.py
   ```

## How to Use

1. **Import the Function**: If you are integrating this function into another project, you can import it as follows:
   ```python
   from main import words_in_sentence
   ```

2. **Call the Function**: Pass a sentence to the `words_in_sentence` function to get the words with prime lengths.
   ```python
   result = words_in_sentence("Your sentence here")
   print(result)
   ```

## Understanding Prime Numbers

A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. In this module, the `is_prime(n)` function is used to determine if a number is prime. This function is efficient and handles numbers up to the length constraints specified.

## Conclusion

This module is a straightforward solution for filtering words based on prime lengths. It is lightweight, with no external dependencies, making it easy to use and integrate into various applications where text processing is required.

For any further assistance or queries, please contact our support team.
```
