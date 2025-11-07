#!/usr/bin/env python3
import json
class GameEngine:
    def __init__(self, game_data):
        self.game_data = game_data
        self.current_room = self.game_data['start_room']
        self.inventory = []
    def run(self):
        while True:
            print(self.current_room['description'])
            print('Choices:')
            for choice in self.current_room['choices']:
                print(choice['text'])
            choice = input('> ')
            if choice == 'quit':
                break
            self.current_room = self.game_data['rooms'][choice]
            self.inventory.append(choice)
        print('Game Over')