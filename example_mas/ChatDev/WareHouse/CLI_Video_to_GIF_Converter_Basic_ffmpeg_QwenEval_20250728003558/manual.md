# Video to GIF Converter Tool

## Quick Overview

The Video to GIF Converter Tool is a command-line interface (CLI) application that allows users to convert the first 5 seconds of a video file into an animated GIF. This tool is built using Python and relies on the `ffmpeg` library for video processing.

## 📦 Installation

### Prerequisites

1. **Python**: Ensure you have Python 3.6 or later installed on your system.
2. **ffmpeg**: Install `ffmpeg` on your system. You can download it from the official [FFmpeg website](https://ffmpeg.org/download.html) and follow the installation instructions for your operating system.

### Installing the Tool

1. **Clone the Repository**: Clone the repository containing the Video to GIF Converter Tool from GitHub.
   ```bash
   git clone https://github.com/ChatDev/video-to-gif-converter.git
   cd video-to-gif-converter
   ```

2. **Install Python Dependencies**: Although this tool does not require any additional Python packages, it's a good practice to use a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Basic Command

To convert the first 5 seconds of a video file into an animated GIF, use the following command:
```bash
python main.py <path_to_video_file>
```

### Example

Suppose you have a video file named `example.mp4` in your current directory. You can convert the first 5 seconds of this video into a GIF by running:
```bash
python main.py example.mp4
```

This will generate a file named `example.gif` in the same directory.

## 🛠️ Main Functions

### Input Validation

Before attempting to convert the video, the tool checks if the provided file path is valid. It ensures that the file exists, is readable, and is a video file.

### Video Conversion

The tool uses `ffmpeg` to extract the first 5 seconds of the video and convert it into an animated GIF. The conversion process includes setting the frame rate to 10 fps and scaling the video to a width of 320 pixels while maintaining the aspect ratio.

### Error Handling

The tool includes error handling to manage common issues such as:
- `ffmpeg` not being installed or not in the system's PATH.
- The provided file path not being valid.
- Conversion failures due to issues with the video file.

## 📖 Documentation

For more detailed information, including advanced usage and troubleshooting, please refer to the [full documentation](https://github.com/ChatDev/video-to-gif-converter).

## 🙋‍♂️ Support

If you encounter any issues or have questions, please feel free to open an issue on the [GitHub repository](https://github.com/ChatDev/video-to-gif-converter/issues).

---

This manual provides a comprehensive guide to using the Video to GIF Converter Tool, covering installation, usage, and troubleshooting. We hope you find it helpful!