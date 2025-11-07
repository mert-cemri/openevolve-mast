'''
Defines the story structure, narrative segments, and branching choices.
'''
import copy
class StoryNode:
    '''
    Represents a single narrative segment with text, choices, and conditional logic.
    '''
    def __init__(self, node_id, text, choices=None, conditions=None, effects=None):
        self.node_id = node_id
        self.text = text
        self.choices = choices if choices else []
        self.conditions = conditions if conditions else {}
        self.effects = effects if effects else {}
    def is_end_node(self):
        return len(self.choices) == 0
class Story:
    '''
    Manages the entire story structure and navigation.
    '''
    def __init__(self, player):
        self.player = player
        self.nodes = {}
        self.start_node_id = None
    def load_story(self):
        '''
        Loads the story nodes into memory.
        '''
        self.start_node_id = 'start'
        self.nodes['start'] = StoryNode(
            'start',
            "You wake up in a mysterious forest. What do you do?",
            choices=[
                {'text': "Explore the forest", 'next_node': 'explore'},
                {'text': "Stay put and wait", 'next_node': 'wait'}
            ]
        )
        self.nodes['explore'] = StoryNode(
            'explore',
            "You find a strange artifact. Do you pick it up?",
            choices=[
                {'text': "Yes, take the artifact", 'next_node': 'artifact_taken', 'effects': {'items': ['artifact']}},
                {'text': "No, leave it", 'next_node': 'artifact_left'}
            ]
        )
        self.nodes['wait'] = StoryNode(
            'wait',
            "You wait patiently. A stranger approaches. Do you talk to them?",
            choices=[
                {'text': "Yes, talk to the stranger", 'next_node': 'talk_stranger', 'effects': {'relationships': {'stranger': 'friendly'}}},
                {'text': "No, hide from the stranger", 'next_node': 'hide_stranger'}
            ]
        )
        self.nodes['artifact_taken'] = StoryNode(
            'artifact_taken',
            "The artifact glows warmly in your hand. You feel powerful.",
            choices=[
                {'text': "Continue deeper into the forest", 'next_node': 'deep_forest'}
            ]
        )
        self.nodes['artifact_left'] = StoryNode(
            'artifact_left',
            "You leave the artifact behind and continue cautiously.",
            choices=[
                {'text': "Continue deeper into the forest", 'next_node': 'deep_forest'}
            ]
        )
        self.nodes['talk_stranger'] = StoryNode(
            'talk_stranger',
            "The stranger becomes your ally and guides you out safely. You survive!",
            choices=[]
        )
        self.nodes['hide_stranger'] = StoryNode(
            'hide_stranger',
            "The stranger passes by. You're alone and lost. Eventually, you succumb to the forest.",
            choices=[]
        )
        self.nodes['deep_forest'] = StoryNode(
            'deep_forest',
            "You encounter a wild beast!",
            choices=[
                {'text': "Fight the beast", 'next_node': 'fight_beast', 'conditions': {'items': ['artifact']}},
                {'text': "Run away", 'next_node': 'run_away'}
            ]
        )
        self.nodes['fight_beast'] = StoryNode(
            'fight_beast',
            "Using the artifact, you defeat the beast and become a hero!",
            choices=[]
        )
        self.nodes['run_away'] = StoryNode(
            'run_away',
            "You escape safely but live forever wondering what could have been.",
            choices=[]
        )
    def get_start_node(self):
        return self.nodes.get(self.start_node_id)
    def get_next_node(self, choice):
        # Apply effects if any
        effects = choice.get('effects', {})
        for item in effects.get('items', []):
            self.player.add_item(item)
        for relation, status in effects.get('relationships', {}).items():
            self.player.set_relationship(relation, status)
        next_node_id = choice['next_node']
        original_next_node = self.nodes.get(next_node_id)
        # Create a deep copy to avoid modifying original node
        next_node = copy.deepcopy(original_next_node)
        # Check conditions for choices in the next node without modifying original choices
        if next_node and next_node.choices:
            valid_choices = []
            for ch in next_node.choices:
                conditions = ch.get('conditions', {})
                if self.player.check_conditions(conditions):
                    valid_choices.append(ch)
            if not valid_choices:
                # Provide a fallback ending if no valid choices remain
                next_node.text += "\n\nYou find yourself unable to proceed further due to your previous choices."
                next_node.choices = []
            else:
                next_node.choices = valid_choices
        return next_node