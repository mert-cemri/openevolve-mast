'''
Chance class to handle chance events.
'''
import random
class Chance:
    def draw_card(self, player):
        effects = [
            lambda p: setattr(p, 'money', p.money + 50),
            lambda p: setattr(p, 'money', p.money - 50),
            lambda p: print(f"{p.name} moves forward 3 spaces."),
            # Add more effects as needed
        ]
        effect = random.choice(effects)
        effect(player)
        print(f"{player.name} drew a chance card.")