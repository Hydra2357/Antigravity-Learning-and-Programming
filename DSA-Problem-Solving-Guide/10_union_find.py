"""
Pattern 10: Union Find (Disjoint Set Union)
=============================================
Use when: Need to group elements, find connected components, detect cycles.
Time:  O(alpha(n)) per operation ≈ O(1)   Space: O(n)

Problems: Number of Connected Components, Redundant Connection,
          Accounts Merge, Satisfiability of Equality Equations,
          Most Stones Removed, Friend Circles
"""


# ── Core Union-Find Class ────────────────────────────────────────────────────
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        """Find root with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank. Returns False if already connected."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# ── Example 1: Number of Connected Components ────────────────────────────────
def count_components(n, edges):
    """Count connected components in undirected graph. O(E * alpha(n))"""
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.components


# ── Example 2: Redundant Connection (Cycle Detection) ───────────────────────
def find_redundant_connection(edges):
    """Find the edge that creates a cycle in the graph. O(E * alpha(n))"""
    n = len(edges)
    uf = UnionFind(n + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]
    return []


# ── Example 3: Accounts Merge ────────────────────────────────────────────────
def accounts_merge(accounts):
    """Merge accounts sharing a common email. O(N * alpha(N))"""
    email_to_id = {}
    uf = UnionFind(len(accounts))

    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_id:
                uf.union(i, email_to_id[email])
            else:
                email_to_id[email] = i

    # Group emails by root
    from collections import defaultdict
    groups = defaultdict(set)
    for email, idx in email_to_id.items():
        groups[uf.find(idx)].add(email)

    result = []
    for root, emails in groups.items():
        name = accounts[root][0]
        result.append([name] + sorted(emails))
    return result


# ── Example 4: Detect Cycle in Undirected Graph ──────────────────────────────
def has_cycle(n, edges):
    """Return True if graph contains a cycle. O(E * alpha(n))"""
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return True
    return False


# ── Example 5: Most Stones Removed ───────────────────────────────────────────
def remove_stones(stones):
    """Max stones removable (stone removable if shares row or col). O(n)"""
    uf = UnionFind(20001)
    for r, c in stones:
        uf.union(r, c + 10000)   # offset cols to avoid collision
    roots = {uf.find(r) for r, c in stones} | {uf.find(c + 10000) for r, c in stones}
    # stones - unique islands = removable stones
    unique_components = len({uf.find(r) for r, _ in stones})
    return len(stones) - unique_components


if __name__ == "__main__":
    print("=== Union Find Demo ===\n")

    print("Components n=5 edges=[[0,1],[1,2],[3,4]] →",
          count_components(5, [[0,1],[1,2],[3,4]]))

    edges = [[1,2],[1,3],[2,3]]
    print("Redundant Connection →", find_redundant_connection(edges))

    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                ["John","johnsmith@mail.com","john00@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]]
    merged = accounts_merge(accounts)
    print("Accounts Merge (count) →", len(merged), "groups")

    print("Has Cycle n=4 [[0,1],[1,2],[2,0]] →",
          has_cycle(4, [[0,1],[1,2],[2,0]]))

    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print("Max Stones Removed →", remove_stones(stones))
