'''
Defines the Grid class for managing the 6x8 letter grid.
'''
import random
class Grid:
    def __init__(self):
        self.grid = [['' for _ in range(8)] for _ in range(6)]
        self.highlighted = set()
    def place_spangram(self, spangram):
        # Ensure the spangram touches two opposite sides
        placed = False
        attempts = 0
        while not placed and attempts < 100:
            attempts += 1
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                start_row = random.choice([0, 5])
                start_col = 0
                if self.can_place_word(spangram, start_row, start_col, direction):
                    self.insert_word(spangram, start_row, start_col, direction)
                    self.highlight(spangram)
                    placed = True
            elif direction == 'vertical':
                start_row = 0
                start_col = random.choice([0, 7])
                if self.can_place_word(spangram, start_row, start_col, direction):
                    self.insert_word(spangram, start_row, start_col, direction)
                    self.highlight(spangram)
                    placed = True
    def place_word(self, word, highlight=None):
        # Attempt to place the word on the grid
        placed = False
        attempts = 0
        while not placed and attempts < 100:
            attempts += 1
            start_row = random.randint(0, 5)
            start_col = random.randint(0, 7)
            direction = random.choice(['horizontal', 'vertical', 'diagonal'])
            if self.can_place_word(word, start_row, start_col, direction):
                self.insert_word(word, start_row, start_col, direction)
                if highlight:
                    self.highlight(word)
                placed = True
    def can_place_word(self, word, start_row, start_col, direction):
        # Check if the word can be placed at the given position and direction
        if direction == 'horizontal':
            if start_col + len(word) > 8:
                return False
            for i in range(len(word)):
                if self.grid[start_row][start_col + i] not in ('', word[i]):
                    return False
        elif direction == 'vertical':
            if start_row + len(word) > 6:
                return False
            for i in range(len(word)):
                if self.grid[start_row + i][start_col] not in ('', word[i]):
                    return False
        elif direction == 'diagonal':
            if start_row + len(word) > 6 or start_col + len(word) > 8:
                return False
            for i in range(len(word)):
                if self.grid[start_row + i][start_col + i] not in ('', word[i]):
                    return False
        return True
    def insert_word(self, word, start_row, start_col, direction):
        # Insert the word into the grid at the specified position and direction
        if direction == 'horizontal':
            for i in range(len(word)):
                self.grid[start_row][start_col + i] = word[i]
        elif direction == 'vertical':
            for i in range(len(word)):
                self.grid[start_row + i][start_col] = word[i]
        elif direction == 'diagonal':
            for i in range(len(word)):
                self.grid[start_row + i][start_col + i] = word[i]
    def highlight(self, word):
        # Highlight the word on the grid
        self.highlighted.add(word)
    def can_form_word(self, word):
        # Check if the word can be formed on the grid
        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r >= 6 or c < 0 or c >= 8 or self.grid[r][c] != word[index]:
                return False
            temp, self.grid[r][c] = self.grid[r][c], None  # Mark as visited
            # Explore all 8 possible directions
            found = any(dfs(r + dr, c + dc, index + 1) for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
            self.grid[r][c] = temp  # Unmark
            return found
        for row in range(6):
            for col in range(8):
                if dfs(row, col, 0):
                    return True
        return False
    def is_word_highlighted(self, word):
        return word in self.highlighted
    def display(self):
        # Display the grid
        for row in self.grid:
            print(' '.join(letter if letter else '.' for letter in row))