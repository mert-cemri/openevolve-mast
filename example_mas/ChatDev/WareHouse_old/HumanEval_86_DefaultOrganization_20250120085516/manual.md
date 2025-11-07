manual.md

```
# Anti-Shuffle Application

The Anti-Shuffle application is a simple Python-based utility that processes a given string by rearranging the characters of each word in ascending order based on their ASCII values. The application maintains the order of words and spaces in the input string.

## Main Functionality

The core functionality of the Anti-Shuffle application is encapsulated in the `anti_shuffle` function. This function takes a string as input and returns a new string where each word's characters are sorted in ascending order. Spaces between words are preserved.

### Example Usage

- `anti_shuffle('Hi')` returns `'Hi'`
- `anti_shuffle('hello')` returns `'ehllo'`
- `anti_shuffle('Hello World!!!')` returns `'Hello !!!Wdlor'`

## Installation

The Anti-Shuffle application does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository:**
   - Clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory:**
   - Open a terminal and navigate to the directory where `main.py` is located.

3. **Run the Application:**
   - Execute the script using Python:
     ```bash
     python main.py
     ```

## How to Use

1. **Open the Terminal:**
   - Open your terminal or command prompt.

2. **Navigate to the Application Directory:**
   - Use the `cd` command to navigate to the directory containing `main.py`.

3. **Run the Script:**
   - Execute the script by typing `python main.py` in the terminal.

4. **Input Strings:**
   - The script includes example usage within the `if __name__ == "__main__":` block. You can modify this section to test the `anti_shuffle` function with different input strings.

5. **View Output:**
   - The output will be displayed in the terminal, showing the ordered version of the input strings.

## Customization

To customize the application or test it with different strings, modify the example usage section in `main.py`. Replace the strings in the `print` statements with your own test cases.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the repository.

```