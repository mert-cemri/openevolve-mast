# Select Words Software

This software provides a function to extract words from a given string that contain a specified number of consonants. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function of this software is `select_words(s, n)`, which takes two parameters:
- `s`: A string containing words separated by spaces.
- `n`: A natural number representing the exact number of consonants a word must have to be included in the result.

The function returns a list of words from the string `s` that contain exactly `n` consonants, maintaining the order in which they appear in the string. If the string `s` is empty, the function returns an empty list.

### Examples

- `select_words("Mary had a little lamb", 4)` returns `["little"]`
- `select_words("Mary had a little lamb", 3)` returns `["Mary", "lamb"]`
- `select_words("simple white space", 2)` returns `[]`
- `select_words("Hello world", 4)` returns `["world"]`
- `select_words("Uncle sam", 3)` returns `["Uncle"]`

## Installation

No external dependencies are required to use this software. It is implemented in Python and can be run in any standard Python environment.

### Quick Start

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory containing the `main.py` file:
   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can test the function by running the `main.py` file in a Python environment:
   ```bash
   python main.py
   ```

## Usage

To use the `select_words` function in your own projects, simply import the function from the `main.py` file and call it with the desired parameters.

```python
from main import select_words

result = select_words("Your string here", number_of_consonants)
print(result)
```

## Documentation

The function is straightforward and does not require additional setup or configuration. For any questions or further assistance, please refer to the comments within the code for guidance on how the function operates.

This software is designed to be lightweight and easy to integrate into larger projects where text processing is required.