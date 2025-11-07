```markdown
# Morse Code Translator

A Command Line Interface (CLI) application for translating English text to Morse code and vice versa.

## Introduction

The Morse Code Translator is a simple yet powerful tool that allows users to convert English text into Morse code and decode Morse code back into English text. This application is designed to be used directly from the command line, making it a convenient tool for quick translations.

## Main Functions

- **Text to Morse Code Translation**: Converts English text into Morse code using standard Morse code representations for letters, numbers, and some punctuation marks.
- **Morse Code to Text Translation**: Decodes Morse code back into English text, allowing for easy interpretation of Morse messages.

## Installation

### Prerequisites

- Python 3.x must be installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```
   Replace `<project-directory>` with the name of the cloned repository.

3. **Install Dependencies**: There are no external dependencies required for this project. All functionality is implemented using the standard Python library.

## Usage

### Running the Application

The application can be run from the command line using the following syntax:

```bash
python main.py <mode> <text>
```

- `<mode>`: Specify the mode of operation. Use `'encode'` to translate text to Morse code and `'decode'` to translate Morse code to text.
- `<text>`: The text or Morse code to be translated. For Morse code, use spaces to separate letters and three spaces to separate words.

### Examples

1. **Encoding Text to Morse Code**:
   ```bash
   python main.py encode "Hello World"
   ```
   Output:
   ```
   .... . .-.. .-.. ---   .-- --- .-. .-.. -..
   ```

2. **Decoding Morse Code to Text**:
   ```bash
   python main.py decode ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
   ```
   Output:
   ```
   HELLO WORLD
   ```

## Documentation

For further details on the Morse code standards used and additional examples, please refer to the source code documentation within the `morse_code_translator.py` file.

## Support

For any issues or questions, please contact the development team at [support@chatdev.com](mailto:support@chatdev.com).

```
