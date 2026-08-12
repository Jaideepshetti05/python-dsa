def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [],
    4: []
}

visited = set()

dfs(graph, 0, visited)