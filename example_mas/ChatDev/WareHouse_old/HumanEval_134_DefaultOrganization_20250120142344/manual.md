# Check If Last Char Is A Letter

This software provides a simple function to determine if the last character of a given string is an alphabetical character and is not part of a word. This can be useful in text processing tasks where such checks are necessary.

## Main Functionality

The main function provided by this software is:

- `check_if_last_char_is_a_letter(txt)`: This function takes a string `txt` as input and returns `True` if the last character is an alphabetical character and is not part of a word (i.e., preceded by a space). Otherwise, it returns `False`.

### Examples

- `check_if_last_char_is_a_letter("apple pie")` ➞ `False`
- `check_if_last_char_is_a_letter("apple pi e")` ➞ `True`
- `check_if_last_char_is_a_letter("apple pi e ")` ➞ `False`
- `check_if_last_char_is_a_letter("")` ➞ `False`

## Installation

This software is implemented in Python. To use it, you need to have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/).

### Environment Setup

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your working directory to the project directory.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Although there are no additional dependencies listed in `requirements.txt`, ensure your Python environment is set up correctly. You can create a virtual environment to manage dependencies:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

   Then, install any necessary packages (if any are added in the future) using:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the function, you can run the `main.py` file directly or import the function into your own Python script.

### Running Directly

You can run the `main.py` file to see example outputs:

```bash
python main.py
```

### Importing the Function

To use the function in your own script, import it as follows:

```python
from main import check_if_last_char_is_a_letter

# Example usage
result = check_if_last_char_is_a_letter("your text here")
print(result)
```

## Conclusion

This software provides a straightforward utility for checking the last character of a string. It is designed to be simple and efficient, making it easy to integrate into larger text processing workflows. If you have any questions or need further assistance, please contact our support team.