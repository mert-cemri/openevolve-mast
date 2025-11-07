# Split Words User Manual

Welcome to the Split Words software! This tool is designed to process a string of text and split it into words based on specific delimiters or count certain characters based on their order in the alphabet. This manual will guide you through the main functions of the software, how to install it, and how to use it effectively.

## Main Functions

The primary function of this software is `split_words`, which processes a given string of text in the following ways:

1. **Split on Whitespace**: If the text contains any whitespace, the function will split the text into a list of words based on the whitespace.

2. **Split on Commas**: If there are no whitespaces but there are commas in the text, the function will split the text into a list of words based on the commas.

3. **Count Lowercase Letters with Odd Order**: If the text contains neither whitespaces nor commas, the function will count the number of lowercase letters that have an odd order in the alphabet (e.g., 'b', 'd', 'f', etc.) and return this count.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file to your local machine.

2. **No Additional Dependencies**: There are no additional dependencies required for this project, so you can proceed directly to using the software.

## How to Use

To use the `split_words` function, follow these steps:

1. **Open the `main.py` File**: Locate the `main.py` file in your downloaded repository.

2. **Run the Function**: You can run the function by calling it with a string input. For example:

    ```python
    from main import split_words

    # Example usage
    result1 = split_words("Hello world!")
    print(result1)  # Output: ["Hello", "world!"]

    result2 = split_words("Hello,world!")
    print(result2)  # Output: ["Hello", "world!"]

    result3 = split_words("abcdef")
    print(result3)  # Output: 3
    ```

3. **Interpret the Results**: The function will return a list of words if the text contains whitespaces or commas, or an integer representing the count of lowercase letters with odd order if neither delimiter is present.

## Conclusion

The Split Words software is a simple yet powerful tool for processing strings of text based on specific criteria. With no external dependencies required, it is easy to install and use. We hope this manual helps you get the most out of the software. If you have any questions or need further assistance, please feel free to reach out to our support team.