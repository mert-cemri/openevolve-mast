manual.md

```
# Words String Splitter

A simple Python utility to split a string of words separated by commas or spaces into a list of individual words.

## Overview

The `words_string` function is designed to take a string input where words are separated by commas or spaces and return a list of those words. This can be particularly useful for text processing tasks where you need to handle and manipulate individual words from a sentence or a list.

## Main Functionality

- **Function Name:** `words_string`
- **Input:** A string (`s`) containing words separated by commas or spaces.
- **Output:** A list of words.

### Example Usage

```python
>>> words_string("Hi, my name is John")
['Hi', 'my', 'name', 'is', 'John']

>>> words_string("One, two, three, four, five, six")
['One', 'two', 'three', 'four', 'five', 'six']
```

## Installation

This utility is written in Python and does not require any external libraries, making it easy to integrate into any Python environment.

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd <project-directory>
   ```

3. **Run the Script:**

   You can directly run the script using Python:

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function:**

   If you wish to use the `words_string` function in another script, you can import it as follows:

   ```python
   from main import words_string
   ```

2. **Call the Function:**

   Pass a string to the function and receive a list of words:

   ```python
   words = words_string("Hello, world, this is a test")
   print(words)  # Output: ['Hello', 'world', 'this', 'is', 'a', 'test']
   ```

## Additional Information

This utility is designed to be simple and efficient, with no additional dependencies required. It is suitable for basic text processing tasks where splitting a string into words is needed.

For any issues or contributions, please refer to the project's repository on GitHub.

```