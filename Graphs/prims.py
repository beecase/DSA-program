import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def prim_mst(self):
        visited = [False] * self.V
        min_heap = [(0, 0, -1)]  # (weight, vertex, parent)
        total_cost = 0
        mst_edges = []

        while min_heap:
            weight, u, parent = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            total_cost += weight

            if parent != -1:
                mst_edges.append((parent, u, weight))

            for v, w in self.adj[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v, u))

        return total_cost, mst_edges



g = Graph(5)

g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

cost, mst = g.prim_mst()

print("Minimum Cost:", cost)
print("Edges in MST:")
for u, v, w in mst:
    print(u, "-", v, ":", w)