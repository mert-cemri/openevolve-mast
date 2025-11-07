# MP3 Tag Editor CLI User Manual

## Overview

The MP3 Tag Editor CLI is a command-line interface tool designed to allow users to view and modify basic ID3 tags of MP3 files. It supports editing tags such as title, artist, album, and year. This tool is built using Python and leverages the `mutagen` library for MP3 tag manipulation.

## Features

- **View Tags**: Display the current ID3 tags of an MP3 file.
- **Modify Tags**: Update the title, artist, album, and year of an MP3 file.
- **User-Friendly CLI**: Simple and intuitive command-line interface for easy usage.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.
- `pip` (Python package installer) should be available.

### Steps to Install

1. **Clone the Repository** (if you haven't already):
   ```bash
   git clone https://github.com/ChatDev/mp3-tag-editor.git
   cd mp3-tag-editor
   ```

2. **Install Dependencies**:
   The project requires the `mutagen` library. You can install it using `pip` by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install `mutagen` directly:
   ```bash
   pip install mutagen>=1.45.1
   ```

## Usage

### Basic Commands

- **View Tags**:
  To view the current tags of an MP3 file, use the `--view` option:
  ```bash
  python main.py yourfile.mp3 --view
  ```

- **Modify Tags**:
  To modify the tags of an MP3 file, specify the tags you want to update:
  ```bash
  python main.py yourfile.mp3 --title "New Title" --artist "New Artist" --album "New Album" --year "2023"
  ```

### Command-Line Options

- `file`: The path to the MP3 file you want to edit.
- `--title`: Set the title of the MP3 file.
- `--artist`: Set the artist of the MP3 file.
- `--album`: Set the album of the MP3 file.
- `--year`: Set the year of the MP3 file.
- `--view`: View the current tags of the MP3 file.

### Examples

1. **View Tags**:
   ```bash
   python main.py example.mp3 --view
   ```

2. **Modify Tags**:
   ```bash
   python main.py example.mp3 --title "Song Title" --artist "Artist Name" --album "Album Name" --year "2023"
   ```

3. **Modify Specific Tags**:
   You can modify only specific tags if needed:
   ```bash
   python main.py example.mp3 --artist "New Artist"
   ```

## Troubleshooting

- **File Not Found**:
  If the specified file does not exist, you will receive an error message:
  ```
  Error: File 'yourfile.mp3' does not exist.
  ```

- **Invalid File Type**:
  If the specified file is not an MP3 file, you will receive an error message:
  ```
  Error: File 'yourfile.mp3' is not an MP3 file.
  ```

- **Missing Dependencies**:
  If the `mutagen` library is not installed, you will receive an error message:
  ```
  Error: The 'mutagen' library is not installed.
  Please install it using the following command:
  pip install mutagen
  ```

## Conclusion

The MP3 Tag Editor CLI is a powerful tool for managing MP3 file metadata directly from the command line. With its simple interface and robust functionality, it provides an efficient way to view and modify ID3 tags. If you encounter any issues or have suggestions for improvement, feel free to reach out to the development team.

---

This manual should provide a comprehensive guide for users to understand and utilize the MP3 Tag Editor CLI effectively.