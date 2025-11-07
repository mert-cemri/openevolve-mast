manual.md

```
# is_bored Function

The `is_bored` function is a simple Python utility designed to count the number of sentences in a given string that start with the word "I". This function can be useful for text analysis tasks where identifying specific sentence structures is required.

## Main Functionality

- **is_bored(S)**: This function takes a single string input `S`, which is expected to be a sequence of sentences. It returns an integer representing the number of sentences that start with the word "I". Sentences are considered to be delimited by '.', '?', or '!'.

### Example Usage

```python
from main import is_bored

# Example 1
result1 = is_bored("Hello world")
print(result1)  # Output: 0

# Example 2
result2 = is_bored("The sky is blue. The sun is shining. I love this weather")
print(result2)  # Output: 1
```

## Installation and Setup

### Environment Dependencies

This software does not require any external dependencies beyond the standard Python library. Therefore, you can run the function in any standard Python environment without additional installations.

### Quick Start

1. **Clone the Repository**: Start by cloning the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can use the function directly in your Python scripts or interactive sessions.

   ```python
   from main import is_bored
   print(is_bored("I am happy. Are you? I think so!"))
   ```

## Additional Information

- **No External Libraries Required**: The function uses Python's built-in `re` module for regular expression operations, which is included in the standard library.

- **Modifications**: If you need to modify the function for different delimiters or starting words, you can adjust the regular expression pattern and the starting word check within the function.

- **Testing**: You can test the function using various strings to ensure it meets your specific needs. Consider edge cases such as strings with no sentences or multiple delimiters.

This manual provides all the necessary information to understand, install, and use the `is_bored` function effectively. If you have further questions or need support, please contact our support team.
```