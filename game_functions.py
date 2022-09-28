import random, math
from tile import Tile

def runGame(num) :
    # Puzzle will be `num` * `num` dimensions, where `num` is an integer from user input.
    #   `num` is stored in the constant `DIM`.
    DIM = num
    
    # Create two lists of Tile objects; one with randomly shuffled but solvable coordinates,
    #   and the other with the coordinates of a solved DIM * DIM board.
    tiles = None
    solution = None
    # Ensure we don't generate an already solved list of tiles!
    listTiles = list()
    listSoln = list()
    while listTiles == listSoln :
        tiles = genPuzz(DIM, "puzzle")
        solution = genPuzz(DIM, "solvedBoard")

        for tile in tiles : listTiles.append(tile.getNum)
        for tile in solution : listSoln.append(tile.getNum)

    # Initializes 2-D lists used to display board (and solution) with zeros
    board = [[0 for i in range(DIM)] for j in range(DIM)]
    solvedBoard = [[0 for i in range(DIM)] for j in range(DIM)]
    
    # Change values of 2-D lists to contain numbered Tile objects at their respective coordinates
    update(board, tiles)
    update(solvedBoard, solution)

    # Print rules, including what solved state looks like
    printRules(solvedBoard, DIM)

    # Start the game!
    maxTileNum = DIM * DIM - 1
    running = True
    # Loop to take user input and print new game state/relevant message in response, until game is solved
    #   or user quits.
    while running :
        printBoard(board)
        entry = input("Input: ")
        num = None
        try :
            num = int(entry)
        except ValueError :
            if entry == "help" :
                printRules(solvedBoard, DIM)
                continue
            elif entry == "quit" :
                print("Goodbye!")
                running = False
                continue
            else :
                print("Invalid input!")
                continue

        if (num >= 1 and num <= maxTileNum) :
            x = tiles[num-1].x()
            y = tiles[num-1].y()
            oldnum = board[x][y]
            board[x][y] = 0
            # Tile objects contain a `move()` function to determine if they can be moved or not based on
            #   game state. If moveable, the Tile is moved and the function returns True; if not, the
            #   Tile remains in its position and the function returns False.
            if tiles[num - 1].move() :
                update(board, tiles)
                printBoard(board)
            else :
                board[x][y] = oldnum
                print("Cannot move this tile!")
        else : 
            print("No tile found!")
        
        # Check if the game is solved. If yes, end the loop and print a congratulatory message :D
        if solved(tiles, solution, maxTileNum) :
            celebrate()
            running = False

def genPuzz(n, mode) :
    tiles = list()

    # If mode == "puzzle", generate a list of Tile objects with random but solvable coordinates.
    if mode == "puzzle" :
        # Create list of all possible coordinates on board
        possib = list()
        for i in range(0, n) :
            for j in range(0, n) :
                coords = [None]*2
                coords[0] = i
                coords[1] = j
                possib.append(coords)

        inver = False
        while not inver :
            tiles = list()
            # Shuffle list of coordinates
            random.shuffle(possib)
            # We create one less Tile object than n*n to leave an empty space on the board. We initialize
            #   the Tile's coordinates from the shuffled list `possib`.
            for i in range (0, n*n-1):
                t = Tile(i+1, n, possib[i])
                tiles.append(t)
            # The method below returns True if the list of Tile objects generated constitutes a solvable
            #   puzzle. If False, we generate a new list with re-shuffled coordinates until we have a
            #   solvable puzzle.
            inver = solvable(tiles, n)

    # If mode == "solvedBoard", generate a list of Tile objects with coordinates of a solved game state.
    elif mode == "solvedBoard" :
        i = 1
        while i < n*n :
            for x in range(0, n) :
                for y in range(0, n) :
                    coords = [x, y]
                    tiles.append(Tile(i, n, coords))
                    i = i + 1
        # Remove the Tile object where the empty space should be
        tiles.remove(tiles[n*n-1])

    return tiles

# Updates the sublists of 2*2 list `board` with the numbers of Tile objects corresponding to board[x][y]
def update(board, tiles) :
    for tile in tiles :
        x = tile.x()
        y = tile.y()
        board[x][y] = tile.getNum()
        # Each Tile object contains the current game state for functionality of `Tile.move()`
        tile.newGameState(board)

# Prints rules, including what solved game state looks like.
def printRules(solvedBoard, DIM) :
    print("\n RULES: \n 1) Move the numbered tiles on the board \n\t until they are in order from 1-" + str(DIM * DIM - 1) + ". \n\t When solved, it will look like this: ")
    printBoard(solvedBoard)
    print(" 2) You can only move tiles into an \n\t empty space. You cannot move \n\t diagonally. \n\n 3) Input the number of the tile you \n\t wish to move and press Enter. \n")
    print(" \n Other commands you can type: \n\t \"help\" - show these rules again \n\t \"quit\" - exit the game \n")

# Prints 2*2 list `board` in lines of size `len(board)`, with even spacing between items on a line.
def printBoard(board) :
    MAX = len(board)**2

    for i in range(0, len(board)) :
        for j in range(0, len(board)) :
            diff = len(str(MAX)) - len(str(board[i][j]))
            if board[i][j] == 0 :
                print("   " + " " * (diff), end='')
            else :
                print(" " + str(board[i][j]) + " " + " " * (diff), end='')
        print()
    print()

# Check if the current board state `curr` matches the solved board state `ans`. Return True/False appropriately.
def solved(curr, ans, maxTileNum) :
    n = 0
    for i in range(0, maxTileNum) :
        currX = curr[i].x()
        currY = curr[i].y()
        ansX = ans[i].x()
        ansY = ans[i].y()
        if currX != ansX or currY != ansY :
            n = n+1
    return n == 0

# Print a celebratory message from a randomly shuffled list.
#   In the future, we may print fancy ASCII art instead :D
def celebrate() :
    winner = list()
    winner.append("Winner, winner, chicken dinner! (Unless you're vegetarian, we have tofu options)")
    winner.append("Huzzah!")
    winner.append("Hurrah!")
    winner.append("Impressive!")
    winner.append("Felicitations.")
    winner.append("Noice!")

    random.shuffle(winner)
    print(winner[0])

# Returns True if list of Tile objects `tiles` constitutes a solvable puzzle, returns False if not.
def solvable(tiles, n) :
    if (n % 2) != 0 :
        return (inversionCount(tiles) % 2) == 0

    else :
        allSquares = list()
        for i in range(1, n*n + 1) :
            allSquares.append(i)
        
        realSquares = list()
        for tile in tiles :
            num = tile.getSqNum()
            realSquares.append(num)

        emptySqNum = 0
        for r in realSquares :
            x = int(r)
            allSquares.remove(x)
        emptySqNum = allSquares[0]
        
        emptyX = 0
        if emptySqNum <= n :
            emptyX = 1
        else :
            emptyX = (int(emptySqNum/n) + (emptySqNum%n))

        if (n - 1 - emptyX) % 2 == 0 :
            return inversionCount(tiles) % 2 != 0
        else : 
            return inversionCount(tiles) %2 == 0

# Helper function for `chkInversions()` that returns the number of inversions in a list of Tile objects.
#   (See README for more on inversions and n-puzzle solvability conditions.)
def inversionCount(tiles) :
    invs = 0
    for i in range (0, len(tiles)) :
        for j in range(i+1, len(tiles)) :
            tile1sq = tiles[i].getSqNum()
            tile2sq = tiles[j].getSqNum()
            if tile1sq > tile2sq :
                invs = invs + 1
    return invs

def toList(board):
    d1_puzzle = list()
    for row in board:
        for num in row:
            d1_puzzle.append(num)
    return d1_puzzle