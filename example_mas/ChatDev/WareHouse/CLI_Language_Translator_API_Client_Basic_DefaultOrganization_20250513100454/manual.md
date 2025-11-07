```markdown
# Translation CLI Client

A simple command-line interface (CLI) client for translating text using the Google Translate API. This tool allows users to input text and a target language, and it outputs the translated text.

## Main Functions

- **Translate Text**: Input text and specify a target language to receive a translation using the Google Translate API.
- **Error Handling**: Provides feedback if there are issues with the translation process, such as missing API keys or network errors.

## Quick Install

To get started with the Translation CLI Client, you need to install the required dependencies. This can be done easily using `pip`.

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Ensure you have Python installed on your system. Then, install the necessary Python packages using the following command:

```bash
pip install -r requirements.txt
```

This will install the `requests` library, which is used to make HTTP requests to the Google Translate API.

## Setting Up the Environment

Before using the CLI client, you need to set up your environment with the necessary API key.

### Step 3: Set Google Translate API Key

Obtain an API key from Google Cloud Platform for the Google Translate API. Once you have the API key, set it as an environment variable:

```bash
export GOOGLE_TRANSLATE_API_KEY='your_api_key_here'
```

Replace `'your_api_key_here'` with your actual API key.

## How to Use

Once you have installed the dependencies and set up the environment, you can use the CLI client to translate text.

### Step 4: Run the CLI Client

Use the following command to run the CLI client:

```bash
python main.py <text> <target_language>
```

- `<text>`: The text you want to translate.
- `<target_language>`: The language code for the target language (e.g., 'es' for Spanish, 'fr' for French).

### Example

To translate "Hello, world!" into Spanish, run:

```bash
python main.py "Hello, world!" es
```

The output will be the translated text in the specified target language.

## Troubleshooting

- **API Key Not Found**: Ensure that the `GOOGLE_TRANSLATE_API_KEY` environment variable is set correctly.
- **Network Issues**: Check your internet connection if you encounter network-related errors.
- **Invalid Language Code**: Ensure that the target language code is valid and supported by the Google Translate API.

For further assistance, please refer to the official [Google Translate API documentation](https://cloud.google.com/translate/docs).

```