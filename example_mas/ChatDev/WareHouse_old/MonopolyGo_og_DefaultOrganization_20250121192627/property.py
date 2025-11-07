'''
Represents a property on the board.
'''
class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None
    def buy(self, player):
        self.owner = player
    def charge_rent(self, player):
        if self.owner and self.owner != player:
            player.pay_rent(self)