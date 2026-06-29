"""
Dynamic Programming on Trees (Tree DP)
========================================
Finds the Maximum Weight Independent Set on a Tree.
Independent Set: A subset of vertices such that no two are adjacent.
For a tree with vertex weights, find an independent set with max total weight.

Use when: Problem has optimal substructure on a tree structure.
Time:  O(N)   Space: O(N) recursion stack + DP tables

Problems: Max Weight Independent Set, House Robber III,
          Diameter of Binary Tree, Binary Tree Cameras
"""


class TreeNode:
    def __init__(self, val, weight=1):
        self.val = val
        self.weight = weight
        self.neighbors = []


def max_weight_independent_set(root):
    """
    Solves MWIS on a tree.
    dp[u][0] = max weight in subtree of u if u is NOT included
    dp[u][1] = max weight in subtree of u if u IS included
    Returns: (max_weight, set_members)
    """
    dp = {}
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
            # If parent was not included, make greedy choice for u
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


# ── Example 2: House Robber III (LeetCode 337) ───────────────────────────────
class BinaryNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob_tree(root):
    """
    Max money from binary tree where you cannot rob adjacent nodes.
    Returns (rob_root, skip_root) for each subtree.
    Time: O(n)
    """
    def dfs(node):
        if not node:
            return (0, 0)   # (rob_this, skip_this)
        left_rob, left_skip = dfs(node.left)
        right_rob, right_skip = dfs(node.right)
        rob_this = node.val + left_skip + right_skip
        skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)
        return (rob_this, skip_this)

    return max(dfs(root))


# ── Example 3: Diameter of Binary Tree ──────────────────────────────────────
def diameter_of_binary_tree(root):
    """
    Longest path between any two nodes in binary tree.
    Time: O(n)
    """
    diameter = [0]

    def depth(node):
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter[0] = max(diameter[0], left + right)
        return 1 + max(left, right)

    depth(root)
    return diameter[0]


if __name__ == "__main__":
    print("=== Tree DP Demo ===\n")

    # Build tree:
    #      0 (wt: 5)
    #     / \
    #    1   2  (wt: 10, 100)
    #   /
    #  3  (wt: 50)
    nodes = {
        0: TreeNode(0, 5),
        1: TreeNode(1, 10),
        2: TreeNode(2, 100),
        3: TreeNode(3, 50)
    }
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
    print(f"Max Weight Independent Set: {max_wt}  Nodes: {members}")
    print("  (Expected: 150, nodes {2, 3} since 100+50=150 and not adjacent)\n")

    # House Robber III: [3, 2, 3, null, 3, null, 1]
    tree = BinaryNode(3,
                      BinaryNode(2, None, BinaryNode(3)),
                      BinaryNode(3, None, BinaryNode(1)))
    print("House Robber III [3,2,3,null,3,null,1] →", rob_tree(tree), "(Expected: 7)")

    # Diameter: [1, 2, 3, 4, 5]
    dtree = BinaryNode(1,
                       BinaryNode(2, BinaryNode(4), BinaryNode(5)),
                       BinaryNode(3))
    print("Diameter of Binary Tree →", diameter_of_binary_tree(dtree), "(Expected: 3)")
