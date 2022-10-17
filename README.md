# pypuzzle
A sliding tile puzzle game of arbitrary size n = k\*k - 1.

Solver uses A* search with Manhattan distance heuristic.

Credit to @asarandi's [n-puzzle masterclass](https://github.com/asarandi/n-puzzle) for help with A* algorithm.

Note: if you have any concerns for filling up memory, don't run the solver algorithm for k > 3. (Greedy BFS and other less space-intensive algorithms coming soon!) Also, k = 2 has some strange cases that don't seem to match inversions theory, so 3-puzzles may not always be solvable.
