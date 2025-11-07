'''
Property class to represent a property on the board.
'''
class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None
    def buy(self, player):
        player.buy_property(self)
    def charge_rent(self, player):
        player.pay_rent(self)