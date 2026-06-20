"""
Dynamic Programming on Trees (Tree DP)
Finds the Maximum Weight Independent Set on a Tree.
Independent Set: A subset of vertices in a graph such that no two vertices are adjacent.
For a tree with vertex weights, we find an independent set with the maximum total weight.
Time Complexity: O(N) where N is the number of nodes.
Space Complexity: O(N) recursion stack and DP tables.
"""

class TreeNode:
    def __init__(self, val, weight=1):
        self.val = val
        self.weight = weight
        self.neighbors = []

def max_weight_independent_set(root):
    """
    Solves MWIS on a tree.
    Returns: (max_weight, set_members)
    """
    # dp[u][0] = max weight in subtree of u if u is NOT included
    # dp[u][1] = max weight in subtree of u if u IS included
    dp = {}
    
    # Track selected vertices for path reconstruction
    selected = set()
    
    def dfs(u, parent):
        dp[u] = [0, u.weight]
        
        for neighbor in u.neighbors:
            if neighbor != parent:
                dfs(neighbor, u)
                # If u is not included, neighbors can be either included or excluded
                dp[u][0] += max(dp[neighbor][0], dp[neighbor][1])
                # If u is included, neighbors MUST be excluded
                dp[u][1] += dp[neighbor][0]
                
    # Step 1: Compute DP values
    dfs(root, None)
    
    # Step 2: Reconstruct selection
    def reconstruct(u, parent, parent_included):
        if parent_included:
            # If parent was included, u cannot be included
            for neighbor in u.neighbors:
                if neighbor != parent:
                    reconstruct(neighbor, u, False)
        else:
            # If parent was not included, we make greedy choice for u
            if dp[u][1] > dp[u][0]:
                selected.add(u.val)
                for neighbor in u.neighbors:
                    if neighbor != parent:
                        reconstruct(neighbor, u, True)
            else:
                for neighbor in u.neighbors:
                    if neighbor != parent:
                        reconstruct(neighbor, u, False)
                        
    reconstruct(root, None, False)
    
    max_weight = max(dp[root][0], dp[root][1])
    return max_weight, selected

if __name__ == "__main__":
    print("=== Dynamic Programming on Trees Demo ===")
    
    # Build a tree:
    #      0 (wt: 5)
    #     / \
    #    1   2 (wt: 10, 100)
    #   /
    #  3 (wt: 50)
    nodes = {
        0: TreeNode(0, 5),
        1: TreeNode(1, 10),
        2: TreeNode(2, 100),
        3: TreeNode(3, 50)
    }
    
    # Connect tree edges
    nodes[0].neighbors.append(nodes[1])
    nodes[1].neighbors.append(nodes[0])
    
    nodes[0].neighbors.append(nodes[2])
    nodes[2].neighbors.append(nodes[0])
    
    nodes[1].neighbors.append(nodes[3])
    nodes[3].neighbors.append(nodes[1])
    
    print("Tree structure:")
    print("  Node 0 (wt 5) linked to Node 1 (wt 10) and Node 2 (wt 100)")
    print("  Node 1 (wt 10) linked to Node 3 (wt 50)")
    
    max_wt, members = max_weight_independent_set(nodes[0])
    print(f"\nMaximum Weight Independent Set Weight: {max_wt} (Expected: 150)")
    print(f"Selected Nodes: {members} (Expected: {{2, 3}} because 2 and 3 are not adjacent and weight 100+50=150)")
