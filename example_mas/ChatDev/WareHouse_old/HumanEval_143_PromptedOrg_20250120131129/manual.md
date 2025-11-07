# Prime Length Words Extractor

This software module is designed to extract words from a given sentence whose lengths are prime numbers. It is implemented in Python and provides a simple function to achieve this task.

## Main Functionality

The main functionality of this software is to identify and return words from a sentence that have lengths which are prime numbers. The function processes the input sentence, checks the length of each word, and determines if the length is a prime number. If it is, the word is included in the output.

### Key Function

- `words_in_sentence(sentence)`: This function takes a string input representing a sentence and returns a string containing words whose lengths are prime numbers, maintaining the original order.

## Installation

To use this software, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly use the provided Python script.

### Steps to Install Python

1. **Download Python**: Visit the official Python website at [python.org](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**: Follow the installation instructions provided on the website for your specific operating system.

3. **Verify Installation**: Open a terminal or command prompt and type `python --version` to verify that Python is installed correctly.

## Usage

Once Python is installed, you can use the software by following these steps:

1. **Save the Code**: Copy the provided code into a file named `main.py`.

2. **Run the Script**: Open a terminal or command prompt, navigate to the directory where `main.py` is located, and run the script using the command:
   ```
   python main.py
   ```

3. **Use the Function**: You can call the `words_in_sentence` function from within the script or import it into another Python script to use it with different sentences.

### Example Usage

```python
from main import words_in_sentence

sentence1 = "This is a test"
result1 = words_in_sentence(sentence1)
print(result1)  # Output: "is"

sentence2 = "lets go for swimming"
result2 = words_in_sentence(sentence2)
print(result2)  # Output: "go for"
```

## Conclusion

This software provides a simple and efficient way to extract words with prime lengths from a sentence. It is easy to use and requires no additional dependencies, making it a lightweight solution for text processing tasks.