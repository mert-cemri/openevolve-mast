# Sort Numbers User Manual

Welcome to the Sort Numbers software! This tool is designed to sort a space-delimited string of numerals from 'zero' to 'nine'. Below is a detailed guide on how to use this software, including installation instructions and usage examples.

## Quick Install

This project does not require any external dependencies, so you can directly run the Python script without any additional installations. However, ensure you have Python installed on your system.

## 🤔 What is this?

The Sort Numbers software is a simple Python application that takes a string of numeral words (from 'zero' to 'nine') and returns them sorted in ascending order. This can be particularly useful for educational purposes or applications where numeral word sorting is required.

## 📖 Main Function

The core functionality of this software is provided by the `sort_numbers` function. Here is a brief overview:

- **Function Name:** `sort_numbers`
- **Input:** A space-delimited string of numeral words (e.g., 'three one five').
- **Output:** A string with the numeral words sorted from smallest to largest (e.g., 'one three five').

### Example Usage

```python
from main import sort_numbers

# Example input
input_string = 'three one five'

# Sorting the numeral words
sorted_string = sort_numbers(input_string)

# Output: 'one three five'
print(sorted_string)
```

## How to Use

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Download the Script:**
   - Download the `main.py` file containing the `sort_numbers` function.

3. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the script using Python:
     ```bash
     python main.py
     ```

4. **Use the Function:**
   - Import the `sort_numbers` function in your Python script or interactive shell.
   - Pass a space-delimited string of numeral words to the function and get the sorted output.

## Troubleshooting

- **Python Not Found:** Ensure Python is installed and added to your system's PATH.
- **Incorrect Output:** Double-check that the input string contains only valid numeral words ('zero' to 'nine').

For further assistance, please contact our support team. We hope you find this tool useful and easy to integrate into your projects!