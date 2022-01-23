# FUNCTION FOR DISPLAY BOARD STATE
def display_board(board):
    print(f"| {board[0]} | {board[1]} | {board[2]} |       | 1 | 2 | 3 |")
    print("-------------       -------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |       | 4 | 5 | 6 |")
    print("-------------       -------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |       | 7 | 8 | 9 |")

def player_input(player):
    if player == "X":
        print("Player 1's (X) Turn")
    elif player == "O":
        print("Player 2's (O) Turn")

    i = input("Enter ")


# FUNCTION TO INITILIAZE AND PLAY GAME
def play_game():
    # DEFINE INITIAL BOARD WITH BLANK SPACES AND SET PLAYER 1 AS 'X' AND PLAYER 2 AS 'O'
    game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    pl_1 = "X"
    pl_2 = "O"

    display_board(game_board)

# START GAME
play_game()