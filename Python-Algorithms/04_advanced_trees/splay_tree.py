"""
Splay Tree Implementation
Self-adjusting binary search tree where recently accessed elements are splayed to the root.
Amortized Time Complexity: O(log N) for search, insert, delete.
Worst-case Time Complexity: O(N) (can be unbalanced temporarily, but self-corrects).
Space Complexity: O(N)
"""

class SplayNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def splay(self, root, key):
        """
        Brings the key to the root if it exists,
        else splays the last accessed node (predecessor or successor).
        """
        if root is None or root.key == key:
            return root

        # Key lies in left subtree
        if root.key > key:
            # Key is not in tree, we are done
            if root.left is None:
                return root

            # Zig-Zig (Left Left)
            if root.left.key > key:
                # First recursively bring key to root of left-left
                root.left.left = self.splay(root.left.left, key)
                # First rotation for root
                root = self.right_rotate(root)
                
            # Zig-Zag (Left Right)
            elif root.left.key < key:
                # Recursively bring key to root of left-right
                root.left.right = self.splay(root.left.right, key)
                # First rotation for root.left
                if root.left.right is not None:
                    root.left = self.left_rotate(root.left)

            # Second rotation for root
            if root.left is None:
                return root
            else:
                return self.right_rotate(root)

        # Key lies in right subtree
        else:
            # Key is not in tree, we are done
            if root.right is None:
                return root

            # Zag-Zig (Right Left)
            if root.right.key > key:
                # Recursively bring key to root of right-left
                root.right.left = self.splay(root.right.left, key)
                # First rotation for root.right
                if root.right.left is not None:
                    root.right = self.right_rotate(root.right)
                    
            # Zag-Zag (Right Right)
            elif root.right.key < key:
                # Recursively bring key to root of right-right
                root.right.right = self.splay(root.right.right, key)
                root = self.left_rotate(root)

            # Second rotation for root
            if root.right is None:
                return root
            else:
                return self.left_rotate(root)

    def search(self, key):
        self.root = self.splay(self.root, key)
        if self.root and self.root.key == key:
            return self.root
        return None

    def insert(self, key):
        if self.root is None:
            self.root = SplayNode(key)
            return

        # Splay the closest node to the root
        self.root = self.splay(self.root, key)

        # If key is already present, do nothing
        if self.root.key == key:
            return

        # Allocate new node
        new_node = SplayNode(key)

        # If root's key is greater, make root as right child
        if self.root.key > key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        # If root's key is smaller, make root as left child
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None

        self.root = new_node

    def in_order(self, root, acc=None):
        if acc is None:
            acc = []
        if root:
            self.in_order(root.left, acc)
            acc.append(root.key)
            self.in_order(root.right, acc)
        return acc

if __name__ == "__main__":
    print("=== Splay Tree Demo ===")
    splay_tree = SplayTree()
    
    insert_keys = [100, 50, 200, 40, 30, 20, 10]
    print(f"Inserting: {insert_keys}")
    for k in insert_keys:
        splay_tree.insert(k)
        
    print(f"In-order Traversal (should be sorted): {splay_tree.in_order(splay_tree.root)}")
    print(f"Current Root (should be last inserted 10): {splay_tree.root.key}")
    
    # Search 30 -> it should get splayed to root
    print("\nSearching for 30...")
    node = splay_tree.search(30)
    if node:
        print(f"Found! Current Root: {splay_tree.root.key}")
    else:
        print("Not Found!")
        
    # Search 50 -> splayed to root
    print("Searching for 50...")
    splay_tree.search(50)
    print(f"Current Root: {splay_tree.root.key}")
