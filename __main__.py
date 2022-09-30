from game_functions import *

print('''Welcome to n-puzzle! The number of tiles in the puzzle is n = (k * k - 1).
      The more tiles, the harder the puzzle.''')
print()

while True:
    try :
        size = int(input("What size puzzle would you like to solve? Enter an integer k > 1: "))
    except ValueError:
        print("Invalid input! \n")
        continue

    if size <= 1 :
        print("Invalid input! \n")
        continue
    else :
        runGame(size)
        break