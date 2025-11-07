manual.md

```
# Boredom Counter

A simple Python application to count the number of sentences starting with the word "I" in a given string. This application is useful for analyzing text to determine how often sentences begin with a specific word, which in this case is "I".

## Main Functionality

The main function provided by this application is `is_bored(S)`, which takes a string `S` as input and returns the number of sentences that start with the word "I". Sentences are considered to be delimited by '.', '?' or '!'.

### Example Usage

```python
>>> is_bored("Hello world")
0
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
```

## Installation

### Environment Setup

This application does not require any external dependencies, making it straightforward to set up and run. You only need to have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Move into the project directory where the `main.py` file is located.

4. **Run the Code**: You can directly run the `main.py` file using Python:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you want to use the function in another script, you can import it:
   ```python
   from main import is_bored
   ```

2. **Call the Function**: Pass a string to the `is_bored` function to get the count of sentences starting with "I":
   ```python
   result = is_bored("I am happy. You are here. I like this.")
   print(result)  # Output will be 2
   ```

## Additional Information

- **No External Libraries Required**: The application uses Python's built-in `re` module for regular expressions to split the string into sentences.

- **Customization**: You can modify the function to count sentences starting with different words by changing the condition in the list comprehension.

This application is designed to be simple and efficient, providing a quick way to analyze text for specific sentence patterns.
```