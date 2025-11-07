'''
Represents a player in the game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 1500
        self.properties = []
        self.get_out_of_jail_free = False  # New attribute to track the card
    def move(self, steps):
        self.position = (self.position + steps) % 40  # Assuming a board with 40 spaces
    def buy_property(self, property):
        if self.money >= property.price:
            self.money -= property.price
            self.properties.append(property)
            property.buy(self)
    def pay_rent(self, property):
        rent = property.rent
        self.money -= rent
        property.owner.money += rent
    # Add a method to use the Get Out of Jail Free card
    def use_get_out_of_jail_free(self):
        if self.get_out_of_jail_free:
            self.get_out_of_jail_free = False
            return True
        return False