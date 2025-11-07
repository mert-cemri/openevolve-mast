```markdown
# Video to GIF Converter CLI Tool

This tool allows you to convert a short segment of a video file (e.g., the first 5 seconds) into an animated GIF using the command line. It leverages `ffmpeg` for the conversion process.

## Main Functions

- **Convert Video to GIF**: The primary function of this tool is to convert the first 5 seconds of a given video file into a GIF format. This is achieved using `ffmpeg`, a powerful multimedia processing tool.

## Installation

### Prerequisites

- **Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

- **ffmpeg**: This tool requires `ffmpeg` to be installed on your system. You can install `ffmpeg` using your system's package manager or download it from the [official website](https://ffmpeg.org/download.html).

  - **For Ubuntu/Debian**: 
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```

  - **For macOS** (using Homebrew):
    ```bash
    brew install ffmpeg
    ```

  - **For Windows**: Download the executable from the [ffmpeg website](https://ffmpeg.org/download.html) and follow the installation instructions.

### Installation Steps

1. **Clone the Repository**: Clone the repository containing the CLI tool to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: This project uses Python's standard libraries, so no additional Python packages are required.

## Usage

### Running the Tool

1. **Navigate to the Project Directory**: Ensure you are in the directory where the tool is located.

2. **Execute the CLI Tool**: Use the following command to convert a video file to a GIF.

   ```bash
   python main.py <path-to-video-file>
   ```

   Replace `<path-to-video-file>` with the path to the video file you wish to convert.

### Example

To convert a video located at `videos/sample.mp4` to a GIF, run:

```bash
python main.py videos/sample.mp4
```

Upon successful conversion, a GIF file with the same name as the video (but with a `.gif` extension) will be created in the same directory.

## Troubleshooting

- **ffmpeg Not Found**: If you encounter an error indicating that `ffmpeg` is not found, ensure that it is installed and that its path is added to your system's PATH environment variable.

- **Conversion Errors**: If the conversion fails, check the error message for details. Common issues include incorrect file paths or unsupported video formats.

## Support

For further assistance, please contact our support team or refer to the documentation provided with the tool.

```
