"""
TSP Approximation Algorithms (Metric TSP)
TSP is NP-Hard. If edge weights satisfy the triangle inequality (Metric TSP), we can approximate it.
Includes:
1. 2-Approximation Algorithm (MST-based):
   - Computes MST.
   - Traverses MST using DFS (pre-order) to get a path.
   - Shortcuts visited vertices to form a tour.
   - Ratio: <= 2 * OPT.
2. Christofides 1.5-Approximation Algorithm:
   - Computes MST.
   - Finds odd-degree vertices in MST.
   - Computes a Minimum-Weight Perfect Matching on odd-degree vertices.
   - Combines MST + Matching to form an Eulerian multigraph.
   - Constructs Eulerian path and shortcuts to get Hamiltonian cycle.
   - Ratio: <= 1.5 * OPT.
"""

import math
import heapq

class TSPApproximation:
    def __init__(self, size, adj_matrix):
        self.n = size
        self.adj = adj_matrix  # 2D symmetric distance matrix

    def _get_mst_adjacency(self):
        """Computes MST using Prim's algorithm. Returns adj list of MST."""
        mst = {i: [] for i in range(self.n)}
        visited = [False] * self.n
        pq = [(0, 0, -1)]  # (weight, u, parent)
        
        while pq:
            w, u, parent = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            if parent != -1:
                mst[parent].append(u)
                mst[u].append(parent)
                
            for v in range(self.n):
                if not visited[v] and u != v:
                    heapq.heappush(pq, (self.adj[u][v], v, u))
        return mst

    # --- 1. 2-Approximation (MST DFS) ---
    def solve_mst_approximation(self):
        mst = self._get_mst_adjacency()
        
        # Traverse MST using DFS (pre-order)
        tour = []
        visited = [False] * self.n
        
        def dfs(u):
            visited[u] = True
            tour.append(u)
            for v in mst[u]:
                if not visited[v]:
                    dfs(v)
                    
        dfs(0)
        # Return to starting vertex to complete cycle
        tour.append(0)
        
        # Calculate cost
        cost = sum(self.adj[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        return tour, cost

    # --- 2. Christofides 1.5-Approximation ---
    def solve_christofides(self):
        mst = self._get_mst_adjacency()
        
        # Find odd degree vertices in MST
        odd_vertices = [u for u in range(self.n) if len(mst[u]) % 2 != 0]
        
        # Minimum Weight Perfect Matching on odd vertices (Greedy approximation of matching)
        matched = set()
        matching_edges = []
        
        # Sort pairs of odd vertices by distance
        pairs = []
        for i in range(len(odd_vertices)):
            for j in range(i + 1, len(odd_vertices)):
                u, v = odd_vertices[i], odd_vertices[j]
                pairs.append((self.adj[u][v], u, v))
        pairs.sort()
        
        for w, u, v in pairs:
            if u not in matched and v not in matched:
                matched.add(u)
                matched.add(v)
                matching_edges.append((u, v))
                
        # Combine MST edges and Matching edges to form multigraph
        multigraph = {i: list(mst[i]) for i in range(self.n)}
        for u, v in matching_edges:
            multigraph[u].append(v)
            multigraph[v].append(u)
            
        # Find Hierholzer's Eulerian circuit in multigraph
        # Working copies of neighbor lists
        adj_copy = {i: list(multigraph[i]) for i in range(self.n)}
        curr_path = [0]
        eulerian_circuit = []
        
        while curr_path:
            curr_v = curr_path[-1]
            if adj_copy[curr_v]:
                next_v = adj_copy[curr_v].pop()
                adj_copy[next_v].remove(curr_v)  # remove reverse edge in undirected graph
                curr_path.append(next_v)
            else:
                eulerian_circuit.append(curr_path.pop())
                
        eulerian_circuit.reverse()
        
        # Shortcut to form Hamiltonian Cycle
        visited = [False] * self.n
        tour = []
        for v in eulerian_circuit:
            if not visited[v]:
                tour.append(v)
                visited[v] = True
        tour.append(tour[0])  # Complete cycle
        
        # Calculate cost
        cost = sum(self.adj[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        return tour, cost

if __name__ == "__main__":
    print("=== TSP Metric Approximation Demo ===")
    
    # 4 vertices (represent points in 2D space to satisfy triangle inequality)
    # A(0,0), B(0,3), C(4,3), D(4,0)
    # Distances:
    # AB = 3, BC = 4, CD = 3, DA = 4
    # AC = 5, BD = 5
    adj_matrix = [
        [0, 3, 5, 4],
        [3, 0, 4, 5],
        [5, 4, 0, 3],
        [4, 5, 3, 0]
    ]
    
    tsp = TSPApproximation(4, adj_matrix)
    
    tour_2approx, cost_2approx = tsp.solve_mst_approximation()
    print(f"\n2-Approximation (MST-based):")
    print(f"  Tour: {tour_2approx} | Cost: {cost_2approx}")
    
    tour_christo, cost_christo = tsp.solve_christofides()
    print(f"\nChristofides 1.5-Approximation:")
    print(f"  Tour: {tour_christo} | Cost: {cost_christo}")
