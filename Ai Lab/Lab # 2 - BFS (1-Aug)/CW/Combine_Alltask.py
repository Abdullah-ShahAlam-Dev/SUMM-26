graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 2, 5], # 4 ko 5 se connect kiya
    5: [4, 6],
    6: [5, 7],
    7: [6]
}

# Task 2: Counter added inside BFS function
def bfs(graph, start):
    visited = []
    queue = [start]
    # coounter initialze
    count = 0
    
    while queue:
        node = queue.pop(0)
        count += 1  # Node pop hone par count increase
        
        if node not in visited:
            visited.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
    return visited, count  # Return dono values

# Task 3: Run for starting point 0 and 3, and print counts
visited_from_0, count_0 = bfs(graph, 0)
print("Start from 0 -> Order:", visited_from_0, "| Nodes Checked:", count_0)

visited_from_3, count_3 = bfs(graph, 3)
print("Start from 3 -> Order:", visited_from_3, "| Nodes Checked:", count_3)