```markdown
# CLI Network Speed Tester

A simple command-line interface (CLI) application to measure your internet connection's download and upload speeds using a public test server.

## Introduction

The CLI Network Speed Tester is designed to provide users with an easy and efficient way to test their internet speed directly from the command line. By leveraging the `speedtest-cli` library, this tool measures both download and upload speeds, providing results in Megabits per second (Mbps).

## Quick Install

To get started with the CLI Network Speed Tester, you need to install the required dependencies. Follow the steps below to set up your environment:

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**

   Ensure you have Python installed on your system. Then, install the necessary dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `speedtest-cli` library, which is essential for running the speed tests.

## 🤔 What is this?

The CLI Network Speed Tester is a straightforward application that allows users to:

- Measure download speed in Mbps.
- Measure upload speed in Mbps.
- Quickly assess internet performance from the command line.

## How to Use

1. **Run the Application:**

   Navigate to the directory containing the `main.py` file and execute the following command:

   ```bash
   python main.py
   ```

   This will start the network speed test. The application will automatically select the best server for testing and display the results.

2. **Understand the Output:**

   After running the test, you will see output similar to the following:

   ```
   Starting network speed test...
   Download Speed: XX.XX Mbps
   Upload Speed: XX.XX Mbps
   ```

   The download and upload speeds are displayed in Mbps, providing a clear indication of your internet connection's performance.

## Troubleshooting

- **Error Handling:**

  If an error occurs during the speed test, the application will print an error message. Ensure that you have a stable internet connection and that the `speedtest-cli` library is correctly installed.

## 📖 Documentation

For more information on the `speedtest-cli` library and its capabilities, please refer to the official documentation:

- [speedtest-cli Documentation](https://github.com/sivel/speedtest-cli)

This user manual provides a comprehensive guide to installing and using the CLI Network Speed Tester. For any further assistance, please contact our support team.
```