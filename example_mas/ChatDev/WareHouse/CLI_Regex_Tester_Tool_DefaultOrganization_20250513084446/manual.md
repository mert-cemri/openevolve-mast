# CLI Regex Tester

A command-line interface (CLI) tool for testing regular expressions against input strings. This tool allows users to input a regular expression and a test string to determine if the string matches the regex and optionally display matched groups.

## Main Functions

- **Regex Testing**: Input a regular expression and a test string to check for matches.
- **Matched Groups Display**: Optionally display matched groups if the regex matches the test string.
- **Error Handling**: Provides feedback for invalid regular expressions.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Ensure Python is Installed**: This tool requires Python version 3.6 or higher. You can download Python from the [official website](https://www.python.org/downloads/).

2. **Clone the Repository**: If you haven't already, clone the repository containing the CLI Regex Tester code.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your current directory to the project directory.

   ```bash
   cd <project-directory>
   ```

4. **Install Dependencies**: Use pip to install the required dependencies listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

Once you have installed the necessary dependencies, you can use the CLI Regex Tester as follows:

1. **Open a Terminal**: Open your command-line interface (CLI) or terminal.

2. **Run the Script**: Use the following command to run the script, providing the regular expression and the test string as arguments.

   ```bash
   python main.py "<regex>" "<test_string>"
   ```

   - Replace `<regex>` with the regular expression you want to test.
   - Replace `<test_string>` with the string you want to test against the regular expression.

3. **View Results**: The script will output whether a match was found and display any matched groups if applicable.

### Example

To test if the string "hello world" contains the word "hello":

```bash
python main.py "hello" "hello world"
```

Output:

```
Match found!
Matched groups: No groups
```

## Error Handling

If you input an invalid regular expression, the tool will provide an error message indicating the issue with the regex.

## Documentation

For further information and detailed documentation, please refer to the source code comments and the official Python documentation for the `re` and `argparse` modules.

---

This user manual provides a comprehensive guide to installing and using the CLI Regex Tester. For any additional support or inquiries, please contact our support team.