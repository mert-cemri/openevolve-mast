# Music Parser User Manual

Welcome to the Music Parser software! This tool is designed to parse a string of musical notes represented in a special ASCII format and return a list of integers corresponding to the duration of each note in beats.

## Main Functions

The primary function of this software is:

### `parse_music(music_string: str) -> List[int]`

- **Input**: A string representing musical notes in a special ASCII format.
- **Output**: A list of integers where each integer represents the number of beats a note lasts.

### Note Legend

- `'o'`: Whole note, lasts four beats.
- `'o|'`: Half note, lasts two beats.
- `'.|'`: Quarter note, lasts one beat.

### Example

```python
>>> parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python, making it easy to set up and use.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone or download the repository containing the `main.py` file.
3. Navigate to the directory containing `main.py`.

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the Python script with the desired input string. For example:

```bash
python main.py
```

4. The script will output a list of integers representing the beats of each note in the input string.

## Documentation

For further details on how to use the software, you can refer to the comments within the `main.py` file. The function is straightforward and designed to be easily integrated into larger projects if needed.

## Support

If you encounter any issues or have questions about using the Music Parser, please feel free to reach out to our support team. We are here to help you make the most out of this tool.

Thank you for choosing Music Parser! We hope it enhances your musical projects and makes your workflow more efficient.