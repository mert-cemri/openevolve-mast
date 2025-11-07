'''
Defines the PlayerState class, which tracks the player's state.
'''
class PlayerState:
    def __init__(self):
        self.relationships = {}
        self.items = []
    def update_state(self, choice):
        # Example logic to update relationships or items based on the choice
        if choice == "Talk to the villagers":
            self.relationships["villagers"] = self.relationships.get("villagers", 0) + 1
        elif choice == "Enter the castle":
            self.items.append("castle_key")
        # Additional logic can be added here for other choices
    def get_relationships(self):
        return self.relationships
    def get_items(self):
        return self.items