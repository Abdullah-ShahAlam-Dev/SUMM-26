graph = {
    0: [0, 1, 2],
    1: [0, 2],
    2: [0, 1, 4],
    3: [0],
    4: [2]
}


def dfs(graph, start):
    visited= []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

    return visited
print("Code BY:\n Abdullah Shah Alam")
result = dfs(graph,0)
print("DFS TRIVERSAL: ", result)