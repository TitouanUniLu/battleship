import numpy as np

def board():
    board = np.zeros((10,10))
    return(board)

def printBoard(board):
    board_string = ''
    for line in board:
        for elem in line:
            if elem == 100:
                board_string += "X "
            else:
                board_string += str(int(elem)) + " "
        board_string += "\n"
    return board_string