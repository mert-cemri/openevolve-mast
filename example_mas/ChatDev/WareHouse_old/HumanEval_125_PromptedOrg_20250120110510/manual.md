# Split Words Function

This software provides a utility function `split_words` that processes a given string of text according to specific rules. It is designed to split text into words based on whitespace or commas, or to count certain characters when neither is present.

## Main Functions

### split_words(txt)

The `split_words` function takes a single string argument `txt` and performs the following operations:

1. **Split on Whitespace**: If the text contains whitespace, it splits the text into a list of words based on the whitespace.
   - Example: `split_words("Hello world!")` returns `["Hello", "world!"]`.

2. **Split on Commas**: If the text does not contain whitespace but contains commas, it splits the text into a list of words based on the commas.
   - Example: `split_words("Hello,world!")` returns `["Hello", "world!"]`.

3. **Count Lowercase Letters with Odd Order**: If the text contains neither whitespace nor commas, it counts the number of lowercase letters that have an odd order in the alphabet (where `ord('a') = 0`, `ord('b') = 1`, ..., `ord('z') = 25`).
   - Example: `split_words("abcdef")` returns `3` because 'b', 'd', and 'f' have odd orders.

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change into the project directory:
   ```bash
   cd <project-directory>
   ```

3. **Run the Code**: You can directly run the `main.py` file to test the function:
   ```bash
   python main.py
   ```

## Usage

To use the `split_words` function, you can import it into your Python script and call it with the desired string input. Here's an example:

```python
from main import split_words

# Example usage
result1 = split_words("Hello world!")
print(result1)  # Output: ["Hello", "world!"]

result2 = split_words("Hello,world!")
print(result2)  # Output: ["Hello", "world!"]

result3 = split_words("abcdef")
print(result3)  # Output: 3
```

This function is useful for text processing tasks where you need to handle different types of delimiters or count specific characters based on their position in the alphabet.