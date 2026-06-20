"""
Edmonds-Karp Maximum Flow Algorithm
Computes the maximum flow from a source s to a sink t in a flow network.
Edmonds-Karp is an implementation of the Ford-Fulkerson method that uses BFS to find augmenting paths.
Guarantees polynomial runtime by picking the shortest augmenting path first.
Time Complexity: O(V * E^2)
Space Complexity: O(V) for BFS queue and parent list.
"""

from collections import deque

class EdmondsKarp:
    def __init__(self, size):
        self.size = size
        self.residual_graph = [[0] * size for _ in range(size)]

    def add_edge(self, u, v, capacity):
        self.residual_graph[u][v] = capacity

    def _bfs(self, s, t, parent):
        """Finds an augmenting path using BFS. Stores parents of nodes in parent list."""
        visited = [False] * self.size
        queue = deque([s])
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            
            for v in range(self.size):
                # If neighbor v is not visited and edge u -> v has capacity in residual graph
                if not visited[v] and self.residual_graph[u][v] > 0:
                    queue.append(v)
                    parent[v] = u
                    visited[v] = True
                    if v == t:
                        return True
                        
        return False

    def max_flow(self, source, sink):
        parent = [-1] * self.size
        max_flow_val = 0
        
        # While a shortest augmenting path exists
        while self._bfs(source, sink, parent):
            # Find bottleneck capacity along path
            bottleneck = float('inf')
            v = sink
            while v != source:
                u = parent[v]
                bottleneck = min(bottleneck, self.residual_graph[u][v])
                v = u
                
            # Update residual graph capacities
            v = sink
            while v != source:
                u = parent[v]
                self.residual_graph[u][v] -= bottleneck
                self.residual_graph[v][u] += bottleneck
                v = u
                
            max_flow_val += bottleneck
            
        return max_flow_val

if __name__ == "__main__":
    print("=== Edmonds-Karp Algorithm Demo ===")
    
    # 6 vertices flow network:
    # 0: Source (s)
    # 5: Sink (t)
    ek = EdmondsKarp(6)
    ek.add_edge(0, 1, 16)
    ek.add_edge(0, 2, 13)
    ek.add_edge(1, 2, 10)
    ek.add_edge(1, 3, 12)
    ek.add_edge(2, 1, 4)
    ek.add_edge(2, 4, 14)
    ek.add_edge(3, 2, 9)
    ek.add_edge(3, 5, 20)
    ff_expected = 23
    ek.add_edge(4, 3, 7)
    ek.add_edge(4, 5, 4)
    
    source = 0
    sink = 5
    max_flow = ek.max_flow(source, sink)
    print(f"Maximum Flow from {source} to {sink}: {max_flow} (Expected: {ff_expected})")
