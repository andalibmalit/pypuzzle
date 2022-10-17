import random
from solver import a_star
def rungame(size):
    puzzle, soln = puzzleGen(size)
    printrules(soln, size)
    while puzzle != soln:
        printpuzzle(puzzle, size)
        entry = input("Input: ")
        input_move = None
        try:
            input_move = int(entry)
        except ValueError:
            if entry == "help":
                printrules(soln, size)
                continue
            elif entry == "quit":
                print("Goodbye!")
                break
            elif entry == "solve":
                solvable, steps = a_star(puzzle, soln, size)
                if solvable:
                    print("Solved in", len(steps) - 1, "steps!")
                    print(getsoln(steps))
                else:
                    print("Error: puzzle state not solvable!\n")
                continue
            else:
                print("Invalid input!")
                continue
        moves = possible_moves(puzzle, size)
        if input_move in moves.keys():
            puzzle = moves[input_move]
        else:
            print("Cannot move this tile!")
        if puzzle == soln:
            printpuzzle(puzzle, size)
            celebrate()


def puzzleGen(size):
    puzzle = [0 for i in range(size**2)]
    soln = [0 for i in range(size**2)]
    for i in range(size**2 - 1):
        puzzle[i] = i + 1
        soln[i] = i + 1
    while puzzle == soln or not inversions(puzzle, size):
        random.shuffle(puzzle)
    return tuple(puzzle), tuple(soln)


def inversions(puzzle, size): 
    invs = 0
    for i in range(len(puzzle) - 1):
        for j in range(i+1, len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                invs += 1
    z = puzzle.index(0)
    z_row = z//size + z%size
    if size % 2 != 0:
        return invs % 2 == 0
    else:
        if (size - z_row - 1) % 2 == 0:
            return invs % 2 == 0
        else:
            return not (invs % 2 == 0)
    
        
def swap_tiles(puzzle, i, j):
    new_state = list(puzzle)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return tuple(new_state)


def possible_moves(puzzle, size):
    moves = {}
    i = puzzle.index(0)
    if i - size >= 0:
        moves[puzzle[i - size]] = swap_tiles(puzzle, i, i - size)
    if i + size < len(puzzle):
        moves[puzzle[i + size]] = swap_tiles(puzzle, i, i + size)
    if i % size > 0:
        moves[puzzle[i - 1]] = swap_tiles(puzzle, i, i - 1)
    if i % size + 1 < size:
        moves[puzzle[i + 1]] = swap_tiles(puzzle, i, i + 1)
    return moves


def printrules(soln, size):
    print("\nRULES: \n 1) Move the numbered tiles on the puzzle until they are in order from 1-" + str(size**2 - 1) + "\n\t (with the empty '_' tile at the beginning). When solved, it will \n\t look like this: \n")
    printpuzzle(soln, size)
    print(" 2) You can only move tiles into an empty space. You cannot move diagonally. \n\n 3) Input the number of the tile you wish to move and press Enter. \n")
    print(" \nOther commands you can type: \n\t \"help\" - show these rules again \n\t \"solve\" - print the solution \n\t \"quit\" - exit the game \n")


def printpuzzle(puzzle, size):
    temp_puzzle = list(puzzle)
    for i in range(len(temp_puzzle)):
        if temp_puzzle[i] == 0:
            temp_puzzle[i] = "_"
    for i in range(len(temp_puzzle)):
        # Compares character length of "tile" number to maximum length, to format printing
        diff = len(str(size**2)) - len(str(temp_puzzle[i]))
        print(temp_puzzle[i], " ", end=((' ') * diff))
        if (i + 1) % size == 0:
            print()
    print()


def celebrate():
    winner = []
    winner.append("Winner, winner, chicken dinner! (Unless you're vegetarian, we have tofu options)")
    winner.append("Huzzah!")
    winner.append("Hurrah!")
    winner.append("Impressive!")
    winner.append("Felicitations.")
    winner.append("Noice!")
    random.shuffle(winner)
    print(winner[0])
    

def getsoln(steps):
    tiles = []
    for i in range(1, len(steps)):
        tiles.append(steps[i-1][steps[i].index(0)])
    return tiles