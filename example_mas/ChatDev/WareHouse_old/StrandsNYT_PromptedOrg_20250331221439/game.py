'''
Game class manages the overall game logic, including puzzle initialization, user interaction, word validation, hint management, and puzzle completion.
'''
from puzzle_board import PuzzleBoard
import random
class Game:
    def __init__(self, width=8, height=6):
        self.board = PuzzleBoard(width, height)
        self.theme_words = ["PYTHON", "JAVA", "RUBY", "SWIFT"]
        self.spangram = "JAVASCRIPT"
        self.non_theme_words_found = set()
        self.hints_unlocked = 0
        self.highlight_words = []
        self.found_theme_words = set()
        self.initialize_board()
    def initialize_board(self):
        all_words = self.theme_words + [self.spangram]
        random.shuffle(all_words)
        placed_positions = set()
        for word in all_words:
            placed = False
            attempts = 0
            while not placed and attempts < 100:
                attempts += 1
                positions = self.generate_random_positions(len(word))
                if positions and all(pos not in placed_positions for pos in positions):
                    if word == self.spangram and not self.board.is_spangram_valid(positions):
                        continue
                    self.board.place_word(word, positions)
                    placed_positions.update(positions)
                    color = 'yellow' if word == self.spangram else 'blue'
                    self.highlight_words.append((word, positions, color))
                    placed = True
        # Fill remaining empty spaces with random letters
        for y in range(self.board.height):
            for x in range(self.board.width):
                if self.board.board[y][x] == '':
                    self.board.board[y][x] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    def generate_random_positions(self, length):
        for _ in range(100):
            path = []
            x, y = random.randint(0, self.board.width - 1), random.randint(0, self.board.height - 1)
            path.append((x, y))
            while len(path) < length:
                adjacents = self.board.get_adjacent_positions(path[-1])
                adjacents = [pos for pos in adjacents if pos not in path]
                if not adjacents:
                    break
                path.append(random.choice(adjacents))
            if len(path) == length:
                return path
        return None
    def validate_user_word(self, word, positions):
        if not self.board.is_valid_word(word, positions):
            return False, "Invalid word or path."
        for theme_word, theme_positions, _ in self.highlight_words:
            if word == theme_word and set(positions) == set(theme_positions):
                if word not in self.found_theme_words:
                    self.found_theme_words.add(word)
                    return True, "Theme word found!"
                else:
                    return False, "Theme word already found."
        if word not in self.non_theme_words_found:
            self.non_theme_words_found.add(word)
            if len(self.non_theme_words_found) % 3 == 0:
                self.hints_unlocked += 1
                return True, "Non-theme word found! Hint unlocked!"
            return True, "Non-theme word found!"
        return False, "Word already found."
    def display(self):
        self.board.display_board(self.highlight_words, self.found_theme_words)
    def is_completed(self):
        required_words = set(self.theme_words + [self.spangram])
        return required_words == self.found_theme_words