# pypuzzle
n-puzzle in python

## Algebraic formula for sqNum (the number of a given square on the puzzle board)

Below examples are for a 1-puzzle (1x1), 2-, 3-, 4- and 5-puzzle respectively, then generalizing to an n-puzzle.

____
1
____
1 2
3 4
____
1 2 3
4 5 6
7 8 9
____
1   2  3  4
5   6  7  8
9  10 11 12
13 14 15 16
____
1   2  3  4  5
6   7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
____
(1-1)n + 1, (1-1)n + 2, (1-1)n + 3, ... n
(2-1)n + 1, (2-1)n + 2, (2-1)n + 3, ... (2-1)n + n
(3-1)n + 1, (3-1)n + 2, (3-1)n + 3, ... (3-1)n + n
...
(n-1)n + 1, (n-1)n + 2, (n-1)n + 3, ... (n-1)n + n
____

x coord is one plus coefficient of n
y coord is the added constant

sqNum = (x-1)n + y

to get zero-indexed coordinates (for 2D array in program), subtract one from x and y respectively

thus the formula used in the function calcSqNum() is:
sqNum = coords[0] * dim + coords[1] + 1
where coords[0] is the zero-indexed x coordinate, and coords[1] is the zero-indexed y-coordinate