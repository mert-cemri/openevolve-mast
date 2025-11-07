'''
Manages chance events in the game.
'''
import random
class Chance:
    def __init__(self):
        self.events = [
            {"description": "Advance to Go (Collect $200)", "action": self.advance_to_go},
            {"description": "Bank error in your favor. Collect $75", "action": self.collect_money, "kwargs": {"amount": 75}},
            # Add more events as needed
        ]
    def draw_card(self):
        event = random.choice(self.events)
        print(event["description"])
        return event
    def advance_to_go(self, player):
        player.position = 0
        player.money += 200
    def collect_money(self, player, amount):
        player.money += amount