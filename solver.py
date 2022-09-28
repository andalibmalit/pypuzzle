class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(data)
        
    def dequeue(self):
        if !self.isEmpty():
            min_cost, item = None
            for x in self.queue:
                if min_cost = None:
                    min_cost = x["cost"]
                else:
                    if x["cost"] < min_cost:
                        min_cost = x["cost"]
                        item = x
            self.queue.remove(item)
            return item
        else:
            raise LookupError("Attempted to query empty queue.")
        
    def contains(item):
        boolly = False
        for x in self.queue:
            if (item['state'] == x['state']):
                boolly = True
        return boolly
    
    # Only returns useful info for closed_queue
    def listMoves():
        moves = list()
        for i in range(len(self.queue)):
            moves.append(self.queue[i]['last_move'])
        moves.reverse()
        return moves


def a_star(board, solved):
    # Each element of the queues below is a list containing
    #   consecutive puzzle states, the tile moved to reach
    #   that state, and the possible moves in each state.
    open_queue = PriorityQueue()
    closed_queue = PriorityQueue()
    
    open_queue.enqueue({"state": board, "last_move": 0, "moves": possible_moves(board), "cost": 0})
    while !open_queue.isEmpty():
        # Dequeue move with lowest cost, add to closed_queue
        current_state = open_queue.dequeue()
        closed_queue.queue(current_state)
        
        if current_state['state'] == solved:
            break
        
        # Add possible moves from current state to open_queue,
        #   if not 
        for move in current_state["moves"]:
            tentative_state = move['state']         
            next_state = {'state': tentative_state, 
                         'last_move': move['moved'], 
                         'moves': possible_moves(tentative_state), 
                         'cost': start_dist(tentative_state) + manhattan(tentative_state)}
            if !closed_queue.contains(next_state):
                if !open_queue.contains(next_state):
                    open_queue.queue(current_state)
                    
    return closed_queue.listMoves()
                    
        
            
            
            

def possible_moves(state):
    
            
def manhattan(state):
    

def start_dist(state)

# may not be needed   
def toList(board):
    d1_puzzle = list()
    for row in board:
        for num in row:
            d1_puzzle.append(num)
    return d1_puzzle