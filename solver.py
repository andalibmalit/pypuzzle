from itertools import count
from heapq import heappop, heappush

def swap_tiles(puzzle, i, j):
    new_state = list(puzzle)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return tuple(new_state)


def possible_moves(puzzle, size):
    moves = []
    i = puzzle.index(0)
    if i - size >= 0:
        moves.append(swap_tiles(puzzle, i, i - size))
    if i + size < len(puzzle):
        moves.append(swap_tiles(puzzle, i, i + size))
    if i % size > 0:
        moves.append(swap_tiles(puzzle, i, i - 1))
    if i % size + 1 < size:
        moves.append(swap_tiles(puzzle, i, i + 1))
    return moves


def manhattan(puzzle, size, goal):
    res = 0
    for i in range(size**2):
        if puzzle[i] != 0 and puzzle[i] != goal[i]:
            si = goal.index(puzzle[i])
            x = (i % size) - (si % size)
            y = (i // size) - (si // size)
            res += abs(y) + abs(x)
    return res


# See blog post for rundown
def a_star(state, goal, size):
    if size > 4:
        print("\nk larger than 4 is not supported for A* solutions to avoid running out of memory. Proceed at your own risk.")
        return (False, [])
    
    c = count()
    queue = [(0, next(c), state, 0, None)]
    open_set = {}
    closed_set = {}
    while queue:
        _, _, node, node_g, parent = heappop(queue)
        if node == goal:
            steps = [node]
            while parent is not None:
                steps.append(parent)
                parent = closed_set[parent]
            steps.reverse()
            return (True, steps)
        if node in closed_set:
            continue
        closed_set[node] = parent
        tentative_g = node_g + 1
        moves = possible_moves(node, size)
        for m in moves:
            if m in closed_set:
                continue
            if m in open_set:
                move_g, move_h = open_set[m]
                if move_g <= tentative_g:
                    continue
            else:
                move_h = manhattan(node, size, goal)
            open_set[m] = tentative_g, move_h
            heappush(queue, (move_h + tentative_g, next(c), m, tentative_g, node))
    return (False, [])