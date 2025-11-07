manual.md

```
# Anti-Shuffle Application

The Anti-Shuffle application is a simple Python-based utility that processes a given string and returns an ordered version of it. The application sorts the characters of each word in ascending order based on ASCII values while preserving the order of words and spaces in the sentence.

## Main Functionality

The primary function of this application is `anti_shuffle`, which takes a string as input and returns a new string where each word's characters are sorted in ascending order. This function is particularly useful for text processing tasks where maintaining the structure of the sentence is crucial while rearranging the characters within each word.

### Example Usage

- `anti_shuffle('Hi')` returns `'Hi'`
- `anti_shuffle('hello')` returns `'ehllo'`
- `anti_shuffle('Hello World!!!')` returns `'Hello !!!Wdlor'`

## Installation

This application does not require any external Python packages, making it easy to set up and run. You only need to have Python installed on your system.

### Steps to Install Python

1. **Download Python:**
   - Visit the official Python website: [python.org](https://www.python.org/)
   - Download the latest version of Python for your operating system.

2. **Install Python:**
   - Run the downloaded installer.
   - Follow the installation instructions, ensuring that you check the option to add Python to your system PATH.

3. **Verify Installation:**
   - Open a terminal or command prompt.
   - Type `python --version` and press Enter.
   - You should see the installed Python version number.

## How to Use the Application

1. **Clone or Download the Repository:**
   - Clone the repository using Git or download the ZIP file and extract it to your desired location.

2. **Navigate to the Project Directory:**
   - Open a terminal or command prompt.
   - Change the directory to the location where you have saved the `main.py` file.

3. **Run the Application:**
   - Execute the script by typing `python main.py` in the terminal or command prompt.
   - The script will run and display the output of the example usage.

4. **Modify Input:**
   - To test with different strings, open the `main.py` file in a text editor.
   - Modify the input strings in the `if __name__ == "__main__":` block to test with your own examples.

## Conclusion

The Anti-Shuffle application is a straightforward tool designed to help you rearrange characters within words while maintaining the overall sentence structure. With no external dependencies, it is easy to set up and use for various text processing needs.
```