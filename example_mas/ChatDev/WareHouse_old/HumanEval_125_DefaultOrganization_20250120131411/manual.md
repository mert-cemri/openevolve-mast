manual.md

```
# Split Words Application

This application provides a simple utility function to process strings of text. It splits the text into words based on specific criteria and returns either a list of words or a count of specific lowercase letters.

## Main Functionality

The core functionality of this application is encapsulated in the `split_words` function. This function takes a string input and processes it according to the following rules:

1. **Whitespace Splitting**: If the input string contains whitespace, the function splits the string into a list of words based on the whitespace.

2. **Comma Splitting**: If there are no whitespaces but commas are present, the function splits the string into a list of words based on the commas.

3. **Odd Order Lowercase Count**: If neither whitespaces nor commas are present, the function calculates the number of lowercase letters in the string that have an odd order in the alphabet (e.g., 'b', 'd', 'f', etc.) and returns this count.

### Examples

- `split_words("Hello world!")` returns `["Hello", "world!"]`
- `split_words("Hello,world!")` returns `["Hello", "world!"]`
- `split_words("abcdef")` returns `3`

## Installation

This application does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Run the Script**: You can directly run the script using Python. Navigate to the directory containing `main.py` and execute:

   ```bash
   python main.py
   ```

## How to Use

To use the `split_words` function, follow these steps:

1. **Import the Function**: If you are integrating this function into another project, import it from the `main.py` file.

   ```python
   from main import split_words
   ```

2. **Call the Function**: Pass a string to the `split_words` function and handle the output as needed.

   ```python
   result = split_words("Your input string here")
   print(result)
   ```

## Additional Information

This application is designed to be lightweight and efficient, focusing solely on the task of string processing as described. It is ideal for educational purposes, small projects, or as a utility function in larger applications.

For any questions or further assistance, please contact our support team.

```