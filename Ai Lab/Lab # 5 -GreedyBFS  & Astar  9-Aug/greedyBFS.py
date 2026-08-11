import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 3,
    'E': 0
}

def greedy_search(start, goal):
    pq = [(heuristic[start], start, [start])]
    visited = set()
    
    while pq:
        h, current, path = heapq.heappop(pq)
        
        if current == goal:
            return path
            
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor]))
                
    return None

result = greedy_search('A', 'E')
print("Greedy Best First Search:", result)