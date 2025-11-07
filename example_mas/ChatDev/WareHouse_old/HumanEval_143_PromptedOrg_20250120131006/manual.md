# Words in Sentence

This software module provides a function to filter words in a sentence based on the primality of their lengths. It is designed to help users identify words whose lengths are prime numbers from a given sentence.

## Main Functionality

The main function provided by this module is `words_in_sentence(sentence)`. This function takes a string representing a sentence and returns a string containing the words from the original sentence whose lengths are prime numbers. The order of the words in the new string is the same as in the original sentence.

### Example Usage

1. **Input**: "This is a test"
   - **Output**: "is"

2. **Input**: "lets go for swimming"
   - **Output**: "go for"

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the `main.py` file is located:
   ```bash
   cd <directory-name>
   ```

3. **Run the Code**: You can run the `main.py` file using Python to test the function:
   ```bash
   python main.py
   ```

4. **Use the Function**: To use the `words_in_sentence` function in your own projects, you can import it from the `main.py` file:
   ```python
   from main import words_in_sentence

   sentence = "Your sentence here"
   result = words_in_sentence(sentence)
   print(result)
   ```

## Documentation

The function `words_in_sentence(sentence)` is documented within the code itself. It includes a docstring explaining its purpose, input parameters, and expected output.

For further assistance or questions, please contact our support team or refer to the inline comments within the code for more detailed explanations of the logic and implementation.