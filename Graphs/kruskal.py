class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already in the same component (cycle)
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


def kruskal(n, edges):
    """
    n     : number of vertices (0 to n-1)
    edges : list of (weight, u, v)
    returns: (MST cost, list of edges in MST)
    """
    edges.sort()  # Sort edges by weight
    uf = UnionFind(n)
    mst_cost = 0
    mst_edges = []

    for weight, u, v in edges:
        if uf.union(u, v):          # Add edge only if it doesn't form a cycle
            mst_cost += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == n - 1:  # MST is complete
                break

    return mst_cost, mst_edges


# Example 
n = 4
edges = [
    (1, 0, 1),
    (3, 1, 2),
    (4, 2, 3),
    (2, 0, 2),
    (5, 1, 3)
]

cost, mst = kruskal(n, edges)

print("MST Cost:", cost)
print("Edges:", mst)