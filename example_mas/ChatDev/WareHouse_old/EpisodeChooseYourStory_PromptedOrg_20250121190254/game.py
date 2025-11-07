'''
Defines the Game class, which manages the game flow.
'''
from story_segment import StorySegment
from player_state import PlayerState
class Game:
    def __init__(self):
        self.player_state = PlayerState()
        self.story_segments = self.create_story()
        self.current_segment = self.story_segments.get("segment1")
    def create_story(self):
        # Example story setup
        segment1 = StorySegment(
            "You find yourself in a dark forest. Two paths lie ahead.",
            {
                "Take the left path": "segment2",
                "Take the right path": "segment3"
            }
        )
        segment2 = StorySegment(
            "The left path leads to a peaceful village.",
            {
                "Talk to the villagers": "segment4",
                "Continue through the village": "segment5"
            }
        )
        segment3 = StorySegment(
            "The right path leads to a haunted castle.",
            {
                "Enter the castle": "segment6",
                "Run away": "segment7"
            }
        )
        segment4 = StorySegment(
            "The villagers welcome you warmly.",
            {
                "Stay with the villagers": "ending1",
                "Leave the village": "segment5"
            }
        )
        segment5 = StorySegment(
            "You continue your journey and find a treasure chest.",
            {
                "Open the chest": "ending2",
                "Ignore the chest": "ending3"
            }
        )
        segment6 = StorySegment(
            "Inside the castle, you find a mysterious figure.",
            {
                "Talk to the figure": "ending4",
                "Fight the figure": "ending5"
            }
        )
        segment7 = StorySegment(
            "You run away safely, but miss out on an adventure.",
            {
                "Reflect on your journey": "ending6"
            }
        )
        return {
            "segment1": segment1,
            "segment2": segment2,
            "segment3": segment3,
            "segment4": segment4,
            "segment5": segment5,
            "segment6": segment6,
            "segment7": segment7
        }
    def start_game(self):
        while self.current_segment:
            self.current_segment.present()
            choice = None
            choice_list = list(self.current_segment.choices.keys())
            while choice not in range(1, len(choice_list) + 1):
                try:
                    choice = int(input("Enter the number of your choice: "))
                    if choice not in range(1, len(choice_list) + 1):
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            self.process_choice(choice_list[choice - 1])
    def process_choice(self, choice):
        next_segment_key = self.current_segment.choices.get(choice)
        if next_segment_key:
            # Update player state based on choice
            self.player_state.update_state(choice)
            # Move to the next story segment
            self.current_segment = self.story_segments.get(next_segment_key)
            if "ending" in next_segment_key:
                self.determine_ending()
                self.current_segment = None
    def determine_ending(self):
        # Determine the ending based on player state
        relationships = self.player_state.get_relationships()
        items = self.player_state.get_items()
        print("\nGame Over. Your journey ends here.")
        print(f"Relationships: {relationships}")
        print(f"Items collected: {items}")