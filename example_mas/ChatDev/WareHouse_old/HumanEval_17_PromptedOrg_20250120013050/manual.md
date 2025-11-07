# Parse Music User Manual

Welcome to the Parse Music software! This tool is designed to parse a string of musical notes in a special ASCII format and return a list of integers representing the duration of each note in beats. This manual will guide you through the installation process, introduce the main function of the software, and provide instructions on how to use it.

## Main Function

The core function of this software is `parse_music`, which takes a string input representing musical notes and outputs a list of integers corresponding to the duration of each note in beats. The function recognizes the following note representations:

- `'o'` - Whole note, lasts four beats
- `'o|'` - Half note, lasts two beats
- `'.|'` - Quarter note, lasts one beat

### Example Usage

```python
from main import parse_music

music_string = 'o o| .| o| o| .| .| .| .| o o'
beats = parse_music(music_string)
print(beats)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

## Installation

To use the Parse Music software, you need to have Python installed on your system. Follow these steps to set up your environment:

1. **Install Python**: If you haven't already, download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

3. **Set Up a Virtual Environment (Optional but Recommended)**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Dependencies**: There are no additional dependencies required for this software, as it uses only the standard Python library.

## How to Use

1. **Prepare Your Input**: Create a string representing musical notes using the specified ASCII format.

2. **Call the Function**: Use the `parse_music` function from the `main.py` file, passing your input string as an argument.

3. **Get the Output**: The function will return a list of integers, each representing the duration in beats of the corresponding note in the input string.

## Conclusion

The Parse Music software is a simple yet effective tool for converting musical note representations into beat durations. By following this manual, you should be able to set up your environment and use the software efficiently. If you have any questions or need further assistance, please feel free to reach out to our support team.