'''
Property class to represent a property on the board.
'''
class Property:
    def __init__(self, name, cost, rent):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.owner = None
    def buy(self, player):
        if player.money >= self.cost:
            player.money -= self.cost
            self.owner = player
            player.properties.append(self)
            print(f"{player.name} bought {self.name} for ${self.cost}.")
        else:
            print(f"{player.name} cannot afford {self.name}.")
    def charge_rent(self, player):
        if self.owner and self.owner != player:
            player.money -= self.rent
            self.owner.money += self.rent
            print(f"{player.name} paid ${self.rent} rent to {self.owner.name}.")