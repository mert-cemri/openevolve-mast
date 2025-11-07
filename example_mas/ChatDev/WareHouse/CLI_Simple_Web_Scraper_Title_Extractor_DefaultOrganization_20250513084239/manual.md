# WebScraper CLI Tool

A simple command-line interface (CLI) web scraper that extracts and prints the title of a web page from a given URL. This tool handles basic HTTP requests and is implemented in Python.

## Main Functions

The WebScraper CLI tool provides the following main functions:

1. **Fetch HTML Content**: Makes an HTTP GET request to the specified URL and retrieves the HTML content of the web page.

2. **Extract Title**: Parses the HTML content to extract and return the title of the web page.

3. **Command-Line Interface**: Allows users to input a URL directly in the terminal and outputs the title of the web page.

## Installation

To use the WebScraper CLI tool, you need to have Python installed on your system. Additionally, you need to install the required dependencies listed in the `requirements.txt` file.

### Step-by-Step Installation Guide

1. **Clone the Repository**: First, clone the repository containing the WebScraper CLI tool to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment** (Optional but recommended): Create and activate a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**: Use pip to install the required Python packages.

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

Once the environment is set up and dependencies are installed, you can use the WebScraper CLI tool to extract the title of a web page.

### Running the WebScraper

1. **Execute the Script**: Run the `main.py` script using Python.

   ```bash
   python main.py
   ```

2. **Input the URL**: When prompted, enter the URL of the web page you want to scrape.

   ```
   Enter the URL of the web page: https://example.com
   ```

3. **View the Output**: The tool will output the title of the web page.

   ```
   The title of the web page is: Example Domain
   ```

## Troubleshooting

- **HTTP Errors**: If you encounter HTTP errors, ensure that the URL is correct and the server is reachable.

- **No Title Found**: If the tool returns "No title found", the web page might not have a `<title>` tag, or the HTML structure might be non-standard.

## Additional Information

This tool is designed for educational purposes and simple web scraping tasks. For more complex scraping needs, consider using more robust frameworks and tools. Always ensure compliance with the terms of service of the websites you scrape.