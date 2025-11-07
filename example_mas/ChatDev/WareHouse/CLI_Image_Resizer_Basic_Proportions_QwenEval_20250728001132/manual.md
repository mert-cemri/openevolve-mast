# Image Resizer CLI User Manual

## Overview

The Image Resizer CLI is a simple yet powerful tool designed to resize images while maintaining their aspect ratio. It accepts an image file, a target width or height, and outputs the resized image to a new file. This tool is perfect for developers, designers, and anyone who needs to quickly resize images from the command line.

## Features

- **Maintain Aspect Ratio:** Automatically adjusts the other dimension to maintain the original aspect ratio.
- **Command Line Interface (CLI):** Easy to use from the terminal or command prompt.
- **Supports Common Image Formats:** Handles most common image formats like JPEG, PNG, BMP, etc.
- **Error Handling:** Provides informative error messages to help diagnose issues.

## Installation

### Prerequisites

- **Python 3.6+**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Pillow**: A Python Imaging Library fork that the Image Resizer CLI depends on.

### Installing Dependencies

You can install the required dependencies using `pip`. Open your terminal or command prompt and run the following command:

```bash
pip install Pillow
```

## Usage

### Basic Command Structure

The basic command structure for using the Image Resizer CLI is as follows:

```bash
python main.py <input_path> <output_path> [--width <width> | --height <height>]
```

### Parameters

- **`<input_path>`**: The path to the input image file you want to resize.
- **`<output_path>`**: The path where the resized image will be saved.
- **`--width <width>`**: (Optional) The target width for the resized image.
- **`--height <height>`**: (Optional) The target height for the resized image.

### Examples

#### Example 1: Resize by Width

To resize an image to a width of 800 pixels while maintaining the aspect ratio, use the following command:

```bash
python main.py input.jpg output.jpg --width 800
```

#### Example 2: Resize by Height

To resize an image to a height of 600 pixels while maintaining the aspect ratio, use the following command:

```bash
python main.py input.jpg output.jpg --height 600
```

#### Example 3: Error Handling

If you try to specify both width and height, the tool will raise an error:

```bash
python main.py input.jpg output.jpg --width 800 --height 600
```

**Output:**

```
Error: Only one of target width or height should be specified.
```

## Troubleshooting

### Common Issues

- **File Not Found**: Ensure the input file path is correct and the file exists.
- **Invalid File Format**: The tool supports common image formats. If you encounter an error, check the file format.
- **Missing Arguments**: Ensure you specify either `--width` or `--height`.

### Solutions

- **Check File Paths**: Verify that the input and output file paths are correct.
- **Supported Formats**: Ensure the image file is in a supported format (JPEG, PNG, BMP, etc.).
- **Specify Arguments**: Always specify either `--width` or `--height` when running the tool.

## Conclusion

The Image Resizer CLI is a simple yet effective tool for resizing images from the command line. With its easy-to-use interface and robust error handling, it's perfect for anyone who needs to quickly resize images while maintaining their aspect ratio.

If you encounter any issues or have suggestions for improvement, feel free to reach out to our support team or contribute to the project on GitHub.

---

This manual should provide a comprehensive guide for users to understand and use the Image Resizer CLI effectively.