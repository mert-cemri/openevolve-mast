'''
Defines the Player class to manage player state, including items and relationships.
'''
class Player:
    '''
    Manages player's inventory and relationships.
    '''
    def __init__(self):
        self.items = set()
        self.relationships = {}
    def add_item(self, item):
        '''
        Adds an item to the player's inventory.
        '''
        self.items.add(item)
    def set_relationship(self, character, status):
        '''
        Sets the relationship status with a character.
        '''
        self.relationships[character] = status
    def check_conditions(self, conditions):
        '''
        Checks if the player meets the specified conditions.
        '''
        required_items = conditions.get('items', [])
        for item in required_items:
            if item not in self.items:
                return False
        required_relationships = conditions.get('relationships', {})
        for character, status in required_relationships.items():
            if self.relationships.get(character) != status:
                return False
        return True