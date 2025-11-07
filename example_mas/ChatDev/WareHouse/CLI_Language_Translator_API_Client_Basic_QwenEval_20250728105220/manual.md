# Language Translation CLI Client Manual

## Introduction

Welcome to the Language Translation CLI Client manual. This tool allows you to translate text from one language to another using a simple command-line interface. It leverages a language translation API to provide accurate translations. This manual will guide you through the installation, setup, and usage of the tool.

## Main Functions

- **Text Translation:** Enter text and specify the target language to receive a translation.
- **Error Handling:** The tool checks for missing inputs and API errors, providing appropriate error messages.

## Prerequisites

- Python 3.6 or higher
- Internet connection to access the translation API

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ChatDev/LanguageTranslationCLI.git
   cd LanguageTranslationCLI
   ```

2. **Install Dependencies:**

   Ensure you have `pip` installed. Then, install the required packages using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should contain:

   ```
   requests>=2.25.1
   python-dotenv>=0.19.0
   ```

3. **Set Up API Key:**

   - Obtain an API key from a translation service provider (e.g., Google Translate API).
   - Create a `.env` file in the root directory of the project.
   - Add your API key to the `.env` file:

     ```
     API_KEY=your_api_key_here
     ```

## Usage

### Command-Line Interface (CLI)

1. **Run the Application:**

   ```bash
   python main.py
   ```

2. **Input Text and Target Language:**

   - When prompted, enter the text you wish to translate.
   - Enter the target language code (e.g., `en` for English, `fr` for French).

3. **Receive Translation:**

   - The tool will output the translated text.

### Graphical User Interface (GUI)

1. **Run the GUI Application:**

   ```bash
   python gui.py
   ```

2. **Input Text and Target Language:**

   - Enter the text you wish to translate in the "Enter text to translate" field.
   - Enter the target language code in the "Enter target language" field.

3. **Translate:**

   - Click the "Translate" button.
   - The translated text will appear in the "Translation" field.

## Troubleshooting

- **API Key Issues:**
  - Ensure your API key is correctly set in the `.env` file.
  - Verify that the API key has the necessary permissions.

- **Network Issues:**
  - Ensure you have an active internet connection.
  - Check your firewall settings to allow API requests.

- **Input Errors:**
  - Ensure you provide both text and a target language code.
  - Check for typos in the target language code.

## Support

For any issues or questions, please contact our support team at support@chatdev.com.

---

This manual should provide a comprehensive guide for users to install, configure, and use the Language Translation CLI Client. If you have any further questions or need additional assistance, feel free to reach out.