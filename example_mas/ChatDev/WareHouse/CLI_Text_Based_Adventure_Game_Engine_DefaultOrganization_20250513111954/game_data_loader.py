'''
Utility class to load game data from a JSON file.
'''
import json
from room import Room
class GameDataLoader:
    @staticmethod
    def load(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            rooms = {}
            for room_data in data['rooms']:
                room = Room(
                    name=room_data['name'],
                    description=room_data['description'],
                    items=room_data.get('items', []),
                    choices=room_data.get('choices', {})
                )
                rooms[room.name] = room
            return rooms