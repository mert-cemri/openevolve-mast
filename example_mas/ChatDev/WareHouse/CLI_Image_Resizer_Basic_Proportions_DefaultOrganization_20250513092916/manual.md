```markdown
# CLI Image Resizer

A simple command-line interface (CLI) tool for resizing images while maintaining their aspect ratio. This tool uses the Pillow library to handle image processing tasks.

## Quick Install

To use the CLI Image Resizer, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

This command will install the Pillow library, which is necessary for image processing.

## 🤔 What is this?

The CLI Image Resizer is a tool designed to resize images to a specified width or height while maintaining the original aspect ratio. This means that the resized image will not be distorted, preserving the original proportions.

### Main Features

- **Aspect Ratio Maintenance**: Automatically calculates the missing dimension (width or height) to ensure the image's aspect ratio is preserved.
- **Flexible Input**: Allows users to specify either the target width or height.
- **Simple CLI Interface**: Easy to use with command-line arguments for specifying input and output paths, as well as the desired dimensions.

## 📖 How to Use

### Command-Line Usage

To use the CLI Image Resizer, open your terminal or command prompt and navigate to the directory containing `main.py`. Use the following command structure:

```bash
python main.py <input_path> <output_path> --width <target_width> --height <target_height>
```

- `<input_path>`: Path to the input image file.
- `<output_path>`: Path where the resized image will be saved.
- `--width <target_width>`: (Optional) Desired width of the resized image.
- `--height <target_height>`: (Optional) Desired height of the resized image.

**Note**: You must specify either the `--width` or `--height` argument, but not both. If both are specified, the tool will prioritize the width.

### Example

To resize an image to a width of 300 pixels while maintaining aspect ratio:

```bash
python main.py input.jpg output.jpg --width 300
```

To resize an image to a height of 200 pixels while maintaining aspect ratio:

```bash
python main.py input.jpg output.jpg --height 200
```

### Error Handling

If neither `--width` nor `--height` is specified, the program will display an error message:

```
Error: Please specify either target width or height.
```

## Additional Information

For more information on the Pillow library and its capabilities, please refer to the [Pillow documentation](https://pillow.readthedocs.io/en/stable/).

This tool is designed to be simple and efficient, making it easy for users to resize images without needing to understand complex image processing techniques.
```
