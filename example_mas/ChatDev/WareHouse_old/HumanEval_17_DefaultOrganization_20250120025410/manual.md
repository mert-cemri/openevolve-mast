manual.md

```
# Parse Music

Parse Music is a simple Python application designed to interpret a string of musical notes represented in a special ASCII format and return a list of integers indicating the duration in beats for each note.

## Main Functionality

The core functionality of this software is provided by the `parse_music` function. This function takes a string input representing musical notes and outputs a list of integers, where each integer corresponds to the number of beats a note lasts. The mapping of notes to beats is as follows:

- `'o'` - Whole note, lasts four beats
- `'o|'` - Half note, lasts two beats
- `'.|'` - Quarter note, lasts one beat

### Example

```python
>>> parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

## Installation

This application does not require any external dependencies, making it straightforward to set up and run. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are necessary since there are no external dependencies.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python interpreter and import the `parse_music` function:

   ```bash
   python
   ```

   ```python
   from main import parse_music
   ```

4. Use the `parse_music` function by passing a string of musical notes:

   ```python
   result = parse_music('o o| .| o| o| .| .| .| .| o o')
   print(result)
   ```

   This will output:

   ```
   [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
   ```

## Documentation

For further details on the implementation and usage of the `parse_music` function, please refer to the docstring within the `main.py` file. This provides a comprehensive explanation of the function's input, output, and example usage.

```