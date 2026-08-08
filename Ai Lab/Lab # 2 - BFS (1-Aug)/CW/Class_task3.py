# Task 3: Change Starting Point

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 2]
}

def bfs(graph, start):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
    return visited

# 1. Pehle Node 0 se start kar ke result print karein
result_from_0 = bfs(graph, 0)
print("Traversal starting from Node 0:", result_from_0)

# 2. Ab Node 3 se start kar ke result print karein
result_from_3 = bfs(graph, 3)
print("Traversal starting from Node 3:", result_from_3)