'''
Main module to run the interactive storytelling game.
'''
from story_manager import StoryManager
from player import Player
from utilities import print_with_delay
class Game:
    def __init__(self):
        self.story_manager = StoryManager()
        self.player = Player()
        self.current_segment = self.story_manager.get_initial_segment()
    def start_game(self):
        print_with_delay("Welcome to the Interactive Storytelling Game!")
        while self.current_segment:
            self.display_story_segment()
            choices = self.current_segment.get_choices()
            choice = None
            while choice not in choices:
                choice = input("What do you choose? ")
                if choice not in choices:
                    print_with_delay("Invalid choice. Please try again.")
            self.make_choice(choice)
    def make_choice(self, choice):
        self.player.update_relationships(choice)
        self.player.update_items(choice)
        self.current_segment = self.story_manager.get_next_segment(self.current_segment, choice)
    def display_story_segment(self):
        print_with_delay(self.current_segment.text)
if __name__ == "__main__":
    game = Game()
    game.start_game()