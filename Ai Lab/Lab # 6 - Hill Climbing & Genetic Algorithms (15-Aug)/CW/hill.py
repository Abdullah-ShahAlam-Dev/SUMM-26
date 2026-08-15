graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D', 'E'],
    'B': ['F', 'G'],
    'C': ['H', 'I'],
    'G': ['J', 'K'],
    'I': ['L', 'M'],
    'K': ['N', 'O']
}

heuristic = {
    'S': 12, 'A': 9, 'B': 11,
    'C': 8, 'D': 9, 'E': 7, 'F': 9, 'G': 9,
    'H': 6, 'I': 5, 'J': 7, 'K': 6,
    'L': 2, 'M': 0, 'N': 4, 'O': 4
}

def hill_climbing(start):
    current = start
    path = [current]

    while True:
        neighbors = graph.get(current, [])
        if not neighbors:
            break

        # Find the neighbor with the smallest heuristic
        best = neighbors[0]
        best_value = heuristic[best]

        for n in neighbors:
            if heuristic[n] < best_value:
                best_value = heuristic[n]
                best = n

        # Stop if no improvement
        if heuristic[best] >= heuristic[current]:
            break

        current = best
        path.append(current)

    print("Hill-Climbing Path without back tracking:", path)

# Function ko call karna
hill_climbing('S')