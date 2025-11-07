```markdown
# IP Address Lookup CLI Tool

This CLI tool allows users to look up IP address information, such as geolocation and ISP details, using the public IP geolocation API provided by ip-api.com. The user provides an IP address, and the tool fetches and displays the relevant information.

## Main Functions

- **Fetch IP Information**: The tool makes an API request to ip-api.com to retrieve information about the specified IP address.
- **Display Results**: The tool displays the fetched IP information in a user-friendly format, including details like country, region, city, ISP, latitude, and longitude.

## Installation

### Prerequisites

- Ensure you have Python installed on your system. This tool requires Python 3.x.
- You will also need `pip`, the Python package installer, to install the required dependencies.

### Quick Install

1. **Clone the Repository**: First, clone the repository containing the CLI tool to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use `pip` to install the necessary Python packages listed in the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the Tool**: Navigate to the directory containing `main.py` and execute the script using Python, providing the IP address you wish to look up as an argument.

   ```bash
   python main.py <IP_ADDRESS>
   ```

   Replace `<IP_ADDRESS>` with the actual IP address you want to query.

2. **Example Usage**:

   ```bash
   python main.py 8.8.8.8
   ```

   This command will fetch and display information about the IP address `8.8.8.8`.

## Error Handling

- If the tool encounters an error while fetching data (e.g., due to network issues or an invalid IP address), it will display an appropriate error message.
- Ensure the IP address is correctly formatted to avoid errors.

## Support

For any issues or questions regarding the tool, please contact our support team or refer to the documentation provided in the repository.

```
