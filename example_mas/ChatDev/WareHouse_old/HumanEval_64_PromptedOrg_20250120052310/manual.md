# Vowels Count User Manual

Welcome to the Vowels Count software! This tool is designed to help you count the number of vowels in a given string, considering 'a', 'e', 'i', 'o', 'u' as vowels, and 'y' as a vowel only when it appears at the end of the word.

## Main Functions

The primary function of this software is:

- **vowels_count(s):** This function takes a string `s` as input and returns the number of vowels in the string. The vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' (only if 'y' is at the end of the word).

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Download the Code:**
   - Download the `main.py` file from the repository or source where it is hosted.

3. **No Additional Dependencies:**
   - There are no additional dependencies required for this project, as indicated in the `requirements.txt` file.

## How to Use

1. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the script using the command:
     ```
     python main.py
     ```

2. **Test Cases:**
   - The script includes several test cases to verify the functionality of the `vowels_count` function. When you run the script, it will automatically execute these test cases and print "All test cases passed!" if everything is working correctly.

3. **Using the Function:**
   - You can use the `vowels_count` function in your own Python scripts by importing it. Here is an example:
     ```python
     from main import vowels_count

     word = "example"
     count = vowels_count(word)
     print(f"The number of vowels in '{word}' is {count}.")
     ```

## Conclusion

This software provides a simple yet effective way to count vowels in a string, with special consideration for the letter 'y'. It is easy to set up and use, with no additional dependencies required. If you have any questions or need further assistance, please feel free to reach out. Enjoy using the Vowels Count tool!