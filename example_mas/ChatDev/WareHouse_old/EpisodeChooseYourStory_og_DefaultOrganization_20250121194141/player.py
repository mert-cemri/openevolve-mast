'''
Player module to track player variables such as relationships and items.
'''
class Player:
    def __init__(self):
        self.relationships = {}
        self.items = []
    def update_relationships(self, outcome):
        # Example logic to update relationships based on the outcome
        if 'relationship_change' in outcome:
            for character, change in outcome['relationship_change'].items():
                if character in self.relationships:
                    self.relationships[character] += change
                else:
                    self.relationships[character] = change
    def update_items(self, outcome):
        # Example logic to update items based on the outcome
        if 'items' in outcome:
            for item in outcome['items']:
                if item not in self.items:
                    self.items.append(item)