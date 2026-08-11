import heapq

# Graph dictionary as shown in the slide
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

# Heuristic values (estimated distance to goal F)
heuristic = {
    'S': 12,
    'A': 9,
    'B': 8,
    'C': 6,
    'D': 4,
    'E': 5,
    'F': 0
}

def greedy_best_first_search(start, goal):
    # Priority queue mein (heuristic, node, path) store hoga
    pq = [(heuristic[start], start, [start])]
    visited = set()
    
    print("--- CODE BY: ABdulah Shah Alam ---")
    print("--- Search Trace ---")
    
    while pq:
        # Hamesha lowest heuristic wala node pop hoga
        h, current, path = heapq.heappop(pq)
        
        # Requirement: Print the heuristic value at each step chosen
        print(f"Visiting Node '{current}' with heuristic = {h}")
        
        # Agar goal mil gaya toh ruk jayenge
        if current == goal:
            print("\n--- Final Result ---")
            print("Final Path Found:", " -> ".join(path))
            return path
            
        if current in visited:
            continue
            
        visited.add(current)
        
        # Neighbors ko check karo aur queue mein daalo
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor]))
                
    return None

# Start node 'S' hai aur Goal node 'F' hai
greedy_best_first_search('S', 'F')