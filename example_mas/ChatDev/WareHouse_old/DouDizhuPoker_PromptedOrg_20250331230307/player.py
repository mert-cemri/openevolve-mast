'''
Player class representing each player in the game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.is_landlord = False
    def receive_card(self, card):
        self.hand.append(card)
        self.hand.sort(key=lambda c: c.value())
    def show_hand(self):
        return ' '.join(str(card) for card in self.hand)
    def bid(self):
        print(f"{self.name}'s hand: {self.show_hand()}")
        bid = input(f"{self.name}, do you want to bid as landlord? (y/n): ")
        return bid.lower() == 'y'
    def play_cards(self):
        print(f"{self.name}'s hand: {self.show_hand()}")
        cards_input = input(f"{self.name}, enter cards to play separated by spaces (or 'pass'): ")
        if cards_input.lower() == 'pass':
            return []
        selected_cards = []
        input_cards = cards_input.split()
        temp_hand = self.hand.copy()
        for card_str in input_cards:
            for card in temp_hand:
                if str(card) == card_str:
                    selected_cards.append(card)
                    temp_hand.remove(card)
                    break
            else:
                print(f"Card {card_str} not found in hand.")
                return self.play_cards()
        for card in selected_cards:
            self.hand.remove(card)
        return selected_cards