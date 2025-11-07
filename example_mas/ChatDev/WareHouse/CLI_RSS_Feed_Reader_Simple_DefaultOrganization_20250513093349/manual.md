# CLI RSS Feed Reader

Welcome to the CLI RSS Feed Reader! This simple command-line tool allows you to fetch and display the latest article titles and links from any RSS feed URL you provide.

## Main Functions

The CLI RSS Feed Reader is designed to:

- Prompt the user to enter an RSS feed URL.
- Fetch and parse the RSS feed from the provided URL.
- Display the latest article titles and links in a user-friendly format.

## Quick Install

To get started with the CLI RSS Feed Reader, you need to install the required dependencies. Follow these steps to set up your environment:

1. **Clone the Repository:**

   First, clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**

   The application requires the `feedparser` library to function. You can install it using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install all necessary dependencies listed in the `requirements.txt` file.

## How to Use

Once you have installed the dependencies, you can start using the CLI RSS Feed Reader:

1. **Run the Application:**

   Execute the main script to start the application:

   ```bash
   python main.py
   ```

2. **Enter RSS Feed URL:**

   When prompted, enter a valid RSS feed URL. For example:

   ```
   Enter RSS Feed URL: http://example.com/rss
   ```

3. **View Articles:**

   The application will fetch and display the latest article titles and links from the RSS feed. If the URL is invalid or the feed is not well-formed, an error message will be displayed.

   Example output:

   ```
   Title: Example Article 1
   Link: http://example.com/article1

   Title: Example Article 2
   Link: http://example.com/article2
   ```

## Troubleshooting

- **Invalid URL or Feed:** If you encounter an error stating "Invalid RSS feed URL or feed is not well-formed," ensure that the URL is correct and points to a valid RSS feed.

- **No Articles Found:** If no articles are displayed, the RSS feed might be empty or not updated. Verify the feed's content by visiting the URL in a web browser.

## Additional Information

For more information on RSS feeds and how they work, please refer to online resources or documentation specific to the RSS feed you are using.

Thank you for using the CLI RSS Feed Reader! If you have any questions or need further assistance, feel free to reach out.