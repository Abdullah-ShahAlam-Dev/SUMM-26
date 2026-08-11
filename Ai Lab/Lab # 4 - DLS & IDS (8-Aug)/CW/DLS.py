graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}


def depth_limited_search(START, GOAL, LIMIT):
    VISITED = []
    STACK = [(START, 0)]

    while STACK:
        NODE, DEPTH = STACK.pop()

        if NODE not in VISITED:
            VISITED.append(NODE)
            print(f"VISITED: {NODE}, DEPTH: {DEPTH}")

            if NODE == GOAL:
                print("\nGOAL FOUND!")
                return VISITED

            # Expand node only if depth limit is not reached
            if DEPTH < LIMIT:
                for CHILD in reversed(graph[NODE]):
                    STACK.append((CHILD, DEPTH + 1))

    print("\nGOAL NOT FOUND WITHIN DEPTH LIMIT")
    return VISITED


depth_limited_search('A', 'H', 3)