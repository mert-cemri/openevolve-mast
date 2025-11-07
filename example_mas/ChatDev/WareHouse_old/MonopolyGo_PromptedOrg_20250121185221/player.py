'''
Player class to represent a player in the game.
'''
from property import Property
from chance import Chance
class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
    def move(self, roll, board):
        self.position = (self.position + roll) % len(board.spaces)
        space = board.get_space_info(self.position)
        if isinstance(space, Property):
            if space.owner is None:
                self.buy_property(space)
            elif space.owner != self:
                self.pay_rent(space)
        elif isinstance(space, Chance):
            self.handle_chance(space)
    def buy_property(self, property):
        if self.money >= property.cost:
            self.money -= property.cost
            property.owner = self
            self.properties.append(property)
            print(f"{self.name} bought {property.name} for ${property.cost}.")
        else:
            print(f"{self.name} cannot afford {property.name}.")
        if self.money < 0:
            print(f"{self.name} is bankrupt and out of the game!")
            self.remove_from_game()
    def pay_rent(self, property):
        rent = property.rent
        self.money -= rent
        property.owner.money += rent
        print(f"{self.name} paid ${rent} rent to {property.owner.name}.")
        if self.money < 0:
            print(f"{self.name} is bankrupt and out of the game!")
            self.remove_from_game()
    def handle_chance(self, chance):
        event = chance.draw_card()
        print(f"Chance card: {event}")
        if event == "Advance to Go (Collect $200)":
            self.position = 0  # Assuming 'Go' is at position 0
            self.money += 200
            print(f"{self.name} advances to Go and collects $200.")
    def remove_from_game(self):
        self.properties.clear()  # Optionally, return properties to the bank