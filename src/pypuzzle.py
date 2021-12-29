import random
import tile.py

while True:
    try :
        size = int(input("What size puzzle (n * n) would you like to solve?"))
    except ValueError:
        print("Invalid input! Enter an integer n>1: ")
    if size <= 1 :
        print("Invalid input! Enter an integer n>1: ")
    else :
        puzzleGame(size)
        break
    
def puzzleGame(num: int) :
    DIM = num
    
    tiles = generate(DIM)
    ansKey = getKey(DIM)

    board, key = [[0 for i in range DIM] for j in range DIM]
    
    update(board, tiles)
    update(key, ansKey)

    print(("Welcome to the " + (DIM * DIM - 1) + " Puzzler! \n\n RULES: \n 1) Move the numbered tiles on the board \n\t until they are in order from 1-" + (DIM * DIM - 1) + ". \n\t It will look like this: ")
    printBoard(key)
    print(" 2) You can only move tiles into an \n\t empty space. You cannot move \n\t diagonally. \n\n 3) Input the number of the tile you \n\t wish to move and press Enter. \n")
    print(" \n Other commands: \n\t help - show these rules again \n")
    printBoard(board)

    runGame(tiles, ansKey, board, key, DIM * DIM - 1)

    celebrate()

def generate(n: int) :
    possib = list()
    for i in range(0, n) :
        for j in range(0, n) :
            coords = [None]*2
            coords[0] = i
            coords [1] = j
            possib.append(coords)

    tiles = list()
    inver = False
    while not inver :
        random.shuffle(possib)
        for i in range (0, n*n):
            tiles.append(Tile(i+1, n, possib[i]))
        inver = chkInversions(tiles, n)

    return tiles