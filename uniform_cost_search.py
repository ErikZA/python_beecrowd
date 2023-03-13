from queue import PriorityQueue

# Function to get the position of the empty block in the board


def get_empty_pos(board):
    return board.index(' ')

# Function to check if the board is a goal state


def is_goal(state):
    return all(state[i] == 'A' for i in range(len(state)//2))

# Function to generate the successors of a board state


def generate_successors(board):
    empty_pos = get_empty_pos(board)
    successors = []
    for i in range(len(board)):
        # Skip empty block
        if i == empty_pos:
            continue
        # Swap empty block with another block
        successor = board[:]
        successor[empty_pos], successor[i] = successor[i], successor[empty_pos]
        successors.append(successor)
    return successors

# Uniform-cost search algorithm


def uniform_cost_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    explored = set()
    while not frontier.empty():
        # Pop the state with the lowest cost from the priority queue
        cost, state = frontier.get()
        if is_goal(state):
            return state
        explored.add(tuple(state))
        for successor in generate_successors(state):
            if tuple(successor) not in explored:
                # Calculate the cost to reach the successor state
                successor_cost = cost + 1
                # Add the successor state and its cost to the priority queue
                frontier.put((successor_cost, successor))
    return None


# Example usage
board = ['A', 'V', 'A', ' ', 'V', 'A', 'V', 'A', 'V', 'A']
solution = uniform_cost_search(board)
print(solution)
