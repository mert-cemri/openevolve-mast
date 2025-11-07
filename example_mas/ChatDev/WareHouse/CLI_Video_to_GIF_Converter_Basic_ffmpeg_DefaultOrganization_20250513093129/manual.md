```markdown
# Video to GIF Converter CLI Tool

A simple command-line interface (CLI) tool to convert a short video file segment into an animated GIF using `ffmpeg`.

## Overview

This tool allows you to convert the first 5 seconds of a video file into an animated GIF. It is designed to be simple and efficient, leveraging the powerful `ffmpeg` utility for video processing.

## Main Functions

- **Convert Video to GIF**: Extracts the first 5 seconds of a video file and converts it into a GIF format.
- **Error Handling**: Checks for the existence of the input video file and the installation of `ffmpeg` before proceeding with the conversion.

## Installation

### Prerequisites

- **Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/).
- **FFmpeg**: This tool requires `ffmpeg` to be installed and accessible from your system's PATH. You can download it from [ffmpeg.org](https://ffmpeg.org/download.html).

### Environment Setup

1. **Clone the Repository**: Clone the repository containing the CLI tool to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Python Dependencies**: No additional Python packages are required. Ensure `ffmpeg` is installed on your system for the tool to function.

## Usage

### Running the Tool

1. **Open a Terminal**: Navigate to the directory where the tool is located.

2. **Execute the Command**: Use the following command to convert a video file to a GIF.
   ```bash
   python main.py <video_path> <output_path>
   ```

   - `<video_path>`: Path to the input video file.
   - `<output_path>`: Path where the output GIF file will be saved.

### Example

To convert a video located at `videos/sample.mp4` and save the GIF as `output/sample.gif`, run:
```bash
python main.py videos/sample.mp4 output/sample.gif
```

### Error Messages

- **Invalid Video Path**: If the specified video file does not exist, the tool will prompt you to provide a valid path.
- **FFmpeg Not Installed**: If `ffmpeg` is not installed or not found in the system's PATH, the tool will display an error message.

## Support

For any issues or questions, please contact our support team or visit our [GitHub repository](<repository-url>) for more information.

```
```