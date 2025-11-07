'''
This is a simple tic-tac-toe game for two players. The game allows players to take turns marking spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
'''
def print_board(board):
    '''Prints the current state of the board.'''
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    '''Checks if the current player has won the game.'''
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
def is_draw(board):
    '''Checks if the game is a draw.'''
    return all(cell != ' ' for row in board for cell in row)
def tic_tac_toe():
    '''Main function to run the tic-tac-toe game.'''
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        # Get player input
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2) separated by space: ").split())
            if board[row][col] != ' ':
                print("Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as numbers between 0 and 2.")
            continue
        # Place the player's mark on the board
        board[row][col] = current_player
        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        # Check for a draw
        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'
if __name__ == "__main__":
    tic_tac_toe()