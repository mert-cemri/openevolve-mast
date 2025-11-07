'''
Main executable file for the puzzle game. Handles user interaction and game loop with color-coded feedback.
'''
from puzzle_game import PuzzleGame
from colorama import init, Fore, Style
def main():
    init()
    game = PuzzleGame()
    game.generate_daily_puzzle()
    color_map = {
        'Yellow': Fore.YELLOW,
        'Green': Fore.GREEN,
        'Blue': Fore.BLUE,
        'Purple': Fore.MAGENTA
    }
    while not game.is_game_over():
        game.display_grid()
        print(f"Mistakes: {game.mistakes}/4")
        user_input = input("Select 4 words separated by commas (or type 'shuffle' to shuffle): ").strip()
        if user_input.lower() == 'shuffle':
            game.shuffle_words()
            continue
        selected_words = [word.strip() for word in user_input.split(',')]
        if len(selected_words) != 4:
            print(f"{Fore.RED}Please select exactly 4 words.{Style.RESET_ALL}")
            continue
        correct, message, difficulty = game.select_group(selected_words)
        if correct:
            color = color_map.get(difficulty, Fore.WHITE)
            print(f"{color}Correct! Category: {message} (Difficulty: {difficulty}){Style.RESET_ALL}")
        elif message is not None:
            print(f"{Fore.RED}{message}{Style.RESET_ALL}")  # Display the error message returned
        else:
            print(f"{Fore.RED}Incorrect guess. Try again.{Style.RESET_ALL}")
    if game.mistakes >= 4:
        print(f"{Fore.RED}Game Over! You've reached the maximum number of mistakes.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}Congratulations! You've solved the puzzle.{Style.RESET_ALL}")
if __name__ == "__main__":
    main()