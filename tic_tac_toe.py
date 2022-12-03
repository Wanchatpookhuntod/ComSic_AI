import numpy as np

board = np.array([[" ", " ", " "],
                  [" ", " ", " "],
                  [" ", " ", " "]])

position = 0
player = ""

for i in range(9):

    if i%2 == 0:
        position = int(input("X <<< "))
        player = "X"
    else:
        position = int(input("O <<< "))
        player = "O"

    if position == 1:
        board[0, 0] = player
    elif position == 2:
        board[0, 1] = player
    elif position == 3:
        board[0, 2] = player
    elif position == 4:
        board[1, 0] = player
    elif position == 5:
        board[1, 1] = player
    elif position == 6:
        board[1, 2] = player
    elif position == 7:
        board[2, 0] = player
    elif position == 8:
        board[2, 1] = player
    elif position == 9:
        board[2, 2] = player

    print(board)

    if board[0, 0] == player and board[1, 1] == player and board[2, 2] == player \
            or board[0, 2] == player and board[1, 1] == player and board[2, 0] == player \
            or board[0, 0] == player and board[0, 1] == player and board[0, 2] == player \
            or board[1, 0] == player and board[1, 1] == player and board[1, 2] == player \
            or board[2, 0] == player and board[2, 1] == player and board[2, 2] == player \
            or board[0, 0] == player and board[1, 0] == player and board[2, 0] == player \
            or board[0, 1] == player and board[1, 1] == player and board[2, 1] == player \
            or board[0, 2] == player and board[1, 2] == player and board[2, 2] == player:

        print("\n", player, "win")
        break

