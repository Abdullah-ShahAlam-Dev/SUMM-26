# Task 1: DFS Graph
graph_dfs = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def dfs(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # Neighbors ko stack mein add karna
            stack.extend(reversed(graph.get(node, [])))
            # stack.extend(reversed(graph[node]))

    return visited

print("Code BY:\n Abdullah Shah Alam")
result = dfs(graph_dfs, 'A') # clling nodes letter 
print("DFS TRAVERSAL: ", result)