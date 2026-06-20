"""
Edmonds' Blossom Algorithm for General Matching
Finds a maximum cardinality matching in any undirected graph.
Crux: Finds augmenting paths by handling odd cycles ("blossoms") which are contracted
into a single super-vertex when found, and expanded back after finding the path.
Time Complexity: O(V^3) or O(V^2 * E) depending on implementation details.
Space Complexity: O(V)
"""

from collections import deque

class BlossomAlgorithm:
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.adj = {i: [] for i in range(num_vertices)}
        self.match = [-1] * num_vertices

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def _find_lca(self, parent, match, base, u, v):
        """Finds Least Common Ancestor in the forest structure."""
        in_path = [False] * self.v
        while True:
            u = base[u]
            in_path[u] = True
            if match[u] == -1:
                break
            u = parent[match[u]]
            
        while True:
            v = base[v]
            if in_path[v]:
                return v
            v = parent[match[v]]

    def _mark_blossom(self, parent, base, blossom_base, u, v, queue):
        """Contracting the odd-length cycle (blossom) into a single base vertex."""
        while base[u] != blossom_base:
            parent[u] = v
            v = match = self.match[u]
            if base[match] != blossom_base:
                queue.append(match)
            if base[u] == u:
                base[u] = blossom_base
            if base[match] == match:
                base[match] = blossom_base
            u = parent[match]

    def _find_augmenting_path(self, start):
        """Searches for an augmenting path starting from node 'start'."""
        parent = [-1] * self.v
        base = list(range(self.v))
        visited = [False] * self.v
        
        queue = deque([start])
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            
            for v in self.adj[u]:
                if base[u] == base[v] or self.match[u] == v:
                    continue
                    
                # If we found an odd cycle (blossom)
                if (v == start or (self.match[v] != -1 and parent[self.match[v]] != -1)):
                    blossom_base = self._find_lca(parent, self.match, base, u, v)
                    
                    # Contract blossom
                    self._mark_blossom(parent, base, blossom_base, u, v, queue)
                    self._mark_blossom(parent, base, blossom_base, v, u, queue)
                    
                    # Update base representatives for all contracted nodes
                    for i in range(self.v):
                        if base[base[i]] == blossom_base:
                            base[i] = blossom_base
                elif parent[v] == -1:
                    # Unvisited node found
                    parent[v] = u
                    if self.match[v] == -1:
                        # Augmenting path found!
                        # Backtrack to update matchings
                        curr = v
                        while curr != -1:
                            p = parent[curr]
                            nxt = self.match[p]
                            self.match[curr] = p
                            self.match[p] = curr
                            curr = nxt
                        return True
                    else:
                        # Node is matched, extend forest
                        visited[self.match[v]] = True
                        parent[self.match[v]] = v
                        queue.append(self.match[v])
                        
        return False

    def max_matching(self):
        matching_size = 0
        for i in range(self.v):
            if self.match[i] == -1:
                if self._find_augmenting_path(i):
                    matching_size += 1
        return matching_size

if __name__ == "__main__":
    print("=== Edmonds' Blossom Algorithm Demo ===")
    
    # Create general graph
    # 4-cycle with diagonal (has odd cycles/blossoms)
    # vertices: 0, 1, 2, 3
    # edges: (0-1), (1-2), (2-3), (3-0), (0-2)
    blossom = BlossomAlgorithm(4)
    blossom.add_edge(0, 1)
    blossom.add_edge(1, 2)
    blossom.add_edge(2, 3)
    blossom.add_edge(3, 0)
    blossom.add_edge(0, 2)
    
    size = blossom.max_matching()
    print(f"Maximum Matching size in general graph: {size} (Expected: 2)")
    print("Matches:")
    for i in range(blossom.v):
        if blossom.match[i] > i:
            print(f"  Node {i} <---> Node {blossom.match[i]}")
