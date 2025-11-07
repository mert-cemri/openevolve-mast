# ChatDev Dictionary Lookup Tool

## Overview

The ChatDev Dictionary Lookup Tool is a simple yet powerful command-line interface (CLI) application designed to help users quickly look up definitions of words using a local, offline dictionary file. This tool is ideal for developers, students, and anyone who needs a reliable dictionary without an internet connection.

## Features

- **Local Dictionary File:** Utilizes a plain text file (`dictionary.txt`) containing words and their definitions in a `word:definition` format.
- **Command-Line Interface (CLI):** Easy to use from the terminal.
- **Case Insensitivity:** Automatically converts user input to lowercase for accurate matching.
- **Error Handling:** Provides informative messages for invalid inputs and missing definitions.

## Installation

### Prerequisites

- **Python:** Ensure you have Python 3.6 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **pip:** Python's package manager, usually included with Python installations.

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ChatDev/Dictionary_Tool.git
   cd Dictionary_Tool
   ```

2. **Install Dependencies:**
   The tool has no external dependencies beyond Python's standard library, so no additional packages need to be installed via `pip`. However, if you have a `requirements.txt` file, you can run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

To look up a word, run the following command in your terminal:

```bash
python main.py <word>
```

Replace `<word>` with the word you want to look up. For example:

```bash
python main.py apple
```

### Example

Given the `dictionary.txt` file:

```txt
apple: A fruit that is typically red, green, or yellow.
banana: A long curved fruit that grows in clusters and has soft pulpy flesh and yellow skin when ripe.
carrot: A root vegetable that is typically orange, though purple, red, white, and yellow varieties also exist.
```

Running:

```bash
python main.py banana
```

Will output:

```
Definition of 'banana': A long curved fruit that grows in clusters and has soft pulpy flesh and yellow skin when ripe.
```

### Error Handling

- **Invalid Input:** If the user does not provide a word, the tool will display an error message:
  ```
  Usage: python main.py <word>
  ```

- **Empty Input:** If the user provides an empty string, the tool will display an error message:
  ```
  Error: The input word cannot be empty.
  ```

- **Word Not Found:** If the word is not found in the dictionary, the tool will display a message:
  ```
  No definition found for 'word'. Please check the spelling and try again.
  ```

## Customizing the Dictionary

To add, remove, or modify words and definitions, simply edit the `dictionary.txt` file. Ensure each line follows the `word:definition` format, with no spaces around the colon.

### Example

To add a new word:

```txt
orange: A citrus fruit that is typically round and has a tough bright reddish-yellow rind.
```

## Contributing

We welcome contributions to improve the ChatDev Dictionary Lookup Tool. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Open a pull request to the main repository.

## License

The ChatDev Dictionary Lookup Tool is open-source software licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions, feedback, or support, please contact us at [support@chatdev.com](mailto:support@chatdev.com).

---

This manual provides a comprehensive guide to using the ChatDev Dictionary Lookup Tool, ensuring that users can easily install, use, and customize the application to meet their needs.