# Parse Music User Manual

Welcome to the Parse Music software! This tool is designed to help you parse a string of musical notes in a special ASCII format and return a list of integers representing the duration of each note in beats.

## Main Functionality

The main function provided by this software is `parse_music`, which takes a string of musical notes and returns a list of integers corresponding to the duration of each note in beats. The function recognizes the following notes:

- `'o'` - Whole note, lasts four beats
- `'o|'` - Half note, lasts two beats
- `'.|'` - Quarter note, lasts one beat

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

### Environment Setup

This software does not require any external dependencies, making it easy to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to the cloned repository:
   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can directly run the `main.py` file or import the `parse_music` function into your own Python scripts.

## How to Use

1. **Prepare Your Input**: Create a string representing the musical notes you want to parse. Ensure the notes are separated by spaces.

2. **Call the Function**: Use the `parse_music` function to parse your input string and obtain the list of beats.

3. **Interpret the Output**: The function will return a list of integers, each representing the duration in beats of the corresponding note in your input string.

## Additional Information

- **No External Dependencies**: This software does not require any additional Python packages, making it lightweight and easy to integrate into other projects.

- **Customization**: You can easily extend the functionality by adding more note types and their corresponding beats in the `note_to_beats` dictionary within the `parse_music` function.

We hope this tool helps you in your musical endeavors! If you have any questions or need further assistance, please feel free to reach out.