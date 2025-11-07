'''
Player class to represent a player in the game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
    def move(self, roll, board):
        self.position = (self.position + roll) % len(board.spaces)
        board.land_on_space(self)
    def buy_property(self, property):
        if self.money >= property.price:
            self.money -= property.price
            self.properties.append(property)
            property.owner = self
            print(f"{self.name} bought {property.name} for ${property.price}")
    def pay_rent(self, property):
        rent = property.rent
        self.money -= rent
        property.owner.money += rent
        print(f"{self.name} paid ${rent} rent to {property.owner.name}")
    def handle_chance(self, chance_card):
        # Implement chance card effects
        print(f"{self.name} drew a chance card.")
        # Example effect: player.money += 50
        # This is a placeholder for actual chance card effects
        self.money += 50
        print(f"{self.name} received $50 from chance card.")