'''
This script implements a simple tic-tac-toe game playable in the Linux Terminal.
It allows two players to take turns and determines the winner or if the game is a draw.
'''
def print_board(board):
    '''
    Prints the current state of the board.
    '''
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board):
    '''
    Checks if there is a winner or if the game is a draw.
    Returns 'X', 'O', 'Draw', or None.
    '''
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    # Check for draw
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'
    return None
def get_player_input(player, board):
    '''
    Gets input from the player and updates the board.
    '''
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                raise ValueError
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("This cell is already taken. Choose another one.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
def main():
    '''
    Main function to run the tic-tac-toe game.
    '''
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        get_player_input(current_player, board)
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'Draw':
                print("The game is a draw!")
            else:
                print(f"Player {winner} wins!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
if __name__ == "__main__":
    main()