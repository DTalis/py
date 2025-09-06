def create_board():
    """Initializes and returns a 3x3 Tic-Tac-Toe board represented as a 2D list."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    """
    Prints the current state of the game board.
    The rows and columns are labeled from 1 to 3 for user convenience.
    Note: The screen is no longer cleared between turns.
    """
    # Print column headers (1, 2, 3)
    print("\n  1   2   3")
    print("  ---------")
    
    # Iterate through the board to print rows and their numbers
    for i, row in enumerate(board):
        # Print the row number (i+1) and the content of the row
        print(f"{i+1}|{' | '.join(row)}|")
        if i < 2:
            print("  ---------")
    print()

def player_input(player, board):
    """
    Prompts the current player for their move (row, col) and validates the input.
    The function handles invalid input and ensures the chosen cell is empty.
    Returns the 0-based indices (row, col) for the board.
    """
    while True:
        try:
            move_str = input(f"Player '{player}', enter your move (row, col) from 1 to 3: ")
            row, col = map(int, move_str.split(','))
            
            # Convert user's 1-based input to 0-based indices for the board list
            row -= 1
            col -= 1

            # Validate that the move is within bounds and the cell is empty
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please choose an empty cell within the 1-3 range.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter your move in the format 'row,col'.")

def check_win(board, player):
    """
    Checks all possible winning combinations (rows, columns, diagonals)
    for the current player.
    Returns True if the player has won, otherwise returns False.
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    """
    Checks if the game has resulted in a tie.
    Returns True if all cells are filled, otherwise returns False.
    """
    # Check if there are any empty spaces left on the board
    return all(cell != ' ' for row in board for cell in row)

def play():
    """
    Manages the main game flow, including initialization,
    player turns, and checking for win or tie conditions.
    """
    board = create_board()
    current_player = 'X'
    game_over = False
    
    # The main game loop continues until a winner or a tie is found
    while not game_over:
        display_board(board)
        
        # Get the current player's move
        row, col = player_input(current_player, board)
        
        # Update the board with the player's symbol
        board[row][col] = current_player
        
        # Check if the current player has won
        if check_win(board, current_player):
            display_board(board)
            print(f"Player '{current_player}' wins! Congratulations! 🎉")
            game_over = True
        # Check if the game is a tie
        elif check_tie(board):
            display_board(board)
            print("It's a tie! 🤝")
            game_over = True
        else:
            # Switch to the next player
            current_player = 'O' if current_player == 'X' else 'X'

# This block ensures the play() function runs when the script is executed
if __name__ == "__main__":
    play()
