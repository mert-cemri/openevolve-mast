'''
Main file to initialize and run the interactive storytelling game.
'''
from story_node import StoryNode
from player import Player
from gui import GUI
import json
import os
class Game:
    def __init__(self):
        self.player = Player()
        self.story_nodes = self.load_story_nodes()
        self.current_node = self.story_nodes[0]
        self.gui = None
    def load_story_nodes(self):
        with open('story_nodes.json', 'r') as file:
            nodes_data = json.load(file)
        return [StoryNode(node["text"], node["choices"]) for node in nodes_data]
    def start(self):
        if os.environ.get('DISPLAY'):
            self.gui = GUI(self)
            self.gui.display_node(self.current_node)
            self.gui.run()
        else:
            self.run_cli()
    def make_choice(self, choice):
        self.player.update_state(choice)
        next_node_index = self.current_node.choices.get(choice)
        if next_node_index is not None:
            self.current_node = self.story_nodes[next_node_index]
            if self.gui:
                self.gui.display_node(self.current_node)
            else:
                self.display_cli_node(self.current_node)
        else:
            if self.gui:
                self.gui.display_node(StoryNode("The End. Thank you for playing!", {}))
            else:
                print("The End. Thank you for playing!")
    def run_cli(self):
        self.display_cli_node(self.current_node)
        while True:
            choice = input("Enter your choice: ")
            if choice in self.current_node.get_choices():
                self.make_choice(choice)
            else:
                print("Invalid choice. Please try again.")
    def display_cli_node(self, node):
        print(node.text)
        for choice in node.get_choices():
            print(f"- {choice}")
if __name__ == "__main__":
    game = Game()
    game.start()