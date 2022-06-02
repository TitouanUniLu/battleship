from board import board

def checkIfValid(board, boat_size, x, y, pos):
    if pos == "right":
        for i in range(0,boat_size):
            if board[x][y] != 0:
                return False
            else:
                y+=1
        return True

    elif pos == "left":
        for i in range(0,boat_size):
            if board[x][y] != 0:
                return False
            else:
                y-=1
        return True

    elif pos == "up":
        for i in range(0,boat_size):
            if board[x][y] != 0:
                return False
            else:
                x-=1
        return True

    elif pos == "down":
        for i in range(0,boat_size):
            if board[x][y] != 0:
                return False
            else:
                x+=1
        return True

def place_boats(board, number_boats):
    for boats in range(1, number_boats+1):
        valid_input = False
        while not valid_input:
            print("\n -Boat number: ", boats)
            print("Choose the coordinates of the edge of the boat and if it is going left, right, up or down: (ex: 0 0 right)")
            choice = input()
            choice = choice.split(" ")
            x, y, pos = int(choice[0]), int(choice[1]), choice[2]
            if pos == "right" and y <= 10-boats and checkIfValid(board, boats, x, y, pos):
                valid_input = True
                for i in range(0,boats):
                    board[x][y] = boats
                    y += 1
            elif pos == "left" and y >= boats and checkIfValid(board, boats, x, y, pos):
                valid_input = True
                for i in range(0,boats):
                    board[x][y] = boats
                    y -= 1
            elif pos == "up" and x >= boats and checkIfValid(board, boats, x, y, pos):
                valid_input = True
                for i in range(0,boats):
                    board[x][y] = boats
                    x -= 1
            elif pos == "down" and x <= 10-boats and checkIfValid(board, boats, x, y, pos):
                valid_input = True
                for i in range(0,boats):
                    board[x][y] = boats
                    x += 1
            else:
                print("invalid input :( \n")
        print("Current state of the player's board: ")
        print(board, "\n")
    return(board)

def player(num, boat_num):
    game_board = board()
    print("\nPlayer",num,"'s turn to place their boats:")
    P1_board = place_boats(game_board, boat_num)
    print("Final board state of Player",num,": ")
    print(P1_board)
    return(P1_board)