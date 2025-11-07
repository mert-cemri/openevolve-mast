# CLI Regex Tester

A simple command-line interface (CLI) application to test regular expressions against input strings. This tool allows users to verify if a string matches a given regular expression and optionally displays any matched groups.

## Quick Install

To get started with the CLI Regex Tester, you need to have Python installed on your system. The application requires Python version 3.6 or higher.

### Step 1: Clone the Repository

First, clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the actual URL of the repository.

### Step 2: Install Dependencies

Navigate to the project directory and install the required dependencies using pip:

```bash
cd <project-directory>
pip install -r requirements.txt
```

This will ensure that the correct version of Python is used and any necessary packages are installed.

## 🤔 What is this?

The CLI Regex Tester is a tool designed to help users test regular expressions quickly and efficiently. Regular expressions (regex) are powerful tools for matching patterns in strings, and this application provides a straightforward way to test these patterns.

### Main Functions

- **Regex Matching**: Enter a regular expression and a test string to see if they match.
- **Matched Groups**: If the regex includes capturing groups, the tool will display them.
- **Error Handling**: Provides feedback if the entered regular expression is invalid.

## 📖 How to Use

1. **Run the Application**: Execute the main script using Python:

    ```bash
    python main.py
    ```

2. **Enter the Regular Expression**: When prompted, input the regular expression you wish to test.

3. **Enter the Test String**: Provide the string you want to test against the regular expression.

4. **View Results**: The application will display whether a match was found. If there are capturing groups in the regex, it will also display the matched groups.

5. **Error Feedback**: If there is an error in the regular expression syntax, the application will inform you of the specific issue.

## Example Usage

```bash
$ python main.py
Enter the regular expression: (\d{3})-(\d{2})-(\d{4})
Enter the test string: 123-45-6789
Match found! Matched groups: ('123', '45', '6789')
```

In this example, the regular expression is designed to match a Social Security number format, and the test string matches the pattern, displaying the captured groups.

## Troubleshooting

- Ensure you have Python 3.6 or higher installed.
- Verify that all dependencies are installed correctly using the `requirements.txt` file.
- If you encounter issues, double-check the syntax of your regular expression.

## Resources

For more information on regular expressions and their syntax, consider visiting the following resources:

- [Python Regular Expressions Documentation](https://docs.python.org/3/library/re.html)
- [Regular Expressions 101](https://regex101.com/)

This user manual provides all the necessary steps to install, run, and utilize the CLI Regex Tester effectively. Enjoy testing your regular expressions with ease!