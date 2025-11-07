# SpellCheckerCLI User Manual

Welcome to the SpellCheckerCLI, a simple command-line interface (CLI) application designed to check the spelling of words in a text file or string input against a local dictionary file. This manual will guide you through the installation, setup, and usage of the SpellCheckerCLI.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Troubleshooting](#troubleshooting)

## Introduction

The SpellCheckerCLI is a Python-based application that helps users identify potential misspellings in their text. It uses a local dictionary file to compare words and highlight those that are not found in the dictionary. This tool is useful for writers, editors, and anyone who needs to ensure the accuracy of their text.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change your directory to the project folder:

   ```bash
   cd <repository-folder>
   ```

3. **Install Dependencies:**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the SpellCheckerCLI, you need to provide either a text file or a string input. The application will then check the spelling of the words against the local dictionary.

### Command-Line Options

- **Check a Text File:**

  To check the spelling of words in a text file, use the following command:

  ```bash
  python main.py --file <text_file>
  ```

  Replace `<text_file>` with the path to your text file.

- **Check a String:**

  To check the spelling of words in a string, use the following command:

  ```bash
  python main.py --string "<your_string>"
  ```

  Replace `<your_string>` with the text you want to check.

### Example

- Checking a text file:

  ```bash
  python main.py --file example.txt
  ```

- Checking a string:

  ```bash
  python main.py --string "This is a smple text with a misspelled word."
  ```

## Features

- **Local Dictionary:** The application uses a local dictionary file (`dictionary.txt`) to check for correct spellings.
- **Flexible Input:** Supports both text file and string input for spell checking.
- **Quick Feedback:** Provides immediate feedback on potential misspellings.

## Troubleshooting

- **Dictionary File Not Found:**

  If you encounter an error stating that the dictionary file is not found, ensure that `dictionary.txt` is present in the same directory as `main.py`.

- **File Not Found:**

  If the specified text file is not found, check the file path and ensure it is correct.

- **Invalid Input Type:**

  Ensure you are using the correct command-line options (`--file` or `--string`) when running the application.

For further assistance, please contact our support team.

Thank you for using SpellCheckerCLI!