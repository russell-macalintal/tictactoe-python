# FUNCTION FOR DISPLAY BOARD STATE
def display_board(board):
    print(f"| {board[0]} | {board[1]} | {board[2]} |       | 1 | 2 | 3 |")
    print("-------------       -------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |       | 4 | 5 | 6 |")
    print("-------------       -------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |       | 7 | 8 | 9 |")


def player_input(player):
    # INITIAL INPUT VARIABLE FOR WHILE LOOP CONDITIONAL
    i = "START"
    acc_range = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if player == "X":
        print("Player 1's (X) Turn")
    elif player == "O":
        print("Player 2's (O) Turn")

    while i.isdigit() == False or i not in acc_range:
        i = input("Select location [1-9]: ")

    return int(i)


def update_board(board, player_input):



# FUNCTION TO INITILIAZE AND PLAY GAME
def play_game():
    # DEFINE EIGHT POSSIBLE WINNING CONDITIONS
    win_list = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    # DEFINE INITIAL BOARD WITH BLANK SPACES AND SET FIRST PLAYER AS 'X'
    game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    empty_space = " "
    pl = "X"

    # SET WHILE LOOP TO KEEP PLAYING WHILE THERE'S AN EMPTY SPACE ON THE BOARD OR UNTIL A WINNING CONDITION IS MET
    while empty_space in game_board:
        display_board(game_board)
        player_input(pl)



# START GAME
play_game()