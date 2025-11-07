manual.md

```
# Anti-Shuffle Application

This application provides a function called `anti_shuffle` that takes a string and returns an ordered version of it. The ordered version of the string is achieved by sorting the characters of each word in ascending order based on their ASCII values, while maintaining the original order of words and spaces in the sentence.

## Main Functionality

### anti_shuffle Function

- **Purpose**: To reorder the characters of each word in a string in ascending ASCII order.
- **Input**: A string `s` where words are separated by spaces.
- **Output**: A string where each word's characters are sorted, maintaining the original order of words and spaces.

#### Example Usage

```python
from main import anti_shuffle

print(anti_shuffle('Hi'))  # Output: 'Hi'
print(anti_shuffle('hello'))  # Output: 'ehllo'
print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'
```

## Installation

### Environment Setup

To run the `anti_shuffle` function, you need to have Python installed on your system. The function does not require any additional dependencies, so no external packages need to be installed.

1. **Install Python**: If you do not have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

```bash
git clone <repository-url>
```

3. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

```bash
cd <repository-directory>
```

## Usage

1. **Run the Script**: You can run the script directly from the command line to see the example outputs.

```bash
python main.py
```

2. **Integrate into Your Project**: You can import the `anti_shuffle` function into your own Python projects.

```python
from main import anti_shuffle

# Use the function in your project
result = anti_shuffle('Your string here')
```

## Documentation

The `anti_shuffle` function is documented within the `main.py` file. You can refer to the docstring in the function for a detailed explanation of its purpose and usage.

For further assistance or inquiries, please contact our support team.

```

This manual provides a comprehensive guide to using the `anti_shuffle` function, including installation instructions, usage examples, and integration tips.