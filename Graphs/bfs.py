graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B','E','D'],
    'D': ['C','F'],
    'E': ['C', 'F','D'],
    'F': ['D', 'E']
}
def bfs(graph, start):
    visited = set()
    queue = [start]

    visited.add(start)

    while queue:
        vertex = queue.pop(0)   # dequeue
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


bfs(graph, 'B')