'''
This file contains the implementation of the parse_music function, which parses a string of musical notes
in a special ASCII format and returns a list of integers representing the duration in beats for each note.
'''
from typing import List
def parse_music(music_string: str) -> List[int]:
    """ 
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return a list of integers corresponding to how many beats each
    note lasts.
    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Define the mapping from note representation to beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    # Split the input string into individual notes
    notes = music_string.split()
    # Map each note to its corresponding beat count
    beats = [note_to_beats[note] for note in notes]
    return beats