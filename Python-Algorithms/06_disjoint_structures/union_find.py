"""
Union-Find / Disjoint Set Union (DSU)
Data structure that tracks elements partitioned into disjoint subsets.
Optimizations:
1. Path Compression: Flattens the tree structure during find operations, making future finds extremely fast.
2. Union by Rank/Size: Attaches the smaller tree to the root of the larger tree to keep the tree shallow.
Time Complexity: O(alpha(N)) amortized per operation, where alpha is the Inverse Ackermann function (practically constant O(1)).
Space Complexity: O(N)
"""

class UnionFind:
    def __init__(self, size):
        # Initialize parent of each node to itself, and rank/size arrays
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = [1] * size
        self.num_components = size

    def find(self, i):
        """
        Finds the representative of the set containing element i.
        Includes Path Compression.
        """
        if self.parent[i] == i:
            return i
        # Path compression step: point node directly to set representative
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union_by_rank(self, i, j):
        """
        Unites sets containing elements i and j based on rank (depth).
        Returns True if a merge happened, False if they were already in the same set.
        """
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i == root_j:
            return False
            
        # Union by rank: attach smaller tree under larger tree
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
        else:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.rank[root_i] += 1
            
        self.num_components -= 1
        return True

    def union_by_size(self, i, j):
        """
        Unites sets containing elements i and j based on size.
        Returns True if a merge happened, False if they were already in the same set.
        """
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i == root_j:
            return False
            
        # Union by size: attach smaller size tree under larger size tree
        if self.size[root_i] < self.size[root_j]:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        else:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            
        self.num_components -= 1
        return True

    def is_connected(self, i, j):
        """Returns True if elements i and j belong to the same set."""
        return self.find(i) == self.find(j)

if __name__ == "__main__":
    print("=== Disjoint Set Union (DSU) Demo ===")
    
    n = 6
    dsu = UnionFind(n)
    print(f"Created DSU with {n} elements (0 to {n-1})")
    print(f"Initial components count: {dsu.num_components}")
    
    # Perform unions
    dsu.union_by_rank(0, 1)
    dsu.union_by_rank(1, 2)
    dsu.union_by_rank(3, 4)
    
    print("\nAfter union(0,1), union(1,2), union(3,4):")
    print(f"Is 0 connected to 2? {dsu.is_connected(0, 2)} (Expected: True)")
    print(f"Is 0 connected to 3? {dsu.is_connected(0, 3)} (Expected: False)")
    print(f"Components count: {dsu.num_components} (Expected: 3 -> {{0,1,2}}, {{3,4}}, {{5}})")
    
    dsu.union_by_size(2, 4)
    print("\nAfter union(2,4):")
    print(f"Is 0 connected to 3? {dsu.is_connected(0, 3)} (Expected: True)")
    print(f"Representative of 3: {dsu.find(3)}")
    print(f"Representative of 0: {dsu.find(0)}")
    print(f"Components count: {dsu.num_components} (Expected: 2)")
