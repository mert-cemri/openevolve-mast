# IP Address Lookup CLI Tool User Manual

## Introduction

The IP Address Lookup CLI Tool is a command-line interface (CLI) application designed to fetch and display geolocation and ISP information for a given IP address using the public API from [ip-api.com](http://ip-api.com/). This tool is built using Python and is intended for users who need to quickly retrieve IP information for network diagnostics, security analysis, or general curiosity.

## Main Functions

- **IP Information Retrieval**: The tool allows users to input an IP address and retrieves detailed information such as city, region, country, ISP, latitude, and longitude.
- **Error Handling**: The tool includes robust error handling to manage issues such as invalid IP addresses, network errors, and API failures.
- **Logging**: All actions and errors are logged for debugging and auditing purposes.

## Quick Install

To use the IP Address Lookup CLI Tool, you need to have Python installed on your system. The tool has been tested with Python 3.8 and later versions.

### Step 1: Install Python

If you haven't installed Python yet, download and install it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Required Dependencies

The tool requires the `requests` library to make HTTP requests to the IP geolocation API. You can install this library using `pip`.

Open your terminal or command prompt and run the following command:

```bash
pip install -r requirements.txt
```

This command will install the `requests` library and any other dependencies listed in the `requirements.txt` file.

## How to Use the Tool

### Step 1: Run the Tool

Navigate to the directory where the tool is installed and run the following command:

```bash
python main.py <IP_ADDRESS>
```

Replace `<IP_ADDRESS>` with the IP address you want to look up. For example:

```bash
python main.py 8.8.8.8
```

### Step 2: View the Output

The tool will display the geolocation and ISP information for the provided IP address. The output will include:

- **IP Address**: The IP address you entered.
- **City**: The city associated with the IP address.
- **Region**: The region associated with the IP address.
- **Country**: The country associated with the IP address.
- **ISP**: The Internet Service Provider associated with the IP address.
- **Latitude**: The latitude coordinate of the IP address.
- **Longitude**: The longitude coordinate of the IP address.

### Step 3: Handle Errors

If the tool encounters an error (e.g., invalid IP address, network error), it will display an error message in the terminal. The error will also be logged for further analysis.

## Logging

All actions and errors are logged to the console using Python's built-in `logging` module. The log level is set to `INFO`, which means that all informational messages and errors will be displayed.

## Conclusion

The IP Address Lookup CLI Tool is a simple yet powerful utility for retrieving geolocation and ISP information for any given IP address. By following the installation and usage instructions provided in this manual, you can quickly and easily integrate this tool into your workflow.

If you encounter any issues or have suggestions for improvement, please feel free to reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).

---

This manual should provide a comprehensive guide for users to install, configure, and use the IP Address Lookup CLI Tool effectively.