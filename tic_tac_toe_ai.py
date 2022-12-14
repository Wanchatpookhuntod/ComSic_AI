# 1. The game is played on a grid that's 3 squares by 3 squares.
# 2. You are X, your friend (or the computer in this case) is O.
#     Players take turns putting marks in empty squares.
# 3. The first player to get 3 of her marks in a row
#     (up, down, across, or diagonally) is the winner.
# 4. When all 9 squares are full, the game is over.
#    If no player has 3 marks in a row, the game ends in a tie.

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def print_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

# rule of tic tac toe
rule_OX = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 5],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]

def check_win(board, player): # check win game
    win_row = []
    for i in rule_OX:
        win_row.append([board[j] for j in i])

    for i in win_row:
        if len(set(i)) == 1 and i[0] == player:
            return True
    return False



x_win = False
o_win = False

for i in range(9):
    if i % 2 == 0:
        player = "X"
        move = int(input("Turn X <<< "))
        if board[move - 1] == " ":
            board[move - 1] = player

        x_win = check_win(board, player)

    else:
        player = "O"
        move = int(input("Turn O <<< "))
        if board[move - 1] == " ":
            board[move - 1] = player

        o_win = check_win(board, player)

    print_board(board)

    if x_win == True or o_win == True:
        print_board(board)
        if x_win == True:
            print("X win")

        if o_win == True:
            print("O win")
        break
