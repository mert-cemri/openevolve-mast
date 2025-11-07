'''
Player class to represent each player in the game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 1500
        self.properties = []
        self.in_jail = False
    def move(self, steps):
        previous_position = self.position
        self.position = (self.position + steps) % 20
        print(f"{self.name} moved to position {self.position}")
        if self.position < previous_position or self.position == 0:
            self.money += 200
            print(f"{self.name} passed or landed on 'Go' and collected $200! New balance: ${self.money}")
    def pay(self, amount, receiver=None):
        if self.money >= amount:
            self.money -= amount
            if receiver:
                receiver.money += amount
                print(f"{self.name} paid ${amount} to {receiver.name}")
            else:
                print(f"{self.name} paid ${amount}")
        else:
            print(f"{self.name} does not have enough money to pay ${amount}.")
            if receiver:
                receiver.money += self.money
                print(f"{self.name} paid remaining ${self.money} to {receiver.name}")
            self.money = 0
            print(f"{self.name} is bankrupt!")
    def buy_property(self, property):
        if self.money >= property.price:
            self.money -= property.price
            property.owner = self
            self.properties.append(property)
            print(f"{self.name} bought {property.name} for ${property.price}")
        else:
            print(f"{self.name} does not have enough money to buy {property.name}")