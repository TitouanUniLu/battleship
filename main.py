from player import player
from game import game

def main():
    print(" -- WELCOME TO BATTLESHIP BUT WORST THAN THE NORMAL GAME --")
    print(" How many boats per person? each new boat size is increased by one and starts at 1")
    boat_num = int(input())
    max_hit = boat_num*(boat_num+1)/2
    p1b = player(1, boat_num)
    p2b = player(2, boat_num)
    print(" -- TIME TO GAME -- \n")
    print(game(p1b, p2b, max_hit))
    
    

if __name__ == "__main__":
    main()