# URL Shortener CLI

A command-line interface (CLI) tool for shortening URLs using the TinyURL API.

## Introduction

The URL Shortener CLI is a simple and efficient tool designed to shorten long URLs into more manageable links using the TinyURL API. This tool is particularly useful for developers and users who frequently need to share URLs in a concise format.

## Main Functions

- **Shorten URL**: The primary function of this CLI tool is to take a long URL provided by the user and return a shortened version using the TinyURL service.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Quick Install

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**

   Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   The CLI tool requires a TinyURL API key to function. Set the `TINYURL_API_KEY` environment variable with your API key:

   ```bash
   export TINYURL_API_KEY='your_tinyurl_api_key'
   ```

   Alternatively, you can create a `.env` file in the project directory and add the following line:

   ```
   TINYURL_API_KEY=your_tinyurl_api_key
   ```

## Usage

Once you have installed the dependencies and set up the environment variables, you can use the CLI tool to shorten URLs.

### Command-Line Usage

To shorten a URL, run the following command in your terminal:

```bash
python main.py <long_url>
```

Replace `<long_url>` with the URL you wish to shorten. For example:

```bash
python main.py https://www.example.com/very/long/url
```

### Output

The tool will output the shortened URL if successful. If there is an error (e.g., missing API key, invalid URL), an appropriate error message will be displayed.

## Troubleshooting

- **API Key Not Found**: Ensure that the `TINYURL_API_KEY` environment variable is set correctly. You can check this by running `echo $TINYURL_API_KEY` in your terminal.

- **Invalid URL**: Make sure the URL you are trying to shorten is valid and properly formatted.

- **Network Issues**: Ensure that your internet connection is active and stable.

## Documentation

For more detailed documentation and examples, please refer to the source code comments and the README file in the repository.

## Support

For further assistance, please contact our support team or open an issue in the repository.

---

This manual provides a comprehensive guide to installing and using the URL Shortener CLI tool. Follow the instructions carefully to ensure a smooth setup and operation.