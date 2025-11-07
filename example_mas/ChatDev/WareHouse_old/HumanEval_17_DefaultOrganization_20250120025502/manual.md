# Music Parser

This software provides a function to parse a string of musical notes and return a list of integers representing the duration of each note in beats. It is designed to interpret a specific ASCII format for musical notes.

## Main Function

### `parse_music`

- **Description**: This function takes a string input representing musical notes in a special ASCII format and returns a list of integers. Each integer corresponds to the number of beats each note lasts.
  
- **Input**: A string of musical notes. The notes are represented in a specific format:
  - `'o'` - whole note, lasts four beats
  - `'o|'` - half note, lasts two beats
  - `'.|'` - quarter note, lasts one beat

- **Output**: A list of integers representing the duration of each note in beats.

- **Example**:
  ```python
  >>> parse_music('o o| .| o| o| .| .| .| .| o o')
  [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
  ```

## Installation

### Environment Setup

This software does not require any external dependencies, making it easy to set up and use. You only need to have Python installed on your system.

1. **Ensure Python is installed**: You can download and install Python from the official website: [Python.org](https://www.python.org/).

2. **Clone the repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the script**: You can execute the script directly using Python:
   ```bash
   python main.py
   ```

## Usage

To use the `parse_music` function, you can either import it into your own Python script or run it directly from the command line.

### Example Usage in a Python Script

```python
from main import parse_music

music_string = 'o o| .| o| o| .| .| .| .| o o'
beats = parse_music(music_string)
print(beats)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

### Running Directly

If you want to test the function directly, you can modify the `main.py` file to include test cases or use an interactive Python shell.

## Conclusion

This software provides a simple yet effective way to parse musical notes from a string and convert them into beats. It is lightweight and requires no additional dependencies, making it easy to integrate into larger projects or use as a standalone tool.