# CLI Clipboard Manager User Manual

## Introduction

The CLI Clipboard Manager is a command-line interface (CLI) tool designed to manage text-only clipboard operations. It allows users to copy text to an internal clipboard, paste from it, and view its history without interacting with the system clipboard directly.

## Quick Install

To install the CLI Clipboard Manager, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository and install the required dependencies:

```bash
git clone https://github.com/ChatDev/cli-clipboard-manager.git
cd cli-clipboard-manager
pip install -r requirements.txt
```

Alternatively, you can install the package directly from PyPI:

```bash
pip install cli-clipboard-manager
```

## 🤔 What is this?

The CLI Clipboard Manager is a simple yet powerful tool for managing text clipboard operations. It provides the following main functions:

- **Copy**: Copy text to the internal clipboard.
- **Paste**: Paste text from the internal clipboard.
- **History**: View the history of copied texts.
- **Clear**: Clear the clipboard and/or history.
- **Version**: Show the version of the clipboard manager.
- **Help**: Show a list of available commands.

## 📖 Documentation

### Main Functions

#### Copy

To copy text to the internal clipboard, use the `copy` command:

```bash
> copy
Enter text to copy: Hello, World!
Text copied: Hello, World!
```

#### Paste

To paste text from the internal clipboard, use the `paste` command:

```bash
> paste
Hello, World!
```

#### History

To view the history of copied texts, use the `history` command:

```bash
> history
Clipboard history:
1. Hello, World!
2. Another text
```

#### Clear

To clear the clipboard and/or history, use the `clear` command:

```bash
> clear
What would you like to clear?
  1. Clipboard
  2. History
  3. Both
Enter your choice (1/2/3): 3
Clipboard and history cleared.
```

#### Version

To show the version of the clipboard manager, use the `version` command:

```bash
> version
CLI Clipboard Manager version 1.0
```

#### Help

To show a list of available commands, use the `help` command:

```bash
> help
Available commands:
  copy         - Copy text to the clipboard
  paste        - Paste text from the clipboard
  history      - View the history of copied texts
  clear        - Clear the clipboard and history
  version      - Show the version of the clipboard manager
  help         - Show this help message
  exit         - Exit the application
```

### How to Use

1. **Start the Application**

   To start the CLI Clipboard Manager, run the following command:

   ```bash
   python main.py
   ```

2. **Interact with the Application**

   Once the application is running, you can interact with it using the commands listed above.

3. **Exit the Application**

   To exit the application, use the `exit` command:

   ```bash
   > exit
   Exiting the CLI Clipboard Manager. Goodbye!
   ```

## 🛠️ Requirements

- Python 3.6 or higher
- `clipboard_manager` module
- `cli` module

## 🙌 Contributing

We welcome contributions to the CLI Clipboard Manager! If you have any ideas or bug fixes, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/ChatDev/cli-clipboard-manager).

## 📧 Contact

For any questions or support, please contact us at [support@chatdev.com](mailto:support@chatdev.com).

---

This manual should provide a comprehensive guide for users to understand and use the CLI Clipboard Manager effectively.