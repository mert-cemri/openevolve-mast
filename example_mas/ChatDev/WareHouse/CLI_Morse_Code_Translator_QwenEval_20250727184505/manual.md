# Morse Code Translator CLI

## Quick Overview

The Morse Code Translator CLI is a simple yet powerful command-line interface application that allows users to translate English text to Morse code and vice versa. This tool is perfect for enthusiasts, students, or anyone interested in Morse code.

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher installed on your system.
- `pip` package manager installed (usually comes with Python).

### Steps to Install

1. **Clone the Repository (Optional)**

   If you have `git` installed, you can clone the repository to your local machine:

   ```bash
   git clone https://github.com/ChatDev/MorseCodeTranslator.git
   cd MorseCodeTranslator
   ```

   If you don't have `git`, you can download the repository as a ZIP file and extract it.

2. **Install Dependencies**

   Navigate to the project directory and install the required dependencies using `pip`. For this project, no external dependencies are required, but you can still run the following command to ensure everything is set up correctly:

   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### Running the Application

To start the Morse Code Translator CLI, navigate to the project directory and run the following command:

```bash
python main.py
```

### Main Functions

1. **Translate English to Morse Code**

   - Enter the English text you want to translate.
   - The application will output the corresponding Morse code.

   **Example:**

   ```
   Enter text to translate to Morse code or Morse code to translate to text: Hello World
   Translated Morse code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
   ```

2. **Translate Morse Code to English**

   - Enter the Morse code you want to translate.
   - The application will output the corresponding English text.

   **Example:**

   ```
   Enter text to translate to Morse code or Morse code to translate to text: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
   Translated English text: HELLOWORLD
   ```

3. **Exit the Application**

   - Type `exit` and press Enter to quit the application.

   **Example:**

   ```
   Enter text to translate to Morse code or Morse code to translate to text: exit
   Goodbye!
   ```

### Notes

- **Unknown Characters:** If the input contains characters not supported by Morse code, they will be replaced with `?` in the output.
- **Spaces:** Spaces in English text are represented by `/` in Morse code.
- **Case Insensitivity:** The application treats all input as uppercase.

## 🤝 Contributing

We welcome contributions from the community! If you have any ideas for improvements or bug fixes, feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/ChatDev/MorseCodeTranslator).

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to reach out if you have any questions or need further assistance with the Morse Code Translator CLI!

---

This manual should provide a clear and detailed guide for users to understand and use the Morse Code Translator CLI effectively.