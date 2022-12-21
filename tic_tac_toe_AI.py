import numpy as np

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

array_win = np.array([[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],

                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6]])
X_win = False
O_win = False

m=0
def check_draw():
    # for i in range(len(board)):
    #     if board[i] == " ":
    #         return False
    # return True


    if len(set(board)) == 1 and  board[0] == " ":
        return False
    return True


def win_rule(board, player,):

    if ((board[0] == player) and (board[0] == board[1]) and (board[1] == board[2]) and (board[0] == board[2])) or \
        ((board[3] == player) and (board[3] == board[4]) and (board[4] == board[5]) and (board[5] == board[3])) or \
        ((board[6] == player) and (board[6] == board[7]) and (board[7] == board[8]) and (board[8] == board[6])) or \
        ((board[0] == player) and (board[0] == board[3]) and (board[3] == board[6]) and (board[6] == board[3])) or \
        ((board[1] == player) and (board[1] == board[4]) and (board[4] == board[7]) and (board[7] == board[1])) or \
        ((board[2] == player) and (board[2] == board[5]) and (board[5] == board[8]) and (board[8] == board[2])) or \
        ((board[0] == player) and (board[0] == board[4]) and (board[4] == board[8]) and (board[8] == board[0])) or \
        ((board[2] == player) and (board[2] == board[4]) and (board[4] == board[6]) and (board[6] == board[2])) :
        return True
    else:
        return False

def com_move():
    best_score = -1
    best_move = 0

    for i in range(len(board)):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            print(i, score)
            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def minimax(board, is_max):
    # o = win_rule(board, "O")
    # x = win_rule(board, "X")

    if win_rule(board, "O"):
        return 1

    elif win_rule(board, "X"):
        return -1

    elif check_draw():
        return 0

    if is_max:
        best_score = -1
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "

                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = 1
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "

                if score < best_score:
                    best_score = score

        return best_score


for i in range(9):
    print_board(board)

    if i %2 == 0:
        move = int(input(">>> "))
        player = "X"

        if board[move -1] == " ":
            board[move - 1] = player

        X_win = win_rule(board, player)
    else:

        player = "O"
        board[com_move()] = player

        O_win = win_rule(board, player)

    if X_win or O_win :
        print_board(board)

        if X_win:
            print("X win")

        if O_win:
            print("O win")

        break






