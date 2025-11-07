manual.md

```
# Split Words Application

This application provides a simple function to process a string of words. It splits the string based on specific conditions and returns either a list of words or a count of specific characters. 

## Main Functionality

The main function of this application is `split_words(txt)`, which operates as follows:

1. **Whitespace Splitting**: If the input string contains whitespace, the function splits the string into a list of words based on the whitespace.

2. **Comma Splitting**: If there are no whitespace characters but there are commas, the function splits the string into a list of words based on the commas.

3. **Odd Order Count**: If neither whitespace nor commas are present, the function counts the number of lowercase letters in the string that have an odd order in the alphabet (where 'a' is 0, 'b' is 1, ..., 'z' is 25) and returns this count.

### Examples

- `split_words("Hello world!")` returns `["Hello", "world!"]`
- `split_words("Hello,world!")` returns `["Hello", "world!"]`
- `split_words("abcdef")` returns `3`

## Installation

This application does not require any external dependencies. You can simply download the `main.py` file and run it using Python.

### Requirements

- Python 3.x

## How to Use

1. **Download the Code**: Save the `main.py` file to your local machine.

2. **Run the Code**: Open a terminal or command prompt, navigate to the directory where `main.py` is located, and run the following command:

   ```bash
   python main.py
   ```

3. **Test the Function**: You can test the function by modifying the example usage at the bottom of the `main.py` file or by calling the `split_words(txt)` function with different input strings.

## Additional Information

This application is designed to be simple and efficient, focusing on processing strings based on specific conditions. It is suitable for educational purposes or as a utility function in larger projects where text processing is required.

For further assistance or inquiries, please contact our support team.
```