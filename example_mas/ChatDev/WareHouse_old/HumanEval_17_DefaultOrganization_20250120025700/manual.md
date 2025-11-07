manual.md

```
# Parse Music

Parse Music is a simple Python application designed to interpret a string of musical notes represented in a special ASCII format and return a list of integers that correspond to the duration of each note in beats.

## Main Functionality

The main function provided by this application is `parse_music`, which takes a string input of musical notes and outputs a list of integers. Each integer represents the number of beats a note lasts based on the following legend:

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

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**

   This project does not require any external packages. Ensure you have Python installed.

## How to Use

1. **Prepare Your Music String**

   Create a string that represents your musical notes using the specified ASCII format.

2. **Call the `parse_music` Function**

   Use the `parse_music` function to parse your music string and obtain the beats.

3. **Interpret the Output**

   The output will be a list of integers, each representing the duration in beats of the corresponding note in your input string.

## Documentation

For further details on the implementation and usage, please refer to the inline comments and docstrings within the `main.py` file.

```