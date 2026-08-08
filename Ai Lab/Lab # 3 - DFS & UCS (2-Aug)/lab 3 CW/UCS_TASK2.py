import heapq

# Task 2: UCS Weighted Graph[cite: 1]
graph_ucs = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 2), ('C', 7)],
    'C': [('D', 1), ('G', 6)],
    'D': [('G', 3)],
    'G': []
}

def ucs(graph, start, goal):
    visited = set()
    queue = [(0, start, [start])]

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        if node in visited:
            continue
        visited.add(node)

# used here graph bcz if node did not exist in graph so move foraward dont crashs /stop the porgram
        for neighbor, step in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + step, neighbor, path + [neighbor]))

    return None, None # 1 for path another for cost

print("Code BY:\n Abdullah Shah Alam")
path, cost = ucs(graph_ucs, 'A', 'G')
print("UCS Path:", path, "with Cost:", cost)