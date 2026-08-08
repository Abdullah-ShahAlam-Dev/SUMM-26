# Code
import random
from collections import deque

# Generate Starting Puzzle

number = "0189"      
random.seed(number)

digits = list("012345678")
random.shuffle(digits)

start = "".join(digits)
# start = "123450786"

goal = "123456780"

print("Starting Puzzle:", start)
print("Goal Puzzle:", goal)

# Move Functions

def move_up(puzzle):
    index = puzzle.index("0")

    if index < 3:
        return None

    new = list(puzzle)
    new[index], new[index - 3] = new[index - 3], new[index]
    return "".join(new)


def move_down(puzzle):
    index = puzzle.index("0")

    if index > 5:
        return None

    new = list(puzzle)
    new[index], new[index + 3] = new[index + 3], new[index]
    return "".join(new)


def move_left(puzzle):
    index = puzzle.index("0")

    if index % 3 == 0:
        return None

    new = list(puzzle)
    new[index], new[index - 1] = new[index - 1], new[index]
    return "".join(new)


def move_right(puzzle):
    index = puzzle.index("0")

    if index % 3 == 2:
        return None

    new = list(puzzle)
    new[index], new[index + 1] = new[index + 1], new[index]
    return "".join(new)

# Get Next States

def get_next_states(puzzle):
    next_states = []

    for move in [move_up, move_down, move_left, move_right]:
        state = move(puzzle)
        if state is not None:
            next_states.append(state)

    return next_states

# BFS Algorithm

def bfs(start, goal):
    queue = deque([start])

    visited = set()
    visited.add(start)

    parent = {}
    states_checked = 0

    while queue:
        current = queue.popleft()
        states_checked += 1

        if current == goal:
            path = []

            while current != start:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path, states_checked

        for next_state in get_next_states(current):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                queue.append(next_state)

    return None, states_checked

# Print Puzzle Nicely

def print_puzzle(puzzle):
    for i in range(0, 9, 3):
        print(" ".join(puzzle[i:i+3]))
    print()

# Run BFS

path, checked = bfs(start, goal)

if path:
    print("\nSolution Found!\n")

    for step, state in enumerate(path):
        print("Step", step)
        print_puzzle(state)

    print("Total Moves:", len(path) - 1)
    print("Total States Checked:", checked)

else:
    print("\nNo solution exists for this puzzle.")
    print("States Checked:", checked)