'''
Board class to manage the game board, properties, and special positions.
'''
from property import Property
from chance import ChanceCard
class Board:
    def __init__(self):
        self.positions = [None] * 20
        self.chance_card = ChanceCard()
        self.setup_board()
    def setup_board(self):
        property_positions = [1, 3, 5, 6, 8, 9, 11, 13, 14, 16, 18, 19]
        prices = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320]
        rents = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
        for pos, price, rent in zip(property_positions, prices, rents):
            self.positions[pos] = Property(f"Property {pos}", price, rent)
        self.positions[7] = "Chance"
        self.positions[17] = "Chance"
        self.positions[10] = "Jail"
        self.positions[15] = "Free Parking"
        self.positions[0] = "Go"
    def handle_position(self, player, players):
        position = self.positions[player.position]
        if isinstance(position, Property):
            if position.owner is None:
                choice = input(f"{position.name} is available for ${position.price}. Buy? (y/n): ")
                if choice.lower() == 'y':
                    player.buy_property(position)
            elif position.owner != player:
                print(f"{position.name} is owned by {position.owner.name}. Rent is ${position.rent}")
                player.pay(position.rent, position.owner)
        elif position == "Chance":
            self.chance_card.draw_card(player)
        elif position == "Jail":
            player.in_jail = True
            print(f"{player.name} landed in Jail!")
        elif position == "Free Parking":
            print(f"{player.name} landed on Free Parking. Nothing happens.")
        elif position == "Go":
            print(f"{player.name} landed on 'Go'. Collect $200!")
            player.money += 200
            print(f"{player.name}'s new balance: ${player.money}")
        else:
            print(f"{player.name} landed on an empty space. Nothing happens.")