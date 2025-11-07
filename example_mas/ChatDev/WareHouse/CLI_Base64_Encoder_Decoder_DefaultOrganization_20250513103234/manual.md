```markdown
# Base64 Encode/Decode CLI Tool

A simple command-line interface (CLI) tool to encode and decode strings using Base64 encoding.

## Quick Install

To use the Base64 Encode/Decode CLI Tool, ensure you have Python installed on your system. The tool requires Python version 3.6 or higher.

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the directory where the repository was cloned.

3. **Install Dependencies:**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   This will ensure that the necessary Python version is used.

## 🤔 What is this?

The Base64 Encode/Decode CLI Tool is a simple utility that allows users to encode and decode strings using Base64 encoding directly from the command line. This can be useful for various applications, including data serialization, encoding binary data, and more.

## 📖 How to Use

The tool provides two main functions: encoding and decoding strings. Users can specify the operation they want to perform and provide the input string as a command-line argument.

### Usage

To use the tool, open your command line interface and navigate to the directory where the tool is located. Use the following command structure:

```bash
python main.py <operation> <input_string>
```

- `<operation>`: Specify the operation to perform. Use `encode` to encode a string or `decode` to decode a string.
- `<input_string>`: The string you want to encode or decode.

### Examples

1. **Encoding a String:**

   To encode a string, use the `encode` operation:

   ```bash
   python main.py encode "Hello, World!"
   ```

   This will output the Base64 encoded version of "Hello, World!".

2. **Decoding a String:**

   To decode a Base64 encoded string, use the `decode` operation:

   ```bash
   python main.py decode "SGVsbG8sIFdvcmxkIQ=="
   ```

   This will output the original string "Hello, World!".

## Troubleshooting

- Ensure that you have Python 3.6 or higher installed.
- If you encounter any errors, verify that the input string is correctly formatted for the specified operation.
- For decoding, ensure that the input string is a valid Base64 encoded string.

## Support

For any questions or issues, please contact our support team or refer to the documentation provided in the repository.

```
