'''
Main entry point for the interactive storytelling game.
'''
from story_manager import StoryManager
from player_state import PlayerState
from story_segment import StorySegment
class Game:
    def __init__(self):
        self.story_manager = StoryManager()
        self.player_state = PlayerState()
        self.current_segment = None
    def start_game(self):
        self.story_manager.load_story()
        self.current_segment = self.story_manager.get_segment("start")
        while self.current_segment:
            self.current_segment.display()
            choices = self.current_segment.get_choices()
            choice = self.process_choice(choices)
            self.player_state.update_state(choice.effects)
            self.current_segment = self.story_manager.get_segment(choice.next_segment_id)
        self.determine_ending()
    def process_choice(self, choices):
        while True:
            try:
                print("Choose an option:")
                for idx, choice in enumerate(choices):
                    print(f"{idx + 1}: {choice.description}")
                selected = self.get_user_input("Enter choice number: ", len(choices))
                return choices[selected]
            except ValueError:
                print("Invalid input. Please enter a number.")
    def get_user_input(self, prompt, num_choices):
        while True:
            try:
                selected = int(input(prompt)) - 1
                if 0 <= selected < num_choices:
                    return selected
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    def determine_ending(self):
        # Example logic to determine the ending based on player_state
        state = self.player_state.get_state()
        if state.get("friendship", 0) > 0:
            print("You have made a friend along the way. Your journey ends with companionship.")
        elif state.get("wealth", 0) > 0:
            print("You have found wealth on your journey. Your adventure ends in prosperity.")
        else:
            print("The journey ends without significant change. Thank you for playing!")
if __name__ == "__main__":
    game = Game()
    game.start_game()