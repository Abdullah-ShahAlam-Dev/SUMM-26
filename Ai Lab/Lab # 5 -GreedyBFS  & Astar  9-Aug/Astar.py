import heapq

# Graph with edge costs (child, cost)
GRAPH = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 3)],
    'C': [('E', 5)],
    'D': [('E', 2)],
    'E': []
}

# Heuristic values for each node
HEURISTICS = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 3,
    'E': 0
}

def a_star(start, goal):
    g_start = 0
    h_start = HEURISTICS[start]
    f_start = g_start + h_start
    
    # queue format: (f_cost, node, path, g_cost)
    queue = [(f_start, start, [start], g_start)]
    visited = []
    
    print("--- CODE BY: Abdullah Shahalam ---")
    
    while queue:
        f_cost, node, path, g_cost = heapq.heappop(queue)
        
        if node in visited:
            continue
            
        if node == goal:
            print("\nGoal Reached!")
            print(" -> ".join(path), "=", g_cost)
            return path
            
        visited.append(node)
        
        for child, cost in GRAPH[node]:
            if child in visited:
                continue
                
            new_g = g_cost + cost
            new_h = HEURISTICS[child]
            new_f = new_g + new_h
            new_path = path + [child]
            
            heapq.heappush(queue, (new_f, child, new_path, new_g))
            
    return None

# Start node 'A' aur Goal node 'E' ke sath function call
a_star('A', 'E')