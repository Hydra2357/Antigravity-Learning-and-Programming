"""
Ford-Fulkerson Maximum Flow Algorithm
Computes the maximum flow from a source s to a sink t in a flow network.
Uses Depth-First Search (DFS) to find augmenting paths in the residual network.
Time Complexity: O(E * f) where f is the maximum flow value.
Space Complexity: O(V) for the DFS recursion stack.
"""

class FordFulkerson:
    def __init__(self, size):
        self.size = size
        # Residual graph: residual_graph[u][v] represents capacity of edge u -> v
        self.residual_graph = [[0] * size for _ in range(size)]

    def add_edge(self, u, v, capacity):
        self.residual_graph[u][v] = capacity

    def _dfs(self, s, t, visited, path):
        """Finds an augmenting path from s to t using DFS."""
        if s == t:
            return True
            
        visited.add(s)
        for v in range(self.size):
            # Check if there is capacity available and neighbor is not visited
            if v not in visited and self.residual_graph[s][v] > 0:
                path[v] = s
                if self._dfs(v, t, visited, path):
                    return True
        return False

    def max_flow(self, source, sink):
        # Store parent nodes of vertices in the path
        path = [-1] * self.size
        max_flow_val = 0
        
        # While there exists an augmenting path from source to sink
        while True:
            visited = set()
            if not self._dfs(source, sink, visited, path):
                break  # No more augmenting paths
                
            # Find the bottleneck capacity along the path found by DFS
            bottleneck = float('inf')
            v = sink
            while v != source:
                u = path[v]
                bottleneck = min(bottleneck, self.residual_graph[u][v])
                v = u
                
            # Update residual capacities of the edges and reverse edges
            v = sink
            while v != source:
                u = path[v]
                self.residual_graph[u][v] -= bottleneck
                self.residual_graph[v][u] += bottleneck
                v = u
                
            max_flow_val += bottleneck
            
        return max_flow_val

if __name__ == "__main__":
    print("=== Ford-Fulkerson Algorithm Demo ===")
    
    # 6 vertices flow network:
    # 0: Source (s)
    # 5: Sink (t)
    ff = FordFulkerson(6)
    ff.add_edge(0, 1, 16)
    ff.add_edge(0, 2, 13)
    ff.add_edge(1, 2, 10)
    ff.add_edge(1, 3, 12)
    ff.add_edge(2, 1, 4)
    ff.add_edge(2, 4, 14)
    ff.add_edge(3, 2, 9)
    ff.add_edge(3, 5, 20)
    ff.add_edge(4, 3, 7)
    ff.add_edge(4, 5, 4)
    
    source = 0
    sink = 5
    max_flow = ff.max_flow(source, sink)
    print(f"Maximum Flow from {source} to {sink}: {max_flow} (Expected: 23)")
