# Image Metadata Extractor

A command-line interface (CLI) tool and graphical user interface (GUI) application for extracting and displaying basic metadata from image files (JPEG, PNG).

## Overview

The Image Metadata Extractor is a versatile tool designed to help users extract essential metadata from image files. This includes information such as the image format, resolution, and creation date (if available). The tool is available as both a CLI and a GUI application, providing flexibility for different user preferences.

## Main Functions

- **Extract Metadata**: Retrieve metadata such as format, resolution, and creation date from JPEG and PNG image files.
- **Command-Line Interface**: Use the CLI tool to quickly extract metadata by providing the image file path.
- **Graphical User Interface**: Use the GUI application for a more interactive experience, allowing users to browse and select image files.

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package manager)

### Quick Install

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install the required Python packages using the following command:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the Pillow library, which is necessary for handling image files.

## Usage

### Command-Line Interface (CLI)

1. **Navigate to the Project Directory**: Open your terminal and navigate to the directory where the project is located.

2. **Run the CLI Tool**: Use the following command to extract metadata from an image file:

   ```bash
   python main.py <path-to-image-file>
   ```

   Replace `<path-to-image-file>` with the actual path to the image file you want to analyze. The tool will display the extracted metadata in the terminal.

### Graphical User Interface (GUI)

1. **Run the GUI Application**: Execute the following command to start the GUI application:

   ```bash
   python gui.py
   ```

2. **Select an Image File**: Click the "Browse" button to open a file dialog. Select the image file you wish to analyze.

3. **View Metadata**: The extracted metadata will be displayed in the text area of the GUI. If an error occurs, an error message will be shown.

## Additional Information

- **Supported Image Formats**: The tool supports JPEG and PNG image files.
- **Error Handling**: If an error occurs during metadata extraction, an error message will be displayed, indicating the nature of the issue.

For further assistance or to report issues, please contact our support team. We hope you find the Image Metadata Extractor useful for your image analysis needs!