manual.md

```
# Split Words Utility

The Split Words Utility is a Python-based application designed to process strings of text and return a list of words based on specific criteria. This utility is useful for text processing tasks where you need to split text into words or count specific characters.

## Main Functions

The primary function of this utility is `split_words(txt)`, which performs the following operations:

1. **Split on Whitespace**: If the input text contains whitespace, the function splits the text into a list of words based on the whitespace.

2. **Split on Commas**: If the input text does not contain whitespace but contains commas, the function splits the text into a list of words based on the commas.

3. **Count Lowercase Letters with Odd Order**: If the input text contains neither whitespace nor commas, the function returns the count of lowercase letters that have an odd order in the alphabet. For example, 'b' (ord('b') = 1) and 'd' (ord('d') = 3) are considered odd.

## Installation

To use the Split Words Utility, you need to have Python installed on your system. Follow these steps to set up your environment:

1. **Install Python**: Ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Set Up a Virtual Environment** (optional but recommended):
   - Create a virtual environment: `python -m venv env`
   - Activate the virtual environment:
     - On Windows: `.\env\Scripts\activate`
     - On macOS/Linux: `source env/bin/activate`

3. **Install Dependencies**: There are no additional dependencies required for this utility. However, if you plan to extend the functionality, you can manage dependencies using a `requirements.txt` file.

## Usage

To use the Split Words Utility, follow these steps:

1. **Create a Python Script**: Create a Python script (e.g., `main.py`) and include the `split_words` function code provided.

2. **Call the Function**: Use the `split_words` function by passing a string as an argument. For example:

   ```python
   from main import split_words

   result = split_words("Hello world!")
   print(result)  # Output: ["Hello", "world!"]

   result = split_words("Hello,world!")
   print(result)  # Output: ["Hello", "world!"]

   result = split_words("abcdef")
   print(result)  # Output: 3
   ```

3. **Run the Script**: Execute your script using Python:

   ```bash
   python main.py
   ```

## Documentation

For further details on how to use the function and examples of different use cases, please refer to the comments within the code. The function is designed to be straightforward and easy to integrate into larger projects.

Feel free to modify and extend the functionality to suit your specific needs. If you encounter any issues or have questions, please reach out to our support team for assistance.
```