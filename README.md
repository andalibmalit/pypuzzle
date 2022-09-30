# pypuzzle
n-puzzle in python

## Interesting theory
The method **chkInversions()** ensures that every puzzle generated is actually solvable. This is based off the "inversions" method for determining solvability of a given n-puzzle. If we assume the tiles are displayed in a 1-D array rather than 2-D, a pair of tiles [A, B] form an inversion where A appears before B, but A > B. Take the following example (x is the empty square):
### 2-D puzzle
|  7  |  4  |  6  |

|  x  |  8  |  2  |

|  1  |  3  |  5  |

### 1-D notation
[7, 4, 6, 8, 2, 1, 3, 5]

*Inversion count: 18*


According to the formula for inversion-based solvability:
* if matrix width *n* is odd, the puzzle is solvable only if there are an even number of inversions;
* if *n* is even and the blank square is on an even row counting from the bottom (e.g second-last or fourth-last row), the puzzle is solvable if the number of inversions is odd;
* if *n* is even and the blank square is on an odd row from the bottom (e.g. third-last), the puzzle is solvable if the number of inversions is even.

Thus the given example is solvable by the first set of criteria above.


See **chkInversions()** method comments for details on how I implemented this algorithm. 

## Algorithm for sqNum (the number of a given square on the puzzle board)

Below examples are for a 1-puzzle (1x1), 2-, 3-, 4- and 5-puzzle respectively, then generalizing to an n-puzzle. (Markdown syntax messes up the spacing; if interested please read this section in plaintext...)

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

To get zero-indexed coordinates (for 2D array in program), subtract one from x and y respectively

Thus the formula used in the function calcSqNum() is `sqNum = coords[0] * dim + coords[1] + 1` where coords[0] is the zero-indexed x coordinate, and coords[1] is the zero-indexed y-coordinate
