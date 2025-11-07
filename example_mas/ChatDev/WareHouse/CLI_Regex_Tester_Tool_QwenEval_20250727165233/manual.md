# Regex Tester CLI Tool

## Introduction

The Regex Tester CLI Tool is a command-line interface application designed to help users test regular expressions against strings. It provides feedback on whether the string matches the regex and can optionally display matched groups.

## Main Functions

1. **Regex Matching:** The tool checks if a given test string matches a specified regular expression.
2. **Matched Groups:** If the user requests, the tool can display the groups captured by the regex.

## Quick Install

To use the Regex Tester CLI Tool, you need to have Python installed on your system. Follow these steps to install the necessary dependencies:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ChatDev/regex-tester.git
   cd regex-tester
   ```

2. **Install Dependencies:**
   The `requirements.txt` file is empty, meaning there are no external dependencies required for this tool. However, ensure you have Python installed:
   ```bash
   python --version
   ```

## How to Use

### Basic Usage

To test a regular expression against a string, use the following command:

```bash
python main.py <regex> <test_string>
```

**Example:**
```bash
python main.py '\d+' 'There are 123 apples'
```

**Output:**
```
Match found: 123
```

### Displaying Matched Groups

To display matched groups, use the `-g` or `--groups` flag:

```bash
python main.py <regex> <test_string> -g
```

**Example:**
```bash
python main.py '(\d+)([a-zA-Z]+)' 'There are 123 apples' -g
```

**Output:**
```
Match found: 123apples
Matched groups: ('123', 'apples')
```

### Handling Regex Errors

If the provided regular expression is invalid, the tool will display an error message:

**Example:**
```bash
python main.py '(' 'There are 123 apples'
```

**Output:**
```
Regex error: unmatched '('
```

## Advanced Usage

### Using Special Characters

If your regular expression includes special characters, you may need to escape them using backslashes (`\`). In the command line, you might need to escape these characters twice (once for the shell and once for Python).

**Example:**
```bash
python main.py '\\d+' 'There are 123 apples'
```

### Testing Complex Patterns

You can test complex regex patterns with multiple groups and quantifiers:

**Example:**
```bash
python main.py '(\w+)\s+(\w+)' 'John Doe' -g
```

**Output:**
```
Match found: John Doe
Matched groups: ('John', 'Doe')
```

## Troubleshooting

### No Match Found

If the test string does not match the regex, the tool will indicate that no match was found:

**Example:**
```bash
python main.py '\d+' 'There are no numbers here'
```

**Output:**
```
No match found.
```

### Invalid Regex

Ensure that your regular expression is valid. Common issues include unmatched parentheses or unsupported syntax.

## Conclusion

The Regex Tester CLI Tool is a powerful utility for developers and testers working with regular expressions. It provides a simple and effective way to test regex patterns and understand how they match against strings. For more advanced usage and examples, refer to the documentation or the source code.

---

This manual should provide a comprehensive guide for users to understand and effectively use the Regex Tester CLI Tool.