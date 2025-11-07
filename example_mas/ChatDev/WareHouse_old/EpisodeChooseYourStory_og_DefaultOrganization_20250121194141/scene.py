'''
Scene module to represent and manage narrative segments.
'''
from data import Data
class Scene:
    def __init__(self, scene_id, narrative, choices):
        self.scene_id = scene_id
        self.narrative = narrative
        self.choices = choices
    @staticmethod
    def load_scene(scene_id):
        scene_data = Data.load_scene_data()
        if scene_id in scene_data:
            data = scene_data[scene_id]
            choices = {cid: Choice(desc["description"], desc["next_scene"]) for cid, desc in data["choices"].items()}
            return Scene(scene_id, data["narrative"], choices)
        return None
    def get_choices(self):
        return self.choices
class Choice:
    def __init__(self, description, next_scene):
        self.description = description
        self.next_scene = next_scene