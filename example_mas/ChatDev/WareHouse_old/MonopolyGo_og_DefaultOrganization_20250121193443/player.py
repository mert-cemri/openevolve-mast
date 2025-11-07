'''
Represents a player in the game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 1500
        self.properties = []
    def move(self, steps, board, chance):
        self.position = (self.position + steps) % len(board.properties)
        property = board.get_property(self.position)
        if property.is_chance:
            event = chance.draw_card()
            event["action"](self, **event.get("kwargs", {}))
        elif property.owner and property.owner != self:
            self.pay_rent(property)
        elif not property.owner:
            self.buy_property(property)
    def buy_property(self, property):
        if self.money >= property.price:
            self.money -= property.price
            self.properties.append(property)
            property.buy(self)
    def pay_rent(self, property):
        rent = property.rent
        if self.money >= rent:
            self.money -= rent
            property.owner.money += rent
        else:
            # Handle the case where the player cannot afford the rent
            print(f"{self.name} cannot afford the rent of ${rent} for {property.name}.")
            # Implement further logic, e.g., declaring bankruptcy or skipping the payment