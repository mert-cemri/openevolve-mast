# Prime Length Words Filter

This software module provides a function to filter words in a sentence based on the length of the words being prime numbers. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function of this software is `words_in_sentence(sentence)`, which takes a sentence as input and returns a string containing the words from the original sentence whose lengths are prime numbers. The order of the words in the returned string is the same as in the original sentence.

### Example Usage

```python
# Example usage:
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
```

## Installation

No external dependencies are required for this software. It is implemented purely in Python, and you can run it in any standard Python environment.

### Requirements

- Python 3.x

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

    ```bash
    cd <repository-directory>
    ```

3. **Run the Code**: You can run the `main.py` file directly using Python to test the function with your own sentences.

    ```bash
    python main.py
    ```

4. **Integrate into Your Project**: If you want to use the `words_in_sentence` function in your own project, simply copy the function and the helper function `is_prime` into your codebase.

## Understanding the Code

- **`is_prime(n)`**: This helper function checks if a given number `n` is a prime number. It returns `True` if `n` is prime and `False` otherwise.

- **`words_in_sentence(sentence)`**: This function splits the input sentence into words, checks the length of each word, and filters out the words whose lengths are prime numbers. It then joins these words back into a single string and returns it.

## Conclusion

This software provides a straightforward solution to filter words based on prime number lengths. It is easy to integrate and use in various Python projects where such functionality is required.