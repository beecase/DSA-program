from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.adjacency_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency_list[u].append(v)
        if not self.directed:
            self.adjacency_list[v].append(u)

    def bfs(self, start):
        if start not in self.adjacency_list:
            return []

        visited = set()
        queue = deque([start])
        order = []
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            order.append(vertex)

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    

    def dfs_recursive(self, start):
        if start not in self.adjacency_list:
            return []

        visited = set()
        order = []

        def _dfs(vertex):
            visited.add(vertex)
            order.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return order

    def __str__(self):
        lines = []
        for vertex, neighbors in self.adjacency_list.items():
            lines.append(f"  {vertex} → {neighbors}")
        return "Graph:\n" + "\n".join(lines)


# --- Demo ---
g = Graph()
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F')]
for u, v in edges:
    g.add_edge(u, v)

print(g)
print("BFS from A:           ", g.bfs('A'))
print("DFS recursive from A: ", g.dfs_recursive('A'))