'''
Game module to manage the game flow and logic.
'''
from scene import Scene
from player import Player
class Game:
    def __init__(self, gui):
        self.gui = gui
        self.player = Player()
        self.current_scene = None
    def start_game(self):
        self.current_scene = Scene.load_scene("start")
        self.update_scene()
    def make_choice(self, choice_id):
        choice = self.current_scene.choices[choice_id]
        outcome = {
            'relationship_change': {},  # Add logic to determine relationship changes
            'items': []  # Add logic to determine items obtained
        }
        self.player.update_relationships(outcome)
        self.player.update_items(outcome)
        next_scene = Scene.load_scene(choice.next_scene)
        if next_scene is not None:
            self.current_scene = next_scene
            self.update_scene()
        else:
            # Display error and allow the player to choose again
            self.gui.display_error("The chosen path leads to an unknown destination. Please make another choice.")
    def update_scene(self):
        self.gui.display_scene(self.current_scene)