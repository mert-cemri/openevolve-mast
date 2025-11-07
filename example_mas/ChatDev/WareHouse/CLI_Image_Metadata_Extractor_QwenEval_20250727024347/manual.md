# Image Metadata Extractor CLI Tool

## Description

The Image Metadata Extractor CLI Tool is a command-line utility designed to extract and display basic metadata from JPEG and PNG image files. The metadata includes the image format, resolution, and creation date if available. This tool is built using Python and leverages the Pillow and ExifRead libraries for image processing and metadata extraction.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps to Install

1. **Clone the Repository**

   Open your terminal and run the following command to clone the repository:

   ```bash
   git clone https://github.com/ChatDev/image-metadata-extractor.git
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd image-metadata-extractor
   ```

3. **Install Dependencies**

   Use pip to install the required dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the following packages:
   - Pillow (for image processing)
   - ExifRead (for extracting EXIF metadata)

## Usage

### Command-Line Interface (CLI)

The CLI tool allows you to extract metadata from an image file by providing the file path as a command-line argument.

#### Basic Usage

1. **Run the CLI Tool**

   Use the following command to run the tool:

   ```bash
   python main.py <image_path>
   ```

   Replace `<image_path>` with the path to your image file.

2. **Example**

   ```bash
   python main.py /path/to/image.jpg
   ```

   **Output:**

   ```
   Format: JPEG
   Resolution: (1920, 1080)
   Creation Date: 2023:01:01 12:34:56
   ```

### Graphical User Interface (GUI)

The GUI provides a user-friendly interface for selecting an image file and viewing its metadata.

#### Steps to Use the GUI

1. **Run the GUI Tool**

   Use the following command to start the GUI:

   ```bash
   python gui.py
   ```

2. **Select an Image File**

   - Click the "Browse" button to open a file dialog.
   - Navigate to the desired image file and select it.

3. **View Metadata**

   - The metadata will be displayed in the GUI window.

   **Example:**

   ```
   Format: PNG
   Resolution: (800, 600)
   Creation Date: Not available
   ```

## Main Functions

### CLI Tool

- **Extract Metadata**: The `ImageMetadataExtractor` class handles the extraction of metadata from image files.
- **Command-Line Interface**: The `cli.py` script provides a command-line interface for the tool.

### GUI Tool

- **Graphical User Interface**: The `gui.py` script provides a graphical user interface for the tool.
- **File Selection**: Users can select an image file using a file dialog.
- **Metadata Display**: The metadata is displayed in the GUI window.

## Troubleshooting

### Common Issues

- **File Not Found**: Ensure that the provided image file path is correct.
- **Unsupported File Format**: The tool supports only JPEG and PNG files.
- **Missing Dependencies**: Ensure that all dependencies are installed correctly.

### Solutions

- **Check File Path**: Verify that the file path is correct and the file exists.
- **Supported Formats**: Ensure that the image file is in JPEG or PNG format.
- **Install Dependencies**: Run `pip install -r requirements.txt` to install all dependencies.

## Contributing

We welcome contributions to the Image Metadata Extractor CLI Tool. If you have any suggestions, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/ChatDev/image-metadata-extractor).

## License

The Image Metadata Extractor CLI Tool is released under the MIT License. See the [LICENSE](https://github.com/ChatDev/image-metadata-extractor/blob/main/LICENSE) file for more details.

---

This manual should provide a comprehensive guide for users to install, use, and troubleshoot the Image Metadata Extractor CLI Tool. If you have any further questions or need additional assistance, feel free to reach out.