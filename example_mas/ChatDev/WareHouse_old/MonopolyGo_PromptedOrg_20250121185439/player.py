'''
Represents a player in the game, tracking their money and properties.
'''
import random
class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        print(f"{self.name} rolled a {dice_roll}.")
        return dice_roll
    def move(self, board, dice_roll):
        self.position = (self.position + dice_roll) % board.size
        board.land_on_space(self)
    def buy_property(self, property):
        if self.money >= property.price:
            self.money -= property.price
            self.properties.append(property)
            property.owner = self
            print(f"{self.name} bought {property.name} for ${property.price}.")
        else:
            print(f"{self.name} cannot afford {property.name}.")
    def pay_rent(self, property):
        rent = property.rent
        self.money -= rent
        property.owner.money += rent
        print(f"{self.name} paid ${rent} in rent to {property.owner.name}.")
    def handle_chance(self, chance):
        card = chance.draw_card()
        print(f"{self.name} drew a chance card: {card}.")
        if card == "Advance to Go (Collect $200)":
            self.position = 0  # Assuming 'Go' is at position 0
            self.money += 200
            print(f"{self.name} advances to Go and collects $200.")
        elif card == "Bank error in your favor. Collect $75":
            self.money += 75
            print(f"{self.name} collects $75 from a bank error.")
        elif card == "Doctor's fees. Pay $50":
            self.money -= 50
            print(f"{self.name} pays $50 in doctor's fees.")
        # Add more cases for other chance cards as needed