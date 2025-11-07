# Words String Splitter

This software provides a simple function to split a string of words separated by commas or spaces into an array of words. It is designed to be lightweight and efficient, requiring no external dependencies.

## Main Functionality

The main functionality of this software is encapsulated in the `words_string` function. This function takes a single string input and returns a list of words. The input string can contain words separated by either commas or spaces, and the function will handle both cases seamlessly.

### Function: `words_string`

- **Purpose**: Splits a string into words separated by commas or spaces and returns an array of the words.
- **Input**: A string `s` containing words separated by commas or spaces.
- **Output**: A list of words.

#### Example Usage

```python
# Example 1
result = words_string("Hi, my name is John")
print(result)  # Output: ["Hi", "my", "name", "is", "John"]

# Example 2
result = words_string("One, two, three, four, five, six")
print(result)  # Output: ["One", "two", "three", "four", "five", "six"]
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change into the project directory:
   ```bash
   cd <project-directory>
   ```

3. **Run the Code**: You can directly run the `main.py` file to test the function:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: Import the `words_string` function into your Python script.
   ```python
   from main import words_string
   ```

2. **Call the Function**: Use the function by passing a string of words separated by commas or spaces.
   ```python
   words = words_string("Hello, world, this is a test")
   print(words)  # Output: ["Hello", "world", "this", "is", "a", "test"]
   ```

## Documentation

For further details on the usage and examples, please refer to the comments within the `main.py` file. The function is straightforward and designed to be intuitive for developers of all levels.

This software is ideal for applications where you need to process strings of words and convert them into a list format for further manipulation or analysis.