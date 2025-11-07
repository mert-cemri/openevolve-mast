# Check If Last Char Is A Letter

This software provides a simple function to determine if the last character of a given string is an alphabetical character and is not part of a word. This can be useful in text processing tasks where such a distinction is necessary.

## Main Functionality

The main function provided by this software is:

- `check_if_last_char_is_a_letter(txt)`: This function takes a string `txt` as input and returns `True` if the last character of the string is an alphabetical character and is not part of a word, and `False` otherwise.

### Examples

- `check_if_last_char_is_a_letter("apple pie")` ➞ `False`
- `check_if_last_char_is_a_letter("apple pi e")` ➞ `True`
- `check_if_last_char_is_a_letter("apple pi e ")` ➞ `False`
- `check_if_last_char_is_a_letter("")` ➞ `False`

## Installation

### Environment Setup

This software does not require any external dependencies, making it straightforward to set up and use. You can run this function in any Python environment.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your directory to the project folder:

   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can directly run the `main.py` file to test the function:

   ```bash
   python main.py
   ```

## Usage

To use the function, simply call it with a string argument. Here's a quick guide on how to use it:

1. **Import the Function**: If you have the function in a separate file, import it into your script.

   ```python
   from main import check_if_last_char_is_a_letter
   ```

2. **Call the Function**: Pass a string to the function and capture the result.

   ```python
   result = check_if_last_char_is_a_letter("your string here")
   print(result)  # This will print True or False based on the input
   ```

## Conclusion

This software provides a straightforward solution to check if the last character of a string is an isolated alphabetical character. With no external dependencies, it is easy to integrate into any Python project.