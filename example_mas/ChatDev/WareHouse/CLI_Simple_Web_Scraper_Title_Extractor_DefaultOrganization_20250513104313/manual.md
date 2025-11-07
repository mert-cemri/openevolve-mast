```
# Simple CLI Web Scraper

This is a simple command-line interface (CLI) web scraper that takes a URL as input and extracts and prints the title of the web page. It handles basic HTTP requests and is implemented in Python.

## Main Functions

- **Fetch Web Page**: The scraper fetches the web page content using an HTTP GET request.
- **Extract Title**: It extracts the title from the HTML content of the web page.
- **Display Title**: The extracted title is printed to the console.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- pip (Python package manager) to install dependencies.

### Quick Install

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use pip to install the required dependencies listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

   The dependencies include:
   - `requests==2.31.0`: For making HTTP requests.
   - `beautifulsoup4==4.12.2`: For parsing HTML content.

## How to Use

1. **Navigate to the Project Directory**: Ensure you are in the directory where the `main.py` file is located.

2. **Run the Scraper**: Use the following command to run the scraper. Replace `<URL>` with the actual URL of the web page you want to scrape.

   ```bash
   python main.py <URL>
   ```

   Example:

   ```bash
   python main.py https://www.example.com
   ```

3. **View the Output**: The title of the web page will be printed to the console.

## Troubleshooting

- **Error Fetching Page**: If you encounter an error while fetching the page, ensure that the URL is correct and that you have an active internet connection.
- **No Title Found**: If the output is "No title found", it means the web page does not have a `<title>` tag in its HTML content.

## Additional Information

- This tool is designed for educational purposes and simple web scraping tasks.
- Ensure compliance with the website's terms of service before scraping.

For further assistance or to report issues, please contact our support team.

```
