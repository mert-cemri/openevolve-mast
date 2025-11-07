```markdown
# CLI Network Speed Tester

A simple command-line interface (CLI) application to test your network's download and upload speeds using the `speedtest-cli` library.

## Introduction

The CLI Network Speed Tester is designed to provide users with an easy-to-use tool for measuring their internet connection speeds. By leveraging the `speedtest-cli` library, this application connects to a public test server to measure both download and upload speeds, providing results in Mbps (Megabits per second).

## Main Functions

- **Download Speed Test**: Measures the download speed of your internet connection.
- **Upload Speed Test**: Measures the upload speed of your internet connection.

## Quick Install

To get started with the CLI Network Speed Tester, you'll need to install the necessary dependencies. Follow the steps below to set up your environment:

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use `pip` to install the required dependencies listed in the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `speedtest-cli` library necessary for running the application.

## How to Use

Once you have installed the dependencies, you can run the application to test your network speed:

1. **Run the Application**: Execute the `main.py` file to start the speed test.

   ```bash
   python main.py
   ```

2. **View Results**: The application will display your network's download and upload speeds in Mbps.

   ```
   Testing network speed...
   Download Speed: XX.XX Mbps
   Upload Speed: XX.XX Mbps
   ```

## Documentation

For further details on the `speedtest-cli` library and its capabilities, please refer to the [official documentation](https://github.com/sivel/speedtest-cli).

## Support

If you encounter any issues or have questions, please reach out to our support team or open an issue in the project repository.

Enjoy testing your network speed with our CLI Network Speed Tester!
```
