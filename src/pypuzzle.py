import random, math
from tile import Tile
    
def puzzleGame(num) :
    DIM = num
    
    tiles = generate(DIM)
    ansKey = getKey(DIM)

    board = [[0 for i in range(DIM)] for j in range(DIM)]
    key = [[0 for i in range(DIM)] for j in range(DIM)]
    
    update(board, tiles)
    update(key, ansKey)

    z = str(DIM * DIM - 1)
    print("Welcome to the " + z + " Puzzler! \n\n RULES: \n 1) Move the numbered tiles on the board \n\t until they are in order from 1-" + z + ". \n\t It will look like this: ")
    printBoard(key)
    print(" 2) You can only move tiles into an \n\t empty space. You cannot move \n\t diagonally. \n\n 3) Input the number of the tile you \n\t wish to move and press Enter. \n")
    print(" \n Other commands: \n\t help - show these rules again \n")
    printBoard(board)

    runGame(tiles, ansKey, board, key, DIM * DIM - 1)

    celebrate()

def chkInversions(tiles, n) :
    if (n % 2) != 0 :
        return (inversionCount(tiles) % 2) == 0
    else :
        allSquares = list()
        for i in range(1, n*n + 1) :
            allSquares.append(i)
        
        realSquares = list()
        for tile in tiles :
            num = tile.getSqNum()
            print(num)
            realSquares.append(num)

        emptySqNum = 0
        for r in realSquares :
            x = int(r)
            allSquares.remove(allSquares.index(x))
        emptySqNum = allSquares[0]
        
        emptyX = 0
        if emptySqNum <= n :
            emptyX = 1
        else :
            emptyX = (int(sqNum/n) + (sqNum%n))

        if (n - 1 - emptyX) % 2 == 0 :
            return inversionCount(tiles) % 2 != 0
        else : return inversionCount(tiles) %2 == 0

def generate(n) :
    possib = list()
    for i in range(0, n) :
        for j in range(0, n) :
            coords = [None]*2
            coords[0] = i
            coords[1] = j
            possib.append(coords)

    tiles = list()
    inver = False
    while not inver :
        random.shuffle(possib)
        for i in range (0, n*n):
            tiles.append(Tile(i+1, n, possib[i]))
        inver = chkInversions(tiles, n)

    return tiles

def inversionCount(tiles) :
    invs = 0
    for i in range (0, len(tiles)) :
        for j in range(i+1, len(tiles)) :
            tile1sq = tiles[i].getSqNum()
            tile2sq = tiles[j].getSqNum()
            if tile1sq > tile2sq :
                invs = invs + 1
    return invs

def getKey(n) :
    tiles = list()
    i = 1
    while i < n*n : # why does this always generate n*n tiles, rather than the desired n*n-1, for any comparison of i < 2 to i < n*n?)
        for x in range(0, n) :
            for y in range(0, n) :
                coords = [x, y]
                tiles.append(Tile(i, n, coords))
                i = i + 1

    tiles.remove(tiles[n*n-1])
    return tiles

def update(board, tiles) :
    for tile in tiles :
        x = tile.xZero()
        y = tile.yZero()
        board[x][y] = tile.getNum()
        tile.updateLay(board)

def printBoard(board) :
    for i in range(0, len(board)) :
        for j in range(0, len(board)) :
            if board[i][j] == 0 :
                print("   ")
            else :
                z = str(board[i][j])
                print(" " + z + " ")
        print()
    print()

def runGame(tiles, ansKey, board, key, tileMax) :
    DIM = math.sqrt(tileMax+1)
    soln = False
    while not solved :
        try :
            entry = input("Input: ")
            if (entry >= 1 and entry <= tileMax) :
                x = tiles[entry-1].xZero()
                y = tiles[entry-1].yZero()
                oldVal = board[x][y]
                board[x][y] = 0
                if tiles[entry - 1].move() :
                    update(board, tiles)
                    printBoard(board)
                else :
                    board[x][y] = oldVal
                    print("Cannot move this tile!")
            else : print("No tile found!")
        except TypeError :
            if entry.casefold() == "help".casefold() :
                print("Welcome to the " + (DIM * DIM - 1) + " Puzzler! \n\n RULES: \n 1) Move the numbered tiles on the board \n\t until they are in order from 1-" + (DIM * DIM - 1) + ". \n\t It will look like this: ")
                printBoard(key)
                print(" 2) You can only move tiles into an \n\t empty space. You cannot move \n\t diagonally. \n\n 3) Input the number of the tile you \n\t wish to move and press Enter. \n")
                print(" \n Other commands: \n\t help - show these rules again \n")
                printBoard(board)
            else :
                print("Invalid input!")
        soln = solved(tiles, ansKey, tileMax)

def solved(curr, ans, maxnum) :
    n = 0
    for i in range(0, maxnum) :
        currX = curr[i].xZero()
        currY = curr[i].yZero()
        ansX = ans[i].xZero()
        ansY = ans[i].yZero()
        if currX != ansX or currY != ansY :
            n = n+1
        return n == 0

def celebrate() :
    winner = list()
    winner.append("Winner, winner, chicken dinner! (Unless you're vegetarian, we have tofu options)")
    winner.append("Huzzah!")
    winner.append("Hurrah!")
    winner.append("Impressive!")
    winner.append("Felicitations.")
    winner.append("Noice!")
    random.shuffle(winner)
    return winner[0]

while True:
    try :
        size = int(input("What size puzzle (n * n) would you like to solve? "))
    except ValueError:
        print("Invalid input! Enter an integer n>1: ")
    if size <= 1 :
        print("Invalid input! Enter an integer n>1: ")
    else :
        puzzleGame(size)
        break