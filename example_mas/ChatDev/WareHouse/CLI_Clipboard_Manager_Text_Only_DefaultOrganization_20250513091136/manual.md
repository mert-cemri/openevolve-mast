# CLI Clipboard Manager

A command-line interface (CLI) application to manage an internal clipboard for text. This tool allows users to copy text to the clipboard, paste the most recently copied text, and view the clipboard history.

## Quick Install

To get started with the CLI Clipboard Manager, you need to have Python installed on your system. The application requires Python version 3.6 or higher.

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

This will ensure that you have the necessary Python version to run the application.

## 🤔 What is this?

The CLI Clipboard Manager is a simple yet powerful tool designed to manage text-based clipboard operations from the command line. It operates independently of the system clipboard, maintaining its own history of copied text.

### Main Features

- **Copy Text**: Add text to the internal clipboard.
- **Paste Text**: Retrieve the most recently copied text.
- **View History**: Display the history of all copied text entries.

## 📖 How to Use

Once you have installed the dependencies, you can start using the CLI Clipboard Manager by running the main script.

### Running the Application

To start the application, execute the following command in your terminal:

```bash
python main.py
```

### Commands

After starting the application, you can use the following commands:

- **`copy <text>`**: Copies the specified text to the clipboard.
  - Example: `copy Hello, World!`
- **`paste`**: Pastes the most recently copied text.
- **`history`**: Displays the history of all copied text entries.
- **`exit`**: Exits the clipboard manager.

### Example Usage

1. **Copy Text**: 
   - Input: `copy Hello, World!`
   - Output: `Text copied: "Hello, World!"`

2. **Paste Text**: 
   - Input: `paste`
   - Output: `Pasted text: "Hello, World!"`

3. **View History**: 
   - Input: `history`
   - Output:
     ```
     Clipboard History:
     1: Hello, World!
     ```

4. **Exit**: 
   - Input: `exit`
   - Output: `Exiting the clipboard manager.`

## Support

For any issues or questions, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

---

This user manual provides a comprehensive guide to installing and using the CLI Clipboard Manager. Enjoy managing your text clipboard efficiently!