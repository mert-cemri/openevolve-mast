# Music Parser

This software provides a function to parse a string of musical notes in a special ASCII format and returns a list of integers representing the duration of each note in beats.

## Main Function

### `parse_music`

- **Description**: This function takes a string input representing musical notes and returns a list of integers. Each integer corresponds to the duration in beats of the respective note in the input string.

- **Input**: 
  - `music_string` (str): A string representing musical notes in a special ASCII format.

- **Output**: 
  - List[int]: A list of integers where each integer represents the number of beats a note lasts.

- **Note Legend**:
  - `'o'` - Whole note, lasts four beats
  - `'o|'` - Half note, lasts two beats
  - `'.|'` - Quarter note, lasts one beat

- **Example**:
  ```python
  >>> parse_music('o o| .| o| o| .| .| .| .| o o')
  [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
  ```

## Installation

### Environment Setup

This project does not require any external dependencies, making it simple to set up. You only need Python installed on your system.

### Steps

1. **Clone the Repository**: 
   - If the code is hosted in a repository, clone it using:
     ```bash
     git clone <repository-url>
     ```
   - Navigate to the project directory:
     ```bash
     cd <project-directory>
     ```

2. **Ensure Python is Installed**:
   - Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Run the Code**:
   - You can directly run the `main.py` file to test the function:
     ```bash
     python main.py
     ```

## Usage

To use the `parse_music` function, you can import it into your Python script and call it with the desired input string. Here is a simple example:

```python
from main import parse_music

# Example music string
music_string = 'o o| .| o| o| .| .| .| .| o o'

# Parse the music string
beats = parse_music(music_string)

# Output the result
print(beats)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This manual provides all the necessary information to set up and use the music parser function effectively. If you encounter any issues or have questions, please refer to the documentation or contact support.