manual.md

```
# CLI Translation Tool

A simple command-line interface (CLI) tool for translating text into different languages using the `googletrans` library.

## Introduction

The CLI Translation Tool allows users to input text and specify a target language to receive a translated output. It leverages the `googletrans` library to interact with the Google Translate API, providing a straightforward way to perform translations directly from the command line.

## Main Functions

- **Text Translation**: Input any text and specify the target language code to receive an instant translation.
- **Language Support**: Supports a wide range of languages as provided by the Google Translate API.
- **Error Handling**: Provides feedback in case of network issues or other errors during translation.

## Installation

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installing Dependencies

1. Open your terminal or command prompt.
2. Install the `googletrans` library using pip by running the following command:
   ```bash
   pip install googletrans==4.0.0-rc1
   ```

## Usage

1. Clone or download the repository containing the `main.py` and `translator.py` files.
2. Open your terminal or command prompt and navigate to the directory containing these files.
3. Run the `main.py` script with the text you want to translate and the target language code. For example, to translate "Hello" to Spanish, use the following command:
   ```bash
   python main.py "Hello" es
   ```
   Replace `"Hello"` with your desired text and `es` with the language code for your target language.

## Language Codes

Refer to the [Google Translate language codes](https://cloud.google.com/translate/docs/languages) to find the appropriate code for your target language.

## Troubleshooting

- **Translation Failed**: If you encounter a "Translation failed" error, please check your network connection and try again. The `googletrans` library may have reliability issues due to changes in the Google Translate API.
- **Alternative Libraries**: If issues persist, consider exploring alternative libraries or APIs for more reliable translation services.

## Support

For further assistance, please contact our support team or refer to the documentation provided within the repository.

```