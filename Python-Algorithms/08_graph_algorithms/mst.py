"""
Minimum Spanning Tree (MST) Algorithms
Finds a subset of edges connecting all vertices in an undirected, edge-weighted graph with minimum total edge weight.
Includes:
1. Kruskal's Algorithm: Uses Disjoint Set Union (DSU) to sort edges and add non-cycle edges. O(E log E) time.
2. Prim's Algorithm: Uses a min-heap to grow MST from a starting node. O(E log V) time.
"""

import heapq

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def kruskals_mst(n, edges):
    """
    Kruskal's MST algorithm.
    edges: List of tuples (weight, u, v)
    Returns: (mst_edges, mst_weight)
    """
    dsu = DSU(n)
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[0])
    
    mst_edges = []
    mst_weight = 0
    
    for weight, u, v in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            mst_weight += weight
            if len(mst_edges) == n - 1:
                break
                
    return mst_edges, mst_weight

def prims_mst(n, adjacency_list):
    """
    Prim's MST algorithm.
    adjacency_list: dict where adj[u] is list of (neighbor_v, edge_weight)
    Returns: (mst_edges, mst_weight)
    """
    mst_edges = []
    mst_weight = 0
    visited = [False] * n
    
    # Priority queue storing (weight, u, parent)
    pq = [(0, 0, -1)]
    
    while pq and len(mst_edges) < n:
        weight, u, parent = heapq.heappop(pq)
        
        if visited[u]:
            continue
            
        visited[u] = True
        mst_weight += weight
        if parent != -1:
            mst_edges.append((parent, u, weight))
            
        for v, w in adjacency_list.get(u, []):
            if not visited[v]:
                heapq.heappush(pq, (w, v, u))
                
    return mst_edges, mst_weight

if __name__ == "__main__":
    print("=== Minimum Spanning Tree (MST) Demo ===")
    
    n_vertices = 4
    # Edges represented as (weight, u, v)
    edges = [
        (10, 0, 1),
        (6, 0, 2),
        (5, 0, 3),
        (15, 1, 3),
        (4, 2, 3)
    ]
    
    # Adjacency list representation for Prim's algorithm
    adj = {i: [] for i in range(n_vertices)}
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    print(f"Edges list: {edges}")
    
    kruskal_res, kruskal_wt = kruskals_mst(n_vertices, edges)
    print(f"\nKruskal's MST edges: {kruskal_res}")
    print(f"Kruskal's MST total weight: {kruskal_wt}")
    
    prim_res, prim_wt = prims_mst(n_vertices, adj)
    print(f"\nPrim's MST edges: {prim_res}")
    print(f"Prim's MST total weight: {prim_wt}")
