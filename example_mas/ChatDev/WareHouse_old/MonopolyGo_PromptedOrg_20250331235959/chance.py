'''
ChanceCard class to represent simplified chance cards.
'''
import random
class ChanceCard:
    def __init__(self):
        self.cards = [
            ("Win lottery! Collect $200", lambda player: setattr(player, 'money', player.money + 200)),
            ("Pay hospital fees of $100", lambda player: player.pay(100)),
            ("Go to Jail!", lambda player: setattr(player, 'in_jail', True)),
            ("Found money on street! Collect $50", lambda player: setattr(player, 'money', player.money + 50)),
            ("Speeding fine! Pay $50", lambda player: player.pay(50))
        ]
    def draw_card(self, player):
        card = random.choice(self.cards)
        print(f"Chance Card: {card[0]}")
        card[1](player)
        print(f"{player.name}'s new balance: ${player.money}")