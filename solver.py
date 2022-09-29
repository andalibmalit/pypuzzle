class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
    
    # Dequeue is not working properly, it appears that nothing gets deleted
    #   from `queue`...    
    def dequeue(self):
        if not self.isEmpty():
            min_cost, item = self.queue[0]['cost'], self.queue[0]
            for x in self.queue:
                if x['cost'] < min_cost:
                    min_cost = x['cost']
                    item = x
            self.queue.remove(item)
            return item
        else:
            raise LookupError("Attempted to query empty queue.")
    
    def findState(self, item):
        for i in range(len(self.queue)):
            if self.queue[i]['board_state'] == item['board_state']:
                found = self.queue[i]
                
        return found
        
    def contains(self, item):
        boolly = False
        for x in self.queue:
            if (item['board_state'] == x['board_state']):
                boolly = True
        return boolly
    
    # Only returns useful info for closed_queue
    def listMoves(self):
        moves = list()
        for i in range(len(self.queue)):
            # Ignore initial move of '0' (empty space)
            if self.queue[i]['last_move'] != 0:
                moves.append(self.queue[i]['last_move'])
        return moves


def a_star(board, solved):
    # Each element of the queues below is a list containing
    #   consecutive puzzle states, the tile moved to reach
    #   that state, and the possible moves in each state.
    open_queue = PriorityQueue()
    closed_queue = PriorityQueue()
    
    init_board = board
    
    open_queue.enqueue({'board_state': init_board, 'last_move': 0, 'possible_moves': possible_moves(init_board), 'cost': 0})
    
    #debug
    #print("Possible moves: ")
    #print(possible_moves(board))
    #count = 0
    #print("Starting queue: ")
    #print(open_queue.queue)
    #/debug
    
    while not open_queue.isEmpty():
        
        #debug
        #print("**ITERATION**: " + str(count))
        #count += 1
        #if count >= 5:
            #break
        #/debug
        
        # Dequeue move with lowest cost, add to closed_queue
        current_state = open_queue.dequeue()
        while not open_queue.isEmpty():
            open_queue.dequeue()
        
        #debug
        #print("current_state: ")
        #print(current_state)
        #print("Check if dequeue worked: ")
        #print(open_queue.queue)        
        #/debug
        
        closed_queue.enqueue(current_state)
        
        if current_state['board_state'] == solved:
            
            #debug
            #print("Solved!")
            #/debug
            
            break
        
        # Add possible moves from current state to open_queue,
        #   if not already in either queue
        
        # stuck on infinite loop at very first iteration... just repeats
        #   the same tentative states after init_board over and over
        for move in current_state['possible_moves']:
            tentative_state = move['new_state']
            
            #debug
            #print("Tentative state: ")
            #print(toList(tentative_state))         
            #/debug
            
            next_state = {'board_state': tentative_state, 
                         'last_move': move['moved'], 
                         'possible_moves': possible_moves(tentative_state), 
                         'cost': start_dist(init_board, tentative_state) + manhattan(tentative_state, solved)}
            
            if not closed_queue.contains(next_state):
                if open_queue.contains(next_state):
                    if open_queue.findState(next_state)['cost'] > next_state['cost']:
                        
                        #debug
                        #print("Enqueued next_state:")
                        #print(next_state)
                        #print("cost: ")
                        #print(next_state['cost'])
                        #/debug
                        open_queue.queue.remove(open_queue.findState(next_state))
                        open_queue.enqueue(next_state)
                else:
                    
                    #debug
                    #print("Enqueued next_state:")
                    #print(next_state)
                    #print("cost: ")
                    #print(next_state['cost'])
                    #/debug
                    
                    open_queue.enqueue(next_state)
    
    #debug
    #print("SOLUTION: ")
    #/debug
    
    return closed_queue.listMoves()
            

def swap_tiles(board_1D, i, j, size):
    temp_board = list(board_1D)
    temp_board[i], temp_board[j] = temp_board[j], temp_board[i]
    return temp_board[i], toBoard(temp_board, size)


# Returns 'possible_moves', a list of dictionaries each with two keys 'moved' and 'new_state'.
#   'moved' is the number of the tile moved into the empty space.
#   'new_state' is the state of the board after moving said tile.
#   Credit to @asarandi on Github for his elegant function; I adapted it to my puzzle.
def possible_moves(board):
    moves = list()
    board_1D = toList(board)
    
    #debug
    #print("board_1D: ")
    #print(board_1D)
    #/debug
    
    i = board_1D.index(0)
    
    if i - len(board) >= 0:
        moved, new_state = swap_tiles(board_1D, i, i - len(board), len(board))
        moves.append({'moved': moved, 'new_state': new_state})
    if i + len(board) < (len(board))**2:
        moved, new_state = swap_tiles(board_1D, i, i + len(board), len(board))
        moves.append({'moved': moved, 'new_state': new_state})
    if i % len(board) > 0:
        moved, new_state = swap_tiles(board_1D, i, i - 1, len(board))
        moves.append({'moved': moved, 'new_state': new_state})
    if i % len(board) + 1 < len(board):
        moved, new_state = swap_tiles(board_1D, i, i + 1, len(board))
        moves.append({'moved': moved, 'new_state': new_state})
        
    return moves
    

# Representing distance of a board state from initial state by the number of tiles in 
#    a different position
def start_dist(init_board, board):
    mismatch_count = 0
    for i in range(len(init_board)):
        for j in range(len(init_board)):
            if init_board[i][j] != board[i][j]:
                mismatch_count += 1
    
    return mismatch_count


# Using Manhattan distance for heuristic of possible moves
def manhattan(board, solved):
    board_1D = toList(board)
    solved_1D = toList(solved)
    size = len(board)
    
    h = 0
    for i in range(size**2):
        if board_1D[i] != 0 and board_1D[i] != solved_1D[i]:
            si = solved_1D.index(board_1D[i])
            y = (i // size) - (si // size)
            x = (i % size) - (si % size)
            h += abs(y) + abs(x)
    return h


def toList(board):
    board_1D = list()
    for row in board:
        for num in row:
            board_1D.append(num)
    return board_1D


# may be problematic
def toBoard(board_1D, size):
    board = [[0 for i in range(size)] for j in range(size)]
    depth = 0
    for i in range(size):
        for j in range(size):
            board[i][j] = board_1D[i+j+depth]
        #!!!!!
        depth += size - 1
        
    return board