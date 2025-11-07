# Typing Speed Tester CLI

## Introduction

The Typing Speed Tester CLI is a command-line application designed to help users improve their typing skills by testing their words per minute (WPM) and accuracy. The application presents a random paragraph of text, and the user types it. After the user finishes typing, the application calculates and displays the WPM and accuracy.

## Main Functions

1. **Random Paragraph Generation**: The application fetches a random paragraph from an external API. If the API request fails, it uses a default paragraph.
2. **Timer**: The application starts a timer when the user begins typing and stops the timer when the user finishes typing.
3. **WPM Calculation**: The application calculates the words per minute based on the number of words typed and the elapsed time.
4. **Accuracy Calculation**: The application calculates the accuracy by comparing the user's input with the original paragraph.
5. **Feedback**: The application provides feedback on the user's performance, indicating whether they typed more or fewer words than the paragraph or if they completed the paragraph accurately.

## Quick Install

To install the Typing Speed Tester CLI, you need to have Python 3.6 or higher installed on your system. Follow these steps to install the application:

1. **Clone the Repository**: Clone the repository from GitHub or download the source code.
   ```bash
   git clone https://github.com/your-repo/typing-speed-tester.git
   cd typing-speed-tester
   ```

2. **Install Dependencies**: Install the required dependencies using `pip`.
   ```bash
   pip install -r requirements.txt
   ```

## How to Use/Play

1. **Run the Application**: Execute the main script to start the application.
   ```bash
   python main.py
   ```

2. **Start the Test**: Press `Enter` to start the typing test. The application will display a random paragraph of text.

3. **Type the Paragraph**: Type the paragraph as accurately and quickly as possible.

4. **Submit Your Input**: Press `Enter` after you have finished typing the paragraph.

5. **View Results**: The application will display the time taken, WPM, and accuracy. It will also provide feedback on your performance.

6. **Retry**: You can choose to retry the test by typing `y` when prompted. Type `n` to exit the application.

## Example Usage

```bash
$ python main.py
Welcome to the Typing Speed Tester!
Press Enter to start the test...

Type the following paragraph:

The quick brown fox jumps over the lazy dog.

Time taken: 5.00 seconds
Words per minute (WPM): 12.00
Accuracy: 100.00%
Great job on completing the paragraph!
Do you want to try again? (y/n): y
Press Enter to start the test...

Type the following paragraph:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Time taken: 15.00 seconds
Words per minute (WPM): 24.00
Accuracy: 95.00%
You typed more words than the paragraph. Please focus on accuracy.
Do you want to try again? (y/n): n
```

## Troubleshooting

- **API Request Failure**: If the application fails to fetch a paragraph from the API, it will use a default paragraph. Ensure you have an active internet connection.
- **Python Version**: Ensure you have Python 3.6 or higher installed. You can check your Python version by running `python --version`.

## Contributing

We welcome contributions to the Typing Speed Tester CLI. Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to contribute.

## License

The Typing Speed Tester CLI is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Feel free to reach out if you have any questions or need further assistance!