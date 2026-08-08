graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': ['P', 'Q'],
    'I': ['R'],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': [],
    'P': [],
    'Q': [],
    'R': []
}


# Depth-Limited Search function
def depth_limited_search(start, goal, limit):
    visited = []
    stack = [(start, 0)]

    while stack:
        node, depth = stack.pop()

        if node not in visited:
            visited.append(node)
            print(f"Visited: {node}, Depth: {depth}")

            # Goal found
            if node == goal:
                print("\nGoal found!")
                return True, visited

            # Add child nodes only if depth limit not reached
            if depth < limit:
                for child in reversed(graph[node]):
                    stack.append((child, depth + 1))

    return False, visited


# Iterative Deepening Search function
def iterative_deepening_search(start, goal, max_depth):

    # Iteration counter
    iteration = 0

    # Increase depth limit one by one
    for depth_limit in range(max_depth + 1):

        # Increase iteration number
        iteration += 1

        print(f"\n===== Iteration {iteration} | Depth Limit: {depth_limit} =====")

        found, visited = depth_limited_search(
            start, goal, depth_limit
        )

        # If goal is found
        if found:
            print("\n================================")
            print(f"Goal Node: {goal}")
            print(f"Goal found at Depth: {depth_limit}")
            print(f"Goal found in Iteration: {iteration}")
            print("================================")

            return visited

    print("\nGoal not found within maximum depth.")
    return visited


# Run the IDS algorithm
start_node = 'A'
goal_node = 'M'
max_depth = 4

visited_order = iterative_deepening_search(
    start_node,
    goal_node,
    max_depth
)

print("\nVisited Order:", visited_order)