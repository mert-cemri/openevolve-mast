'''
This module contains the implementation of the parse_music function, which parses a string of musical notes
in a special ASCII format and returns a list of integers representing the duration of each note in beats.
'''
from typing import List
def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.
    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Split the input string by spaces to get individual note representations
    notes = music_string.split()
    # Create a mapping from note representation to beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    # Parse each note and convert it to its corresponding beat count
    beats = [note_to_beats[note] for note in notes]
    return beats