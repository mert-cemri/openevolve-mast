'''
Represents the game board, including properties and chance spaces.
'''
from property import Property
from chance import Chance
class Board:
    def __init__(self):
        self.spaces = [
            Property("Mediterranean Avenue", 60, 2),
            Chance(),
            Property("Baltic Avenue", 60, 4),
            # Add more spaces as needed
        ]
        self.size = len(self.spaces)
    def get_space_info(self, position):
        return self.spaces[position]
    def land_on_space(self, player):
        space = self.get_space_info(player.position)
        if isinstance(space, Property):
            if space.owner is None:
                player.buy_property(space)
            elif space.owner != player:
                player.pay_rent(space)
            else:
                print(f"{player.name} landed on their own property {space.name}.")
        elif isinstance(space, Chance):
            player.handle_chance(space)