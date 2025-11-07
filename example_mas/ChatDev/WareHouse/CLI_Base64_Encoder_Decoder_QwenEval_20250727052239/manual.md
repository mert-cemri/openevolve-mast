# Base64 CLI Tool User Manual

## Overview

The Base64 CLI Tool is a simple command-line utility designed to encode and decode strings using Base64 encoding. This tool is built with Python and is easy to use, making it a handy utility for developers and anyone who needs to work with Base64 encoded data.

## Main Functions

- **Encode**: Converts a plain text string into a Base64 encoded string.
- **Decode**: Converts a Base64 encoded string back into its original plain text form.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository (Optional)**: If you want to clone the repository, you can do so using Git. Otherwise, you can download the source code as a ZIP file and extract it.
   ```bash
   git clone https://github.com/your-repo/base64-cli-tool.git
   cd base64-cli-tool
   ```

2. **Install Dependencies**: This tool does not require any third-party packages. However, ensure that Python is correctly installed and added to your system's PATH.

## Usage

### Command-Line Interface (CLI)

The main entry point for the Base64 CLI Tool is `main.py`. You can run this script from the command line to encode or decode strings.

#### Basic Usage

```bash
python main.py <encode|decode> <string>
```

- **encode**: Specifies that you want to encode the provided string.
- **decode**: Specifies that you want to decode the provided string.
- **<string>**: The string you want to encode or decode.

#### Examples

1. **Encoding a String**

   ```bash
   python main.py encode "Hello, World!"
   ```

   **Output:**

   ```
   Encoded: SGVsbG8sIFdvcmxkIQ==
   ```

2. **Decoding a String**

   ```bash
   python main.py decode "SGVsbG8sIFdvcmxkIQ=="
   ```

   **Output:**

   ```
   Decoded: Hello, World!
   ```

### Graphical User Interface (GUI)

The tool also includes a graphical user interface (GUI) for those who prefer a visual interface over the command line. To use the GUI, run `gui_interface.py`.

#### Steps to Run the GUI

1. **Run the GUI Script**

   ```bash
   python gui_interface.py
   ```

2. **Using the GUI**

   - Enter the string you want to encode or decode in the text box.
   - Click the "Encode" button to encode the string.
   - Click the "Decode" button to decode the string.
   - The result will be displayed below the buttons.

## Troubleshooting

- **Invalid Action Error**: If you provide an invalid action (anything other than "encode" or "decode"), the tool will display an error message.
- **Decoding Error**: If the provided string is not a valid Base64 encoded string, the tool will display an error message.

## Contributing

We welcome contributions to this project! If you have any ideas for improvements or bug fixes, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/your-repo/base64-cli-tool).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This manual should provide a comprehensive guide for users to understand and use the Base64 CLI Tool effectively. If you have any further questions or need additional assistance, feel free to reach out!