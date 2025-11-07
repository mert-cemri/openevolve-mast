# Anti-Shuffle User Manual

Welcome to the Anti-Shuffle software! This application is designed to reorder the characters of each word in a given string based on their ASCII values while maintaining the original order of words and spaces. This manual will guide you through the installation process, introduce the main functions of the software, and provide examples of how to use it.

## Quick Install

To get started with the Anti-Shuffle software, you need to have Python installed on your system. If you haven't installed Python yet, please download and install it from [python.org](https://www.python.org/).

### Step 1: Clone the Repository

First, clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the actual URL of the repository.

### Step 2: Navigate to the Project Directory

Change your working directory to the project directory:

```bash
cd <project-directory>
```

Replace `<project-directory>` with the name of the cloned directory.

### Step 3: Install Dependencies

The Anti-Shuffle software does not have any external dependencies, so you can skip this step. However, ensure that your Python environment is set up correctly.

## Main Functionality

The core functionality of the Anti-Shuffle software is encapsulated in the `anti_shuffle` function. This function takes a string as input and returns a new string where each word's characters are sorted in ascending order based on their ASCII values.

### Function Definition

```python
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.
    """
```

### Example Usage

Here are some examples of how to use the `anti_shuffle` function:

```python
# Example 1
result = anti_shuffle('Hi')
print(result)  # Output: 'Hi'

# Example 2
result = anti_shuffle('hello')
print(result)  # Output: 'ehllo'

# Example 3
result = anti_shuffle('Hello World!!!')
print(result)  # Output: 'Hello !!!Wdlor'
```

## How to Use

1. Open your terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located.
3. Run the script using Python:

```bash
python main.py
```

This will execute the example usage provided in the script and display the output in the terminal.

## Conclusion

The Anti-Shuffle software is a simple yet effective tool for reordering characters within words of a string. With no external dependencies, it is easy to set up and use. We hope this manual has provided you with the necessary information to get started. If you have any questions or need further assistance, please feel free to reach out.