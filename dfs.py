graph = {"A": ["1", "2"],
         "1": ["3"],
         "2": ["3", "4", "5", "G"],
         "3": ["G"],
         "4": [],
         "5": ["4", "F"],
         "F": ["G"],
         "G": [],
         }

###########################################################################
def dfs_shortest_path(graph, vertex, finish):
    """Returns shortest path."""
    visited = []
    path = []
    def dfs(visited, graph, vertex, finish):
        if vertex not in visited:
            visited.append(vertex)
            if vertex == finish:
                nonlocal path
                path.append(visited[:])
            for neighbor in graph[vertex]:
                dfs(visited, graph, neighbor, finish)
                visited.remove(neighbor)
    dfs(visited, graph, vertex, finish)
    if path:
        shortest_path = path[0]
        for i in path:
            if len(i) < len(shortest_path):
                shortest_path = i
    return shortest_path

print("Shortest path:", dfs_shortest_path(graph, "A", "G"))


###########################################################################
def dfs_found_paths(graph, vertex, finish):
    """Returns all possible paths."""
    visited = []
    path = []
    def dfs(visited, graph, vertex, finish):
        if vertex not in visited:
            visited.append(vertex)
            if vertex == finish:
                nonlocal path
                path.append(visited[:])
            for neighbor in graph[vertex]:
                dfs(visited, graph, neighbor, finish)
                visited.remove(neighbor)
    dfs(visited, graph, vertex, finish)
    return path

print("All possible paths:", dfs_found_paths(graph, "A", "G"))


###########################################################################
def dfs_first_path(graph, vertex, finish):
    """Returns the first path found."""
    visited = []
    path = []
    found = False
    def dfs(visited, graph, vertex, finish):
        nonlocal found
        if vertex not in visited:
            visited.append(vertex)
            if vertex == finish and not found:
                found = True
                nonlocal path
                path = visited[:]
            for neighbor in graph[vertex]:
                dfs(visited, graph, neighbor, finish)
                visited.remove(neighbor)
    dfs(visited, graph, vertex, finish)
    return path

print("Fitst path found:", dfs_first_path(graph, "A", "G"))
