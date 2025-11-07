'''
Represents the game board and properties.
'''
class Property:
    def __init__(self, name, price, rent, is_chance=False):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None
        self.is_chance = is_chance
    def buy(self, player):
        self.owner = player
    def charge_rent(self, player):
        player.pay_rent(self)
class Board:
    def __init__(self):
        self.properties = [
            Property("Mediterranean Avenue", 60, 2),
            Property("Chance", 0, 0, is_chance=True),
            Property("Baltic Avenue", 60, 4),
            # Add more properties and chance spaces as needed
        ]
    def get_property(self, position):
        return self.properties[position]