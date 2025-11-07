'''
Main executable entry point for the Strands puzzle game.
'''
from game import Game
def main():
    game = Game()
    print("Welcome to the NYT Strands Puzzle!")
    while not game.is_completed():
        game.display()
        user_input = input("Enter a word and positions (e.g., WORD x1,y1 x2,y2 ...): ").strip().upper()
        try:
            parts = user_input.split()
            word = parts[0]
            positions = [tuple(map(int, pos.split(','))) for pos in parts[1:]]
            valid, message = game.validate_user_word(word, positions)
            print(message)
            if game.hints_unlocked:
                print(f"You have {game.hints_unlocked} hint(s) available!")
        except Exception as e:
            print(f"Invalid input format: {e}")
    print("Congratulations! You have completed the puzzle!")
    game.display()
if __name__ == "__main__":
    main()