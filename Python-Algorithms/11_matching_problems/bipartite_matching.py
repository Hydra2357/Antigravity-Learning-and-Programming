"""
Hopcroft-Karp Maximum Bipartite Matching Algorithm
Finds the maximum cardinality matching in a bipartite graph.
Bipartite sets: Left set U and Right set V.
Uses BFS to build a layered structure of vertex-disjoint augmenting paths,
then DFS to find maximum number of augmenting paths using that structure.
Time Complexity: O(E * sqrt(V))
Space Complexity: O(V)
"""

from collections import deque

class HopcroftKarp:
    def __init__(self, num_u, num_v):
        """
        num_u: number of vertices in Left set U
        num_v: number of vertices in Right set V
        """
        self.num_u = num_u
        self.num_v = num_v
        # Adjacency list: adj[u] contains vertices of V connected to u
        # Vertices in U are 1 to num_u
        # Vertices in V are 1 to num_v
        self.adj = {u: [] for u in range(1, num_u + 1)}
        
        # match_u[u] stores the matched vertex of V for u in U (0 if unmatched)
        self.match_u = [0] * (num_u + 1)
        # match_v[v] stores the matched vertex of U for v in V (0 if unmatched)
        self.match_v = [0] * (num_v + 1)
        
        # dist[u] stores distance layer from BFS
        self.dist = [0] * (num_u + 1)

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def _bfs(self):
        """
        Builds a layered graph.
        Returns True if there is an augmenting path (path ending at dummy vertex 0).
        """
        queue = deque()
        for u in range(1, self.num_u + 1):
            if self.match_u[u] == 0:
                # Unmatched vertices are at distance 0
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
                
        # Distance to dummy vertex 0 representing unmatched right side
        self.dist[0] = float('inf')
        
        while queue:
            u = queue.popleft()
            
            if self.dist[u] < self.dist[0]:
                for v in self.adj[u]:
                    # If match_v[v] is unmatched, its match is dummy node 0
                    if self.dist[self.match_v[v]] == float('inf'):
                        self.dist[self.match_v[v]] = self.dist[u] + 1
                        queue.append(self.match_v[v])
                        
        return self.dist[0] != float('inf')

    def _dfs(self, u):
        """Finds augmenting paths recursively using DFS."""
        if u != 0:
            for v in self.adj[u]:
                if self.dist[self.match_v[v]] == self.dist[u] + 1:
                    if self._dfs(self.match_v[v]):
                        self.match_u[u] = v
                        self.match_v[v] = u
                        return True
            self.dist[u] = float('inf')
            return False
        return True

    def max_matching(self):
        matching_size = 0
        while self._bfs():
            for u in range(1, self.num_u + 1):
                if self.match_u[u] == 0 and self._dfs(u):
                    matching_size += 1
        return matching_size

if __name__ == "__main__":
    print("=== Hopcroft-Karp Bipartite Matching Demo ===")
    
    # Left partition U has 4 vertices (1 to 4)
    # Right partition V has 4 vertices (1 to 4)
    hk = HopcroftKarp(4, 4)
    hk.add_edge(1, 1)
    hk.add_edge(1, 2)
    hk.add_edge(2, 2)
    hk.add_edge(3, 2)
    hk.add_edge(3, 3)
    hk.add_edge(3, 4)
    hk.add_edge(4, 3)
    
    size = hk.max_matching()
    print(f"Maximum Bipartite Matching size: {size}")
    print("Matches:")
    for u in range(1, hk.num_u + 1):
        if hk.match_u[u] != 0:
            print(f"  Left U {u} <---> Right V {hk.match_u[u]}")
