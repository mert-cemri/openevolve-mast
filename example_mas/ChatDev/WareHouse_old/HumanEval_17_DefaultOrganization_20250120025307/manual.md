manual.md

```
# Music Note Parser

The Music Note Parser is a simple Python application designed to interpret a string of musical notes in a special ASCII format and return a list of integers representing the duration in beats for each note.

## Main Functionality

The core function of this software is `parse_music`, which takes a string input of musical notes and outputs a list of integers. Each integer corresponds to the number of beats a note lasts. The notes are represented in a specific ASCII format:

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

### Environment Setup

This application does not require any external dependencies, making it straightforward to set up. You only need Python installed on your machine.

### Steps to Install

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd <project-directory>
   ```

3. **Run the Application**

   Since there are no external dependencies, you can directly run the Python script:

   ```bash
   python main.py
   ```

## How to Use

1. **Prepare Your Input**

   Create a string of musical notes using the specified ASCII format.

2. **Call the Function**

   Use the `parse_music` function to parse your input string.

3. **Get the Output**

   The function will return a list of integers, each representing the duration in beats of the corresponding note in the input string.

## Additional Information

This application is designed to be lightweight and easy to use, with no additional setup required beyond having Python installed. It is ideal for educational purposes or simple musical note parsing tasks.

For any questions or support, please contact the development team at ChatDev.
```