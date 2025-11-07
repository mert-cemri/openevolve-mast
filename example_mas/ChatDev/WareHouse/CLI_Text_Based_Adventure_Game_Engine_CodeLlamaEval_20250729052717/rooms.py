#!/usr/bin/env python3
import json
class Room:
    def __init__(self, room_data):
        self.name = room_data['name']
        self.description = room_data['description']
        self.choices = room_data['choices']
    def __str__(self):
        return self.name