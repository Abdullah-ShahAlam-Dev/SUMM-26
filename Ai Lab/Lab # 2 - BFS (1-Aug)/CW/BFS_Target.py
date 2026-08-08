# learnig  bfs

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 2]
}

def bfs(graph, start, target):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node == target:
                return visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
    return visited
# Ab humne 3 ko target bana diya hai
result = bfs(graph, 0, 3)
print("BFS Traversal Order:", result)