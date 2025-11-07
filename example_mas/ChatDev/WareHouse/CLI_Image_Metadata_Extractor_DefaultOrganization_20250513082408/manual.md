```markdown
# Image Metadata CLI Tool

A command-line interface (CLI) tool for extracting and displaying basic metadata from image files (JPEG, PNG). This tool allows users to easily obtain information such as resolution, format, and creation date (if available) from their image files.

## Main Functions

- **Extract Image Metadata**: Retrieve essential metadata from JPEG and PNG image files, including format, resolution, and creation date (if available).
- **Display Metadata**: Present the extracted metadata in a user-friendly format on the command line.

## Installation

To use the Image Metadata CLI Tool, you need to set up your environment by installing the required dependencies. Follow the steps below:

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use `pip` to install the required Python packages listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

   This will install the Pillow library, which is necessary for image processing.

## How to Use

Once you have installed the necessary dependencies, you can use the CLI tool to extract metadata from your image files.

### Usage

Run the following command in your terminal, replacing `<image_file_path>` with the path to your image file:

```bash
python main.py <image_file_path>
```

### Example

To extract metadata from an image located at `images/sample.jpg`, use the command:

```bash
python main.py images/sample.jpg
```

### Output

The tool will display the extracted metadata in the terminal. For example:

```
Image Metadata:
Format: JPEG
Resolution: 1920x1080
Creation Date: 2023:10:01 12:34:56
```

If there is an error (e.g., the file path is incorrect or the file is not a valid image), the tool will display an appropriate error message.

## Troubleshooting

- **Error: No file path provided**: Ensure you provide a valid image file path as an argument when running the tool.
- **Error extracting metadata**: Check if the file path is correct and the file is a valid JPEG or PNG image.

## Documentation

For further information and updates, please refer to the project's documentation or contact support.

```
```