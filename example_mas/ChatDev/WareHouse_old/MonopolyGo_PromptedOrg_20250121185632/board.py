'''
Board class to represent the game board.
'''
from property import Property
from chance import Chance
class Board:
    def __init__(self):
        self.spaces = [Property("Mediterranean Avenue", 60, 2),
                       Chance(),
                       Property("Baltic Avenue", 60, 4)]
        # Add more spaces as needed
    def get_space_info(self, position):
        return self.spaces[position]
    def land_on_space(self, player):
        space = self.get_space_info(player.position)
        if isinstance(space, Property):
            if space.owner is None:
                # Automatically decide to buy if the player has enough money
                if player.money >= space.price:
                    player.buy_property(space)
            elif space.owner != player:
                player.pay_rent(space)
        elif isinstance(space, Chance):
            space.draw_card(player)