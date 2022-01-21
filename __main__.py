from game_functions import *

print('''Welcome to n-puzzle! The number of tiles in the puzzle is (n * n - 1), where n 
is an integer greater than 1. The more tiles, the harder the puzzle.''')
print()

#

# WARNING! There is currently no limit on puzzle size, very large values of n may crash your computer.
#   (Threshold to be determined...)

#

while True:
    try :
        size = int(input("What size puzzle would you like to solve? Enter an integer n > 1: "))
    except ValueError:
        print("Invalid input! \n")
        continue

    if size <= 1 :
        print("Invalid input! \n")
        continue
    else :
        runGame(size)
        break