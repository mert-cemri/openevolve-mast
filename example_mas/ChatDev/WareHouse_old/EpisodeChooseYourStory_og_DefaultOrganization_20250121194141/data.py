'''
Data module to manage game data such as scenes, choices, and outcomes.
'''
class Data:
    @staticmethod
    def load_scene_data():
        # Example scene data
        return {
            "start": {
                "narrative": "You are in a dark forest.",
                "choices": {
                    "1": {"description": "Go north", "next_scene": "north_scene"}
                }
            },
            "north_scene": {
                "narrative": "You find a river.",
                "choices": {
                    "1": {"description": "Swim across", "next_scene": "end_scene"}
                }
            },
            "end_scene": {
                "narrative": "You reached the end.",
                "choices": {}
            }
        }