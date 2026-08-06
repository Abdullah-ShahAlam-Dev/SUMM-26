# Task 2: Count Nodes Checked

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 2, 5],  # 4 ko 5 se connect kiya
    5: [4, 6],     # 5 ko 4 aur 6 se connect kiya
    6: [5, 7],     # 6 ko 5 aur 7 se connect kiya
    7: [6] 
}

def bfs_with_counter(graph, start):
    visited = []
    queue = [start]
    
    # 1. Yahan counter start kiya
    count = 0  

    while queue:
        node = queue.pop(0)
        
        # 2. Jab bhi node pop hoga, count 1 barh jayega
        count += 1  

        if node not in visited:
            visited.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
    # 3. Visited list aur count dono ko return kiya
    return visited, count  

# Function ko call kiya aur dono values ko alag variables mein save kiya
visited_nodes, total_checked = bfs_with_counter(graph, 0)

print("BFS Traversal Order:", visited_nodes)
print("Total Nodes Checked (Popped):", total_checked)