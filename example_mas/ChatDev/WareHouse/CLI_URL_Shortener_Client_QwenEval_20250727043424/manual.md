# URL Shortener CLI User Manual

## Introduction

The URL Shortener CLI is a simple command-line tool designed to shorten long URLs using the TinyURL API. It provides a straightforward interface for users to input a long URL and receive a shortened version. Additionally, a graphical user interface (GUI) version is available for those who prefer a visual approach.

## Key Features

- **Command-Line Interface (CLI):** Easily shorten URLs from the terminal.
- **Graphical User Interface (GUI):** A user-friendly interface for those who prefer a visual approach.
- **Error Handling:** Robust error handling for invalid URLs and API failures.
- **Logging:** Detailed logging for debugging purposes.
- **Configuration:** Support for different URL shortening services (future feature).

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` package manager

### Installing Dependencies

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/chatdev/url_shortener_cli.git
   cd url_shortener_cli
   ```

2. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

   This will install the necessary dependencies, including the `requests` library.

### Installing the Package

You can also install the package directly using `pip`:

```bash
pip install .
```

This command will install the `url_shortener_cli` package along with its dependencies.

## Usage

### Command-Line Interface (CLI)

1. **Shorten a URL:**

   ```bash
   url_shortener https://www.example.com
   ```

   This command will output the shortened URL.

2. **Example Output:**

   ```bash
   Shortened URL: https://tinyurl.com/abc123
   ```

### Graphical User Interface (GUI)

1. **Run the GUI:**

   ```bash
   url_shortener_gui
   ```

2. **Interface Overview:**

   - **Enter the long URL:** Type or paste the long URL you want to shorten.
   - **Shorten URL Button:** Click this button to shorten the URL.
   - **Result:** The shortened URL will be displayed below the button.

### Error Handling

- **Invalid URL:** If the URL is invalid, an error message will be displayed.
- **API Failure:** If the API request fails, an error message will be displayed.

## Configuration

### API Keys

Currently, the tool does not require API keys for TinyURL. However, future versions may support additional services that require API keys.

### Logging

Logging is enabled by default and can be configured in the `main.py` file. Logs are written to the console and can be redirected to a file if needed.

## Troubleshooting

### Common Issues

- **Invalid URL:** Ensure the URL is correctly formatted and accessible.
- **API Failure:** Check your internet connection and try again. If the issue persists, contact support.

### Contact Support

For any issues or questions, please contact us at:

- **Email:** support@chatdev.com
- **GitHub Issues:** [https://github.com/chatdev/url_shortener_cli/issues](https://github.com/chatdev/url_shortener_cli/issues)

## Future Enhancements

- **Support for Additional URL Shortening Services:** Users will be able to choose from multiple services.
- **Configuration Files:** Users can store API keys and other settings in configuration files.
- **Advanced Error Handling:** Improved error messages and recovery options.

## Conclusion

The URL Shortener CLI is a powerful tool for quickly shortening URLs from the command line or through a simple GUI. With robust error handling and logging, it provides a reliable solution for URL shortening needs. We look forward to your feedback and suggestions for future enhancements.

---

This manual should provide a comprehensive guide for users to understand and use the URL Shortener CLI effectively.