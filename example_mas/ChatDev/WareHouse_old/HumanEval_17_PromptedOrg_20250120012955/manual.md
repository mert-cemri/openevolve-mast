# Parse Music User Manual

Welcome to the Parse Music software! This tool is designed to help you parse a string of musical notes in a special ASCII format and return a list of integers representing the duration of each note in beats.

## Main Functionality

The main function of this software is `parse_music`, which takes a string input of musical notes and outputs a list of integers. Each integer corresponds to the number of beats a note lasts. The function recognizes the following note representations:

- `'o'` - Whole note, lasts four beats
- `'o|'` - Half note, lasts two beats
- `'.|'` - Quarter note, lasts one beat

### Example Usage

```python
from main import parse_music

# Example input
music_string = 'o o| .| o| o| .| .| .| .| o o'

# Parse the music string
beats = parse_music(music_string)

# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(beats)
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Steps to Install

1. **Clone the Repository**: You can clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the repository is cloned:
   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can run the code directly using Python:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: Import the `parse_music` function from the `main.py` file.
2. **Prepare Your Input**: Create a string representing the musical notes you want to parse.
3. **Call the Function**: Pass the string to the `parse_music` function to get the list of beats.
4. **Use the Output**: The output will be a list of integers, each representing the duration of the corresponding note in beats.

## Conclusion

The Parse Music software is a simple yet powerful tool for converting musical note strings into beat durations. With no external dependencies, it is easy to set up and use. We hope this tool helps you in your musical endeavors! If you have any questions or need further assistance, please feel free to reach out.