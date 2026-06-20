"""
B-Tree Implementation
A self-balancing search tree where nodes can have multiple keys and children.
Optimized for systems that read/write large blocks of data.
For minimum degree t:
- Every node except root must have at least t-1 keys.
- Every node can have at most 2t-1 keys.
- A non-leaf node with n keys has n+1 children.
Time Complexity: O(log N) for search, insert, delete.
"""

class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Minimum degree

    def search(self, k, x=None):
        """Searches for key k in the subtree. Returns (node, index) if found, else None."""
        if x is None:
            x = self.root
            
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
            
        if i < len(x.keys) and k == x.keys[i]:
            return x, i
            
        if x.leaf:
            return None
        else:
            return self.search(k, x.child[i])

    def insert(self, k):
        root = self.root
        # If root is full, tree grows in height
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(False)
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0, root)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            # Insert key in sorted order
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            # Find child which is going to have the key
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i, x.child[i])
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i, y):
        """
        Splits the child y of node x at index i.
        """
        t = self.t
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        
        # z gets the second half of y's keys and children
        z.keys = y.keys[t : (2 * t) - 1]
        y.keys = y.keys[0 : t - 1]
        
        if not y.leaf:
            z.child = y.child[t : 2 * t]
            y.child = y.child[0 : t]

    def in_order_traverse(self, x=None, acc=None):
        if acc is None:
            acc = []
        if x is None:
            x = self.root
            
        for i in range(len(x.keys)):
            if not x.leaf:
                self.in_order_traverse(x.child[i], acc)
            acc.append(x.keys[i])
            
        if not x.leaf:
            self.in_order_traverse(x.child[-1], acc)
            
        return acc

if __name__ == "__main__":
    print("=== B-Tree Demo ===")
    # Create a B-Tree with minimum degree t = 3
    # Max keys per node = 2t - 1 = 5
    # Min keys per node = t - 1 = 2 (except root)
    btree = BTree(t=3)
    
    insert_keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 4, 8, 12]
    print(f"Inserting keys: {insert_keys}")
    for key in insert_keys:
        btree.insert(key)
        
    in_order = btree.in_order_traverse()
    print(f"In-order Traversal (should be sorted): {in_order}")
    
    # Search tests
    for s_key in [40, 99]:
        result = btree.search(s_key)
        if result:
            print(f"Search for {s_key}: Found!")
        else:
            print(f"Search for {s_key}: Not Found")
