```markdown
# IP Lookup CLI Tool

A command-line interface (CLI) tool to look up IP address information such as geolocation and ISP using the public IP geolocation API from ip-api.com.

## Overview

This CLI tool allows users to input an IP address and retrieve detailed information about its location and service provider. The tool is designed to be simple and efficient, providing quick access to IP-related data directly from the command line.

## Main Functions

- **IP Geolocation**: Retrieve the country, region, and city associated with the given IP address.
- **ISP Information**: Identify the Internet Service Provider (ISP) for the IP address.
- **Geographical Coordinates**: Obtain the latitude and longitude of the IP address location.

## Installation

### Prerequisites

Ensure you have Python installed on your system. This tool requires Python 3.6 or later.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Use pip to install the required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the IP Lookup CLI tool, follow these steps:

1. **Open Terminal**: Open your command-line interface (CLI) or terminal.

2. **Run the Tool**: Execute the `main.py` script with the desired IP address as an argument:
   ```bash
   python main.py <IP-ADDRESS>
   ```

   Replace `<IP-ADDRESS>` with the actual IP address you want to look up.

3. **View Results**: The tool will output the following information:
   - IP Address
   - Country
   - Region
   - City
   - ISP
   - Latitude
   - Longitude

### Example

To look up information for the IP address `8.8.8.8`, run:
```bash
python main.py 8.8.8.8
```

### Error Handling

If the tool encounters an error (e.g., invalid IP address), it will display an error message. Ensure the IP address is correctly formatted and try again.

## Support and Documentation

For further assistance or to report issues, please contact our support team or visit our [documentation page](#) for more detailed guides and troubleshooting tips.

```