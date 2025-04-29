from collections import deque

# Recursive BFS helper
def bfs_recursive(queue, graph, visited):
    if not queue:
        return
    node = queue.popleft()
    print(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    bfs_recursive(queue, graph, visited)

# Input section
n = int(input("Enter number of edges: "))
graph = {}

for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

# Run BFS from all components
visited = set()
for node in graph:
    if node not in visited:
        visited.add(node)
        bfs_recursive(deque([node]), graph, visited)
