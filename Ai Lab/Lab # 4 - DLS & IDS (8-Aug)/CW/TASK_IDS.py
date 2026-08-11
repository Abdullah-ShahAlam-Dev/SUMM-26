# Graph representation from the image
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['G'],
    'F': ['G'],
    'G': [],
    'H': []
}

# Modified DLS for IDS logic 
def dls_for_ids(start, goal, limit):
    visited = []
    stack = [(start, 0)]

    while stack:
        node, depth = stack.pop()

        if node not in visited:
            visited.append(node)
            print(f"Visited: {node}, Depth: {depth}")

            if node == goal:
                # Return True, visited list, and the depth where it was found
                return True, visited, depth

            if depth < limit:
                for child in reversed(graph[node]):
                    stack.append((child, depth + 1))

    return False, visited, -1

# Iterative Deepening Search function
def iterative_deepening_search(start, goal, max_depth):
    iteration = 0

    # Increase depth limit one by one
    for depth_limit in range(max_depth + 1):
        iteration += 1
        print(f"\n===== Iteration {iteration} | Depth Limit: {depth_limit} =====")

        found, visited, found_depth = dls_for_ids(start, goal, depth_limit)

        # If goal is found
        if found:
            print("\n================================")
            print(f"Goal Node: {goal}")
            print(f"Goal found at Depth: {found_depth}")
            print(f"Goal found in Iteration: {iteration}")
            print("================================")
            return visited

    print("\nGoal not found within maximum depth.")
    return visited

# Running Task 2
print("=== Task 2: Iterative Deepening Search ===")
print("=== CODE BY: Abdullah Shha Alam ===")
start_node = 'A'
goal_node = 'G'
max_depth = 5  # Setting a max depth to avoid infinite loop

visited_order = iterative_deepening_search(start_node, goal_node, max_depth)
print("\nFinal Visited Order:", visited_order)