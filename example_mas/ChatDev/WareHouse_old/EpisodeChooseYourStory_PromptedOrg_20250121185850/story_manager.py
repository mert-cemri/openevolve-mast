'''
Manages the story structure and progression.
'''
from story_segment import StorySegment
class StoryManager:
    def __init__(self):
        self.story_data = self.load_story()
    def load_story(self):
        # Placeholder for loading story data from a file or database
        # For simplicity, we will define a simple story structure here
        return {
            "start": StorySegment("You are in a dark forest. Paths lead north and south.", {"north": "north_path", "south": "south_path"}),
            "north_path": StorySegment("You encounter a friendly wolf. He offers to guide you.", {"accept": "wolf_guide", "decline": "lost_in_forest"}),
            "south_path": StorySegment("You find a mysterious cave. Do you enter?", {"enter": "cave_exploration", "ignore": "forest_exit"}),
            # Additional segments would be defined here
        }
    def get_initial_segment(self):
        return self.story_data["start"]
    def get_next_segment(self, current_segment, choice):
        next_segment_key = current_segment.get_next_segment(choice)
        return self.story_data.get(next_segment_key, None)