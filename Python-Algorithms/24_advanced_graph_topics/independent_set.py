"""
Maximum Independent Set Solver
An independent set is a set of vertices in a graph, no two of which are adjacent.
Finding the Maximum Independent Set (MIS) is a classical NP-Hard problem.
This script implements a backtracking solver to find the exact Maximum Independent Set.
Time Complexity: O(2^V) worst-case.
Space Complexity: O(V) recursion depth.
"""

class MaxIndependentSet:
    def __init__(self, num_vertices, edges):
        self.v = num_vertices
        self.adj = {i: set() for i in range(num_vertices)}
        for u, v in edges:
            self.adj[u].add(v)
            self.adj[v].add(u)
            
        self.max_set = []

    def solve(self):
        """Solves for MIS and returns it."""
        self.max_set = []
        self._backtrack(0, [], set())
        return self.max_set

    def _backtrack(self, node, current_set, forbidden_nodes):
        """
        node: current vertex under consideration.
        current_set: list of vertices selected so far.
        forbidden_nodes: set of nodes adjacent to selected vertices.
        """
        # If we checked all nodes, update max if current is larger
        if node == self.v:
            if len(current_set) > len(self.max_set):
                self.max_set = list(current_set)
            return

        # Pruning optimization: if the remaining nodes plus current set size
        # is less than max found so far, prune the branch.
        if len(current_set) + (self.v - node) <= len(self.max_set):
            return

        # Branch 1: Exclude the current node
        self._backtrack(node + 1, current_set, forbidden_nodes)

        # Branch 2: Include the current node (if it is not forbidden)
        if node not in forbidden_nodes:
            current_set.append(node)
            # Add node's neighbors to forbidden set for this branch
            new_forbidden = forbidden_nodes.union(self.adj[node])
            
            self._backtrack(node + 1, current_set, new_forbidden)
            
            current_set.pop()

if __name__ == "__main__":
    print("=== Maximum Independent Set Solver ===")
    
    # Graph structure:
    # 0 - 1 - 2
    # |       |
    # 3 - - - 4
    # Edges: (0-1), (1-2), (0-3), (2-4), (3-4)
    # The max independent set is {0, 2} or {1, 3} or {1, 4} (size 2),
    # or {0, 2, 3}? Wait, 0 is adjacent to 3. What about {1, 3, 4}? No, 3 is adjacent to 4.
    # What about {0, 2, 3}? 0 adjacent to 3.
    # Let's see what the solver finds.
    edges = [
        (0, 1),
        (1, 2),
        (0, 3),
        (2, 4),
        (3, 4)
    ]
    num_vertices = 5
    
    mis = MaxIndependentSet(num_vertices, edges)
    max_set = mis.solve()
    
    print(f"Graph Edges: {edges}")
    print(f"Maximum Independent Set: {max_set} (Size: {len(max_set)})")
