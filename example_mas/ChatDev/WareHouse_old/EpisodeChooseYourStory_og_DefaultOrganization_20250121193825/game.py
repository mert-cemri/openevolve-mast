'''
Defines the Game class which manages the game state and transitions.
'''
from narrative import NarrativeSegment, Choice
from state import GameState
from gui import GUI
class Game:
    def __init__(self):
        self.state = GameState()
        self.gui = GUI(self)
        self.segments = self.create_segments()
        self.current_segment = "segment1"  # Initialize with the starting segment
    def create_segments(self):
        # Example segments
        segment1 = NarrativeSegment(
            "You wake up in a mysterious forest. What do you do?",
            [
                Choice("Explore the forest", "segment2", {"courage": 1}),
                Choice("Stay put", "segment3", {"caution": 1})
            ]
        )
        segment2 = NarrativeSegment(
            "You find a hidden path. Do you follow it?",
            [
                Choice("Follow the path", "segment4", {"curiosity": 1}),
                Choice("Return to the clearing", "segment3", {"caution": 1})
            ]
        )
        segment3 = NarrativeSegment(
            "You decide to stay put. The forest is quiet around you.",
            [
                Choice("Wait longer", "segment1", {"patience": 1}),
                Choice("Explore the forest", "segment2", {"courage": 1})
            ]
        )
        segment4 = NarrativeSegment(
            "Following the path, you discover a hidden village.",
            [
                Choice("Enter the village", "segment5", {"bravery": 1}),
                Choice("Return to the forest", "segment2", {"caution": 1})
            ]
        )
        # Add more segments as needed
        return {
            "segment1": segment1,
            "segment2": segment2,
            "segment3": segment3,
            "segment4": segment4
        }
    def start_game(self):
        self.gui.update_display(self.segments[self.current_segment])
    def make_choice(self, choice):
        choice.apply_effects(self.state)
        self.current_segment = choice.next_segment  # Update the current segment
        next_segment = self.segments[self.current_segment]
        self.gui.update_display(next_segment)