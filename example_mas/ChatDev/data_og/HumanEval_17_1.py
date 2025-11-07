'''
Input to this function is a string representing musical notes in a special ASCII format.
Your task is to parse this string and return a list of integers corresponding to how many beats does each
note last.
Here is a legend:
'o' - whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quarter note, lasts one beat
>>> parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
'''
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Split the input string by spaces to get individual notes
    notes = music_string.split()
    # Create a mapping of note symbols to their respective beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    # Parse the notes and convert them to their respective beats
    beats = [note_to_beats[note] for note in notes]
    return beats