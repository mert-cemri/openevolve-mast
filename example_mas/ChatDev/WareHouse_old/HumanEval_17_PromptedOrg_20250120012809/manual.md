# Parse Music User Manual

Welcome to the Parse Music software! This tool is designed to help you convert a string of musical notes in a special ASCII format into a list of integers representing the duration in beats for each note.

## Main Functionality

The primary function of this software is `parse_music`, which takes a string of musical notes and returns a list of integers. Each integer corresponds to the number of beats a note lasts. The notes are represented in a special ASCII format as follows:

- `'o'` - Whole note, lasts four beats
- `'o|'` - Half note, lasts two beats
- `'.|'` - Quarter note, lasts one beat

### Example Usage

```python
from main import parse_music

# Example input string
music_string = 'o o| .| o| o| .| .| .| .| o o'

# Parsing the music string
beats = parse_music(music_string)

# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(beats)
```

## Installation

This project does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can now run the `main.py` file to use the `parse_music` function.

## How to Use

1. **Prepare Your Music String**: Format your music string using the ASCII notation described above.

2. **Call the Function**: Use the `parse_music` function to convert the music string into a list of beats.

3. **Interpret the Output**: The output will be a list of integers, each representing the duration in beats for the corresponding note in your input string.

## Additional Information

- **No External Libraries Required**: This project is designed to be lightweight and does not require any additional Python packages beyond the standard library.

- **Customization**: You can modify the `note_to_beats` dictionary in the `main.py` file if you need to support additional note types or change the beat durations.

We hope this tool helps you efficiently parse and interpret musical notes in your projects. If you have any questions or need further assistance, please feel free to reach out.