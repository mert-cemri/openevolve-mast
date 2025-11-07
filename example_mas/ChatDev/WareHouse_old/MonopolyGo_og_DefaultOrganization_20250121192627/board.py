'''
Represents the game board.
'''
from property import Property
import random
class Board:
    def __init__(self):
        self.properties = [
            Property("Mediterranean Avenue", 60, 2),
            Property("Baltic Avenue", 60, 4),
            # Add more properties as needed
        ]
        self.chance_cards = [
            "Advance to Go (Collect $200)",
            "Bank error in your favor – Collect $75",
            "Doctor's fees – Pay $50",
            "Get Out of Jail Free",
            "Go to Jail – Go directly to Jail – Do not pass Go, do not collect $200",
            "It is your birthday – Collect $10 from each player",
            "Grand Opera Night – Collect $50 from every player for opening night seats",
            "Income Tax refund – Collect $20",
            "Life Insurance Matures – Collect $100",
            "Pay Hospital Fees of $100",
            "Pay School Fees of $150",
            "Receive $25 Consultancy Fee",
            "You have won second prize in a beauty contest – Collect $10",
            "You inherit $100"
        ]
    def get_property(self, position):
        if position < len(self.properties):
            return self.properties[position]
        return None
    def handle_chance(self, player, players):
        card = random.choice(self.chance_cards)
        print(f"Chance Card: {card}")
        if card == "Advance to Go (Collect $200)":
            player.position = 0
            player.money += 200
        elif card == "Bank error in your favor – Collect $75":
            player.money += 75
        elif card == "Doctor's fees – Pay $50":
            player.money -= 50
        elif card == "Get Out of Jail Free":
            player.get_out_of_jail_free = True  # Update player's attribute
        elif card == "Go to Jail – Go directly to Jail – Do not pass Go, do not collect $200":
            if not player.use_get_out_of_jail_free():
                player.position = 10  # Assuming position 10 is Jail
        elif card == "It is your birthday – Collect $10 from each player":
            for p in players:
                if p != player:
                    p.money -= 10
                    player.money += 10
        elif card == "Grand Opera Night – Collect $50 from every player for opening night seats":
            for p in players:
                if p != player:
                    p.money -= 50
                    player.money += 50
        elif card == "Income Tax refund – Collect $20":
            player.money += 20
        elif card == "Life Insurance Matures – Collect $100":
            player.money += 100
        elif card == "Pay Hospital Fees of $100":
            player.money -= 100
        elif card == "Pay School Fees of $150":
            player.money -= 150
        elif card == "Receive $25 Consultancy Fee":
            player.money += 25
        elif card == "You have won second prize in a beauty contest – Collect $10":
            player.money += 10
        elif card == "You inherit $100":
            player.money += 100