'''
Tracks player-specific data such as relationships and items.
'''
class Player:
    def __init__(self):
        self.relationships = {}
        self.items = []
    def update_relationships(self, choice):
        # Example logic for updating relationships based on choice
        if choice == "accept":
            self.relationships["wolf"] = "friend"
        elif choice == "decline":
            self.relationships["wolf"] = "neutral"
    def update_items(self, choice):
        # Example logic for updating items based on choice
        if choice == "enter":
            self.items.append("mysterious artifact")
        elif choice == "ignore":
            self.items.append("forest map")