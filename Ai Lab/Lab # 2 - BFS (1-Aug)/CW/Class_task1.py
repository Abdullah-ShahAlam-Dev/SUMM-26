# learnig  bfs
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 2, 5],  # 4 ko 5 se connect kiya
    5: [4, 6],     # 5 ko 4 aur 6 se connect kiya
    6: [5, 7],     # 6 ko 5 aur 7 se connect kiya
    7: [6]         # 7 ko 6 se connect kiya
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

result = bfs(graph, 0)
print("BFS Traversal Order:", result)