# Parse Music User Manual

Welcome to the Parse Music software! This tool is designed to help you convert a string of musical notes, represented in a special ASCII format, into a list of integers that correspond to the duration of each note in beats.

## Main Functionality

The primary function of this software is `parse_music`, which takes a string of musical notes and returns a list of integers. Each integer represents the number of beats a note lasts. The software recognizes the following notes:

- `'o'` - Whole note, lasts four beats
- `'o|'` - Half note, lasts two beats
- `'.|'` - Quarter note, lasts one beat

### Example

```python
>>> parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: Download the code to your local machine.

3. **Navigate to the project directory**: Use your command line interface to navigate to the directory where the code is located.

## How to Use

1. **Open the main.py file**: This file contains the `parse_music` function.

2. **Use the function**: You can call the `parse_music` function with a string of musical notes as input. The function will return a list of integers representing the beats for each note.

3. **Run the code**: Execute the Python script to see the results.

### Example Usage

```python
from main import parse_music

# Example input string
music_string = 'o o| .| o| o| .| .| .| .| o o'

# Parse the music string
beats = parse_music(music_string)

# Output the result
print(beats)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

## Support

If you encounter any issues or have questions about using the software, please feel free to reach out to our support team. We are here to help you make the most out of the Parse Music tool.

Thank you for choosing our software to assist with your musical note parsing needs!