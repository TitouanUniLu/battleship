from board import board

def game(player1_board, player2_board, max_hit):
    temp_board1 = board()
    temp_board2 = board()

    maxhit1 = 0
    maxhit2 = 0

    win = False
    turn = 1
    while not win:
        if turn == 1:
            print("Player 1's turn to guess coordinates: ")
            print("Enemy board: ")
            print(temp_board2, "\n")
            guess = input()
            guess = guess.split(" ")
            x, y = int(guess[0]), int(guess[1])
            if player2_board[x][y] != 0:
                maxhit1 += 1
                if maxhit1 == max_hit:
                    print(" -- PLAYER 1 WON THE GAME --")
                    print("all ships were sunk:\n ",player2_board)
                    return(" -- THANKS FOR PLAYING -- ")
                print(" HIT! you get to play again!")
                temp_board2[x][y] = player2_board[x][y]
                print(" Current state of enemy board: ")
                print(temp_board2)
            else:
                print("You missed ...\n")
                turn += 1
        else:
            print("Player 2's turn to guess coordinates: ")
            print("Enemy board: ")
            print(temp_board1,"\n")
            guess = input()
            guess = guess.split(" ")
            x, y = int(guess[0]), int(guess[1])
            if player1_board[x][y] != 0:
                maxhit2 += 1
                if maxhit2 == max_hit:
                    print(" -- PLAYER 2 WON THE GAME --")
                    print("all ships were sunk:\n ",player1_board)
                    return(" -- THANKS FOR PLAYING -- ")
                print(" HIT! you get to play again!")
                temp_board1[x][y] = player1_board[x][y]
                print(" Current state of enemy board: ")
                print(temp_board1)
            else:
                print("You missed ... \n")
                turn -= 1