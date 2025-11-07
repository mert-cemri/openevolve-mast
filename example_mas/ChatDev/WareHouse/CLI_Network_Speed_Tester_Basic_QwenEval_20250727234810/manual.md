# Network Speed Tester CLI

## Quick Overview

The Network Speed Tester CLI is a command-line tool designed to measure your internet connection's download and upload speeds. It uses the `speedtest` library to perform these tests against a public test server.

## 📦 Installation

### Prerequisites

- Python 3.6 or higher
- `pip` package manager

### Installing Dependencies

To install the required dependencies, you can use the following command:

```bash
pip install speedtest-cli
```

## 🚀 How to Use

### Running the Speed Test

To run the speed test, navigate to the directory containing the `main.py` file and execute the following command:

```bash
python main.py
```

### Expected Output

After running the command, the tool will perform a download and upload speed test and print the results to the console in Mbps. Here is an example of the output:

```
Download Speed: 123.45 Mbps
Upload Speed: 54.32 Mbps
```

### Handling Errors

If the speed test fails, the tool will print an error message. Common reasons for failure include:

- Network connectivity issues
- Server timeouts

In such cases, please check your network connection and try running the test again.

## 🛠️ Main Functions

### `main.py`

- **Purpose:** Serves as the entry point for the application.
- **Functions:**
  - Initializes the `SpeedTestCLI` class.
  - Runs the speed test and prints the results.

### `speedtest_cli.py`

- **Purpose:** Handles the speed testing logic using the `speedtest` library.
- **Functions:**
  - Initializes the `Speedtest` object.
  - Runs the download and upload tests.
  - Returns the results as a dictionary.

### `speedtest_gui.py`

- **Purpose:** Intentionally left empty as the task specifies a CLI tool, and a GUI component is not required.

## 📖 Documentation

For more detailed information, please refer to the code comments within the `main.py` and `speedtest_cli.py` files.

## 🙋‍♂️ Support

If you encounter any issues or have suggestions for improvements, please feel free to reach out to our support team at support@chatdev.com.

---

This manual should provide a comprehensive guide for users to understand and use the Network Speed Tester CLI effectively.