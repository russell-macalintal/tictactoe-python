import os

clear = lambda: os.system('clear')

# FUNCTION FOR DISPLAY BOARD STATE
def display_board(board):
    print(f"| {board[6]} | {board[7]} | {board[8]} |       | 7 | 8 | 9 |")
    print("-------------       -------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |       | 4 | 5 | 6 |")
    print("-------------       -------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |       | 1 | 2 | 3 |")


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
        if i.isdigit() and i in acc_range:
            return int(i)
        else:
            print("Invalid Input: Try Again")


def empty_tile(board, tile):
    if board[tile-1] == " ":
        return True
    else:
        return False


def update_board(board, tile, pl):
    board[tile-1] = pl


# FUNCTION TO CHECK IF 'X' OR 'O' HAS WON AFTER EVERY TURN
def check_winner(board, win_list):
    for combo in win_list:
        if board[combo[0]] != " " and board[combo[0]] == board[combo[1]] and board[combo[0]] == board[combo[2]]:
            return True

    return False


# FUNCTION TO INITILIAZE AND PLAY GAME
def play_game():
    # DEFINE EIGHT POSSIBLE WINNING CONDITIONS
    win_list = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    # DEFINE INITIAL BOARD WITH BLANK SPACES AND SET FIRST PLAYER AS 'X'
    game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    empty_space = " "
    players = ["X", "O"]
    pl = players[0]
    winner = False

    # SET WHILE LOOP TO KEEP PLAYING WHILE THERE'S AN EMPTY SPACE ON THE BOARD OR UNTIL A WINNING CONDITION IS MET
    while empty_space in game_board and winner == False:
        display_board(game_board)
        tile = player_input(pl)
        clear()
        # CHECK IF BOARD CONTAINS EMPTY SPACE - IF TRUE, UPDATE BOARD AND SWITCH PLAYER, OTHERWISE REDO PLAYER INPUT
        if empty_tile(game_board, tile):
            update_board(game_board, tile, pl)
            if check_winner(game_board, win_list):
                winner = pl
                display_board(game_board)
                print(f"GAME OVER: {winner} HAS WON!")
                break
            else:
                if pl == players[0]:
                    pl = players[1]
                elif pl == players[1]:
                    pl = players[0]
        else:
            print("Tile is already taken. Try Again.")
   
    display_board(game_board)
    print("GAME OVER: TIE")

# START GAME
play_game()