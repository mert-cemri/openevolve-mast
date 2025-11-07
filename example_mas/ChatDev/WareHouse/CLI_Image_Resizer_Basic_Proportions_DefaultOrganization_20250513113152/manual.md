# CLI Image Resizer User Manual

Welcome to the CLI Image Resizer application! This tool allows you to resize images from the command line while maintaining their aspect ratio. Below you will find detailed instructions on how to install, use, and understand the main functions of this software.

## Main Functions

The CLI Image Resizer application provides the following main functions:

- **Resize Images**: Resize an image to a specified width or height while maintaining the aspect ratio.
- **Save Resized Images**: Save the resized image to a new file.

## Installation

To use the CLI Image Resizer, you need to have Python installed on your system. Additionally, you will need to install the required dependencies. Follow the steps below to set up your environment:

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Dependencies

The application requires the Pillow library for image processing. You can install it using pip:

```bash
pip install -r requirements.txt
```

This command will install the necessary dependencies listed in the `requirements.txt` file.

## Usage

Once you have installed the dependencies, you can use the CLI Image Resizer from the command line. Follow the instructions below to resize an image:

### Step 1: Open Command Line Interface

Open your terminal or command prompt.

### Step 2: Run the Application

Use the following command to run the application:

```bash
python main.py <image_path> [--width <target_width>] [--height <target_height>] <output_path>
```

- `<image_path>`: Path to the input image file you want to resize.
- `--width <target_width>`: (Optional) Target width for the resized image.
- `--height <target_height>`: (Optional) Target height for the resized image.
- `<output_path>`: Path where the resized image will be saved.

**Note**: You must specify either the target width or the target height to resize the image.

### Example

To resize an image to a width of 300 pixels and save it as `resized_image.jpg`, use the following command:

```bash
python main.py input_image.jpg --width 300 resized_image.jpg
```

## Error Handling

If an error occurs during the resizing process, the application will print an error message to the console. Ensure that the image path is correct and that you have specified either a target width or height.

## Conclusion

The CLI Image Resizer is a simple yet powerful tool for resizing images directly from the command line. By following the instructions in this manual, you should be able to easily resize and save images while maintaining their aspect ratio. If you encounter any issues, please ensure that all dependencies are correctly installed and that the command syntax is followed accurately. Enjoy resizing your images!