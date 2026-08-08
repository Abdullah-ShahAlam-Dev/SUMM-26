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

def depth_limited_search(start, goal, limit):
    visited = []
    stack = [(start, 0)]  # Stack holds (node, depth)

    while stack:
        node, depth = stack.pop()

        if node not in visited:
            visited.append(node)
            print(f"Visited: {node}, Depth: {depth}")

            # Goal found condition
            if node == goal:
                print("\nGOAL FOUND!")
                return visited

            # Expand node only if depth limit is not reached
            if depth < limit:
                for child in reversed(graph[node]):
                    stack.append((child, depth + 1))

    print("\nGOAL NOT FOUND WITHIN DEPTH LIMIT")
    return visited

# Running Task 1
print("=== Task 1: Depth-Limited Search ===")
print("=== CODE BY: Abdullah Shha Alam ===")
start_node = 'A'
goal_node = 'G'
depth_limit = 2

print(f"Searching for '{goal_node}' with Depth Limit = {depth_limit}\n")
visited_nodes = depth_limited_search(start_node, goal_node, depth_limit)
print("\nVisited Order:", visited_nodes)