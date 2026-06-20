"""
Maximum Cut (Max-Cut) Heuristics
Max-Cut Problem: Partition vertices of a graph into two sets S and T such that
the weight/number of edges crossing between S and T is maximized.
This problem is NP-Hard.
Includes:
1. Randomized 0.5-Approximation:
   - Assigns each node to S or T with probability 0.5.
   - Expected cut size is >= 0.5 * OPT.
2. Local Search Improvement:
   - Starts with a partition. If moving a vertex from S to T (or T to S)
     increases the cut size, we move it. Repeat until no single-node move improves the cut.
"""

import random

class MaxCutHeuristics:
    def __init__(self, num_vertices, edges):
        self.v = num_vertices
        self.edges = edges
        # Build adjacency list
        self.adj = {i: set() for i in range(num_vertices)}
        for u, v in edges:
            self.adj[u].add(v)
            self.adj[v].add(u)

    def calculate_cut_size(self, partition):
        """partition: set of vertices in S. T is V - S."""
        cut_size = 0
        for u, v in self.edges:
            # Check if edge crosses the partition
            if (u in partition and v not in partition) or (u not in partition and v in partition):
                cut_size += 1
        return cut_size

    def randomized_approx(self):
        """Randomly assigns each node to S or T with 0.5 probability."""
        S = set()
        for i in range(self.v):
            if random.random() < 0.5:
                S.add(i)
        return S

    def local_search(self, initial_S=None):
        """
        Improves a partition S using local search.
        Swaps nodes if doing so increases the cut size.
        """
        if initial_S is None:
            S = self.randomized_approx()
        else:
            S = set(initial_S)
            
        improved = True
        while improved:
            improved = False
            for u in range(self.v):
                # Count neighbors in S and T
                neighbors_in_S = len(self.adj[u].intersection(S))
                neighbors_in_T = len(self.adj[u]) - neighbors_in_S
                
                if u in S:
                    # If we move u to T, the cut changes:
                    # We lose edges from u to neighbors in T (cut edges)
                    # We gain edges from u to neighbors in S (new cut edges)
                    # Net change: neighbors_in_S - neighbors_in_T
                    if neighbors_in_S > neighbors_in_T:
                        S.remove(u)
                        improved = True
                        break  # restart search
                else:
                    # If we move u to S:
                    if neighbors_in_T > neighbors_in_S:
                        S.add(u)
                        improved = True
                        break
                        
        return S

if __name__ == "__main__":
    print("=== Max-Cut Heuristics Demo ===")
    
    # 5-vertex cycle graph (C5)
    # Max cut of C5 is 4 (e.g. partition {0, 2} and {1, 3, 4})
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 0)
    ]
    num_vertices = 5
    
    mc = MaxCutHeuristics(num_vertices, edges)
    
    # Run randomized approx
    random.seed(42)
    rand_S = mc.randomized_approx()
    rand_size = mc.calculate_cut_size(rand_S)
    print(f"Randomized 0.5-Approx Cut: S={rand_S} | size={rand_size}")
    
    # Run local search starting from the random cut
    local_S = mc.local_search(rand_S)
    local_size = mc.calculate_cut_size(local_S)
    print(f"Local Search Improved Cut: S={local_S} | size={local_size} (Expected: 4)")
