# CLI Regex Tester

A powerful command-line tool for testing regular expressions against strings. This tool allows you to verify if a string matches a given regex pattern and optionally display the matched groups.

## Quick Install

To use the CLI Regex Tester, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code. The tool does not require any additional Python packages, so no further installation is necessary.

## 🤔 What is this?

The CLI Regex Tester is a simple yet effective tool for developers and anyone working with regular expressions. It allows you to test regex patterns directly from the command line, providing immediate feedback on whether a string matches the pattern and optionally showing the matched groups.

## 📖 Documentation

### Main Functions

- **Test Regex Pattern**: The primary function of the tool is to test a regular expression pattern against a given string.
- **Show Matched Groups**: Optionally, the tool can display the matched groups if the string matches the regex pattern.
- **Match Type**: You can choose between `re.search` (default) and `re.match` to specify the type of match.

### How to Use

1. **Open your terminal or command prompt.**
2. **Navigate to the directory where the `main.py` file is located.**
3. **Run the tool with the required arguments.**

#### Basic Usage

To test a regex pattern against a string, use the following command:

```bash
python main.py <regex> <test_string>
```

**Example:**

```bash
python main.py '\d+' 'There are 123 apples'
```

**Output:**

```
Match found!
Matched groups: ('123',)
```

#### Advanced Usage

You can also specify whether to show matched groups and the type of match to perform.

**Show Matched Groups:**

```bash
python main.py <regex> <test_string> [show_groups]
```

**Example:**

```bash
python main.py '\d+' 'There are 123 apples' true
```

**Output:**

```
Match found!
Matched groups: ('123',)
```

**Specify Match Type:**

```bash
python main.py <regex> <test_string> [show_groups] [match_type]
```

**Example:**

```bash
python main.py '\d+' '123 apples' true match
```

**Output:**

```
Match found!
Matched groups: ('123',)
```

### Troubleshooting

- **Invalid Regex Pattern**: If you provide an invalid regex pattern, the tool will display an error message.

**Example:**

```bash
python main.py '(\d+' 'There are 123 apples'
```

**Output:**

```
Invalid regex pattern: missing ), unterminated subpattern at position 0
```

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to contribute to the project.

## 📞 Contact

For any questions or feedback, please contact us at [support@chatdev.com](mailto:support@chatdev.com).

---

This manual should provide a comprehensive guide for users to understand and use the CLI Regex Tester effectively.