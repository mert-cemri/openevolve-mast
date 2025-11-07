# Anti-Shuffle Function

This software provides a simple Python function, `anti_shuffle`, which takes a string and returns an ordered version of it. The function arranges the characters of each word in ascending order based on their ASCII values while maintaining the order of words and spaces in the sentence.

## Main Functionality

- **anti_shuffle(s):** This function takes a string `s` as input and returns a new string where each word's characters are sorted in ascending order by ASCII value. The order of words and spaces in the original string is preserved.

### Examples

- `anti_shuffle('Hi')` returns `'Hi'`
- `anti_shuffle('hello')` returns `'ehllo'`
- `anti_shuffle('Hello World!!!')` returns `'Hello !!!Wdlor'`

## Installation

No additional dependencies are required to run this software. It is implemented in pure Python. Ensure you have Python installed on your system.

### Quick Install

1. **Python Installation:** Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository:** Obtain the `main.py` file containing the `anti_shuffle` function.

## Usage

1. **Open the Terminal or Command Prompt.**

2. **Navigate to the Directory:** Change to the directory where `main.py` is located.

3. **Run the Script:** Execute the script using Python to see the function in action. You can modify the script to test with different input strings.

   ```bash
   python main.py
   ```

4. **Modify the Code:** You can edit `main.py` to test the `anti_shuffle` function with different strings by changing the input to the `print` statements at the bottom of the file.

## Documentation

The `anti_shuffle` function is straightforward and does not require additional libraries or frameworks. It uses Python's built-in string and list manipulation capabilities to achieve the desired functionality.

For further customization or integration into larger projects, you can import the `anti_shuffle` function from `main.py` into your own Python scripts.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided within the code comments.