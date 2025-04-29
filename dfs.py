# Function to perform DFS
def dfs(node, graph, visited):
    if node in visited:
        return
    print(node)
    visited.add(node)
    for neighbor in graph.get(node, []):
        dfs(neighbor, graph, visited)

# Input: number of edges
n = int(input("Enter number of edges: "))
graph = {}

# Build the undirected graph
for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

# DFS from all nodes to ensure all components are visited
visited = set()
for node in graph:
    if node not in visited:
        dfs(node, graph, visited)
