import heapq

graph = {
    'A': [('B', 5), ('D', 3)],
    'B': [('C', 1)],
    'C': [('E', 6), ('G', 8)],
    'D': [('E', 2), ('F', 2)],
    'E': [('B', 4)],
    'F': [('G', 3)],
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

        for neighbor, step in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + step, neighbor, path + [neighbor]))

    return None

print("Code BY:\n Abdullah Shah Alam")
path, cost = ucs(graph, 'A', 'G')
print("UCS Path:", path, "with Cost:", cost)
