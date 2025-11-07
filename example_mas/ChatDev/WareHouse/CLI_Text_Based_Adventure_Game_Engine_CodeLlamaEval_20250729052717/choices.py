#!/usr/bin/env python3
import json
class Choice:
    def __init__(self, choice_data):
        self.text = choice_data['text']
        self.room = choice_data['room']
    def __str__(self):
        return self.text