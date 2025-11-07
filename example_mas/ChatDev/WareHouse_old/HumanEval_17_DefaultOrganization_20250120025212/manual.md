# Music Parser User Manual

Welcome to the Music Parser software! This tool is designed to parse a string of musical notes in a special ASCII format and return a list of integers representing the duration of each note in beats. This user manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it effectively.

## Main Functions

The primary function of the Music Parser software is `parse_music`, which takes a string of musical notes and returns a list of integers corresponding to the duration of each note in beats. The function recognizes the following note symbols:

- `'o'`: Whole note, lasts four beats
- `'o|'`: Half note, lasts two beats
- `'.|'`: Quarter note, lasts one beat

### Example Usage

```python
from main import parse_music

# Example input string
music_string = 'o o| .| o| o| .| .| .| .| o o'

# Parse the music string
beats = parse_music(music_string)

# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(beats)
```

## Installation

The Music Parser software is implemented in Python and does not require any external dependencies. To get started, ensure you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

### Quick Install

1. Clone or download the repository containing the `main.py` file.
2. Navigate to the directory containing the `main.py` file.

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located.
3. Run your Python script or interactive session to use the `parse_music` function as demonstrated in the example usage.

## Additional Information

- The software is designed to be lightweight and efficient, with no external dependencies required.
- Ensure your input string follows the correct format with spaces separating each note symbol.

Thank you for choosing the Music Parser software. We hope it meets your needs for parsing musical notes efficiently! If you have any questions or need further assistance, please feel free to reach out.