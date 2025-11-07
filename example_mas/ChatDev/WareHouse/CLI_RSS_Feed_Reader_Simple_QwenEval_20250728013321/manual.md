# RSS Feed Reader CLI Tool

## Overview

The RSS Feed Reader CLI Tool is a simple application that allows users to input an RSS feed URL and fetch the latest article titles and links from that feed. It's designed to be user-friendly and efficient, providing quick access to the latest content from your favorite websites.

## Main Functions

- **Input RSS Feed URL:** Users can enter the URL of an RSS feed they wish to read.
- **Fetch Articles:** The tool fetches the latest articles from the provided RSS feed.
- **Display Articles:** It displays the titles and links of the fetched articles in a readable format.

## Installation

To use the RSS Feed Reader CLI Tool, you need to have Python installed on your system. The tool requires the `requests` library to fetch data from the internet. Here's how you can install the necessary dependencies:

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Navigate to the directory where the `requirements.txt` file is located and run the following command to install the required dependencies:

```bash
pip install -r requirements.txt
```

This command will install the `requests` library, which is essential for fetching data from the internet.

## Usage

### Running the CLI Tool

To run the RSS Feed Reader CLI Tool, navigate to the directory containing the `main.py` file and execute the following command:

```bash
python main.py
```

### Steps to Use the Tool

1. **Enter RSS Feed URL:** When prompted, enter the URL of the RSS feed you wish to read.
2. **View Articles:** The tool will fetch and display the latest article titles and links from the provided RSS feed.

### Example

Here's an example of how to use the tool:

```bash
$ python main.py
Enter the RSS feed URL: https://example.com/rss
Title: Example Article 1
Link: https://example.com/article1

Title: Example Article 2
Link: https://example.com/article2
```

## Troubleshooting

### Common Issues

- **Invalid URL:** Ensure that the URL you enter is correct and points to a valid RSS feed.
- **Network Issues:** If you encounter network-related errors, check your internet connection.
- **Parsing Errors:** If the tool fails to parse the RSS feed, ensure that the feed is well-formed and contains valid XML data.

### Error Messages

- **An error occurred while fetching the feed:** This error indicates a problem with fetching data from the provided URL. Check your internet connection and ensure the URL is correct.
- **An error occurred:** This is a generic error message that can occur due to various issues. Check the error message for more details.

## Conclusion

The RSS Feed Reader CLI Tool is a simple yet powerful application that allows you to quickly access the latest articles from your favorite RSS feeds. By following the installation and usage instructions provided in this manual, you should be able to use the tool without any issues. If you encounter any problems, refer to the troubleshooting section for guidance.

Feel free to provide feedback or report any issues you encounter. We're here to help!

---

This manual should provide a comprehensive guide for users to understand and use the RSS Feed Reader CLI Tool effectively.