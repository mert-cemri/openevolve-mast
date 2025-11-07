'''
Contains PuzzleData class responsible for providing daily puzzle data.
'''
import datetime
class PuzzleData:
    @staticmethod
    def get_daily_puzzle():
        puzzles = [
            {
                'words': [
                    'Apple', 'Banana', 'Orange', 'Grape',
                    'Dog', 'Cat', 'Rabbit', 'Hamster',
                    'Red', 'Blue', 'Green', 'Yellow',
                    'Car', 'Bike', 'Bus', 'Train'
                ],
                'categories': {
                    'Fruits': {
                        'words': ['Apple', 'Banana', 'Orange', 'Grape'],
                        'difficulty': 'Yellow'
                    },
                    'Pets': {
                        'words': ['Dog', 'Cat', 'Rabbit', 'Hamster'],
                        'difficulty': 'Green'
                    },
                    'Colors': {
                        'words': ['Red', 'Blue', 'Green', 'Yellow'],
                        'difficulty': 'Blue'
                    },
                    'Vehicles': {
                        'words': ['Car', 'Bike', 'Bus', 'Train'],
                        'difficulty': 'Purple'
                    }
                }
            },
            # Additional puzzles can be added here
        ]
        today = datetime.date.today()
        puzzle_index = today.toordinal() % len(puzzles)
        return puzzles[puzzle_index]