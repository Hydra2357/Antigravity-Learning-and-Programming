"""
Minimum Cut Algorithms
Finds a cut (partition of vertices into two sets S and T) that minimizes the sum of weights of edges crossing the cut.
Includes:
- Karger's Randomized Contraction Algorithm:
  - Repeatedly contracts randomly chosen edges in an undirected multigraph until only 2 vertices remain.
  - The edges between these two vertices represent the cut.
  - Time Complexity: O(V^2) per trial.
  - Run multiple trials (e.g. V^2 * log V trials) to find the minimum cut with high probability.
"""

import random
import copy

class KargerMinCut:
    def __init__(self, num_vertices, edges):
        """
        edges: list of tuples (u, v) representing undirected edges.
        """
        self.v = num_vertices
        self.edges = edges

    def run_single_contraction(self):
        """
        Contracts edges randomly until only 2 vertices are left.
        Returns: (cut_size, surviving_vertices_representative_sets)
        """
        # Working copy of edges
        edges_copy = list(self.edges)
        
        # dsu maintains connected components of contracted vertices
        parent = list(range(self.v))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
            
        vertices_remaining = self.v
        
        # Contract edges
        while vertices_remaining > 2:
            # Pick a random edge
            edge_idx = random.randint(0, len(edges_copy) - 1)
            u, v = edges_copy[edge_idx]
            
            if union(u, v):
                vertices_remaining -= 1
                
            # Filter out self-loops (edges between contracted nodes in same component)
            edges_copy = [(x, y) for (x, y) in edges_copy if find(x) != find(y)]
            
        # The remaining edges represent the cut crossing the two components
        cut_size = len(edges_copy)
        return cut_size

    def find_min_cut(self, trials=None):
        if trials is None:
            # Theoretical number of trials to guarantee high probability is O(V^2 log V)
            trials = self.v * self.v
            
        min_cut = float('inf')
        for _ in range(trials):
            cut_size = self.run_single_contraction()
            if cut_size < min_cut:
                min_cut = cut_size
        return min_cut

if __name__ == "__main__":
    print("=== Karger's Randomized Min-Cut Demo ===")
    
    # 4-vertex graph:
    # 0 - 1
    # | \ |
    # 2 - 3
    # Min-cut is 2 (e.g. cutting 0-1 and 0-3 leaves 0 isolated)
    edges = [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 3),
        (2, 3)
    ]
    num_vertices = 4
    
    karger = KargerMinCut(num_vertices, edges)
    
    # Run a few trials
    trials = 20
    min_cut = karger.find_min_cut(trials=trials)
    print(f"Number of Vertices: {num_vertices}")
    print(f"Edges:              {edges}")
    print(f"Min-Cut found over {trials} trials: {min_cut} (Expected: 2)")
