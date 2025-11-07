'''
Manages loading and retrieving story segments.
'''
from story_segment import StorySegment, Choice
class StoryManager:
    def __init__(self):
        self.segments = {}
    def load_story(self):
        # Example story loading
        self.segments["start"] = StorySegment(
            "You are in a dark forest. Two paths lie ahead.",
            [
                Choice("Take the left path", "left_path", {"courage": 1}),
                Choice("Take the right path", "right_path", {"caution": 1})
            ]
        )
        self.segments["left_path"] = StorySegment(
            "You encounter a friendly elf.",
            [
                Choice("Talk to the elf", "elf_talk", {"friendship": 1}),
                Choice("Ignore the elf", "ignore_elf", {"friendship": -1})
            ]
        )
        self.segments["right_path"] = StorySegment(
            "You find a treasure chest.",
            [
                Choice("Open the chest", "open_chest", {"wealth": 1}),
                Choice("Leave the chest", "leave_chest", {"caution": 1})
            ]
        )
        # More segments can be added here
    def get_segment(self, segment_id):
        return self.segments.get(segment_id)