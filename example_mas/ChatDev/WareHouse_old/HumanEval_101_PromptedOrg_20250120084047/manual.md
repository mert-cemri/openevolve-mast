manual.md

```
# Words String Splitter

This software provides a simple function to split a string of words separated by commas or spaces into a list of words. It is designed to handle strings where words are separated by either commas, spaces, or a combination of both.

## Main Function

The main function provided by this software is `words_string(s)`. This function takes a single argument, `s`, which is a string containing words separated by commas or spaces. The function returns a list of individual words.

### Example Usage

```python
from main import words_string

# Example 1
result1 = words_string("Hi, my name is John")
print(result1)  # Output: ["Hi", "my", "name", "is", "John"]

# Example 2
result2 = words_string("One, two, three, four, five, six")
print(result2)  # Output: ["One", "two", "three", "four", "five", "six"]
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Steps to Install

1. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Code**: You can directly run the code using Python. No additional installation steps are required.

## How to Use

1. **Import the Function**: Import the `words_string` function from the `main.py` file into your Python script or interactive session.

2. **Call the Function**: Pass a string of words separated by commas or spaces to the `words_string` function.

3. **Get the Result**: The function will return a list of words.

### Example

```python
from main import words_string

input_string = "Hello, world, this is a test"
words_list = words_string(input_string)
print(words_list)  # Output: ["Hello", "world", "this", "is", "a", "test"]
```

## Additional Information

- **No External Libraries**: This software does not require any external Python libraries, making it lightweight and easy to integrate into other projects.

- **Simple and Efficient**: The function uses basic string manipulation techniques to achieve the desired result, ensuring efficiency and simplicity.

For any further questions or support, please contact our development team.
```