"""
AVL Tree Implementation
Self-balancing Binary Search Tree (BST) where the height difference of left and right subtrees (balance factor) is at most 1.
Time Complexities:
    - Search: O(log N)
    - Insertion: O(log N)
    - Deletion: O(log N)
Space Complexity: O(N)
"""

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        
        return y

    def insert(self, root, key):
        # 1. Perform standard BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
            
        # 2. Update height of this ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # 3. Get balance factor to check if it became unbalanced
        balance = self.get_balance(root)
        
        # 4. If node is unbalanced, try 4 cases:
        
        # Case 1 - Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
            
        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
            
        # Case 3 - Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
            
        # Case 4 - Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
            
        return root

    def pre_order(self, root, acc=None):
        if acc is None:
            acc = []
        if root:
            acc.append(root.key)
            self.pre_order(root.left, acc)
            self.pre_order(root.right, acc)
        return acc

    def in_order(self, root, acc=None):
        if acc is None:
            acc = []
        if root:
            self.in_order(root.left, acc)
            acc.append(root.key)
            self.in_order(root.right, acc)
        return acc

if __name__ == "__main__":
    print("=== AVL Tree Demo ===")
    tree = AVLTree()
    root = None
    
    # Constructing tree by inserting keys
    keys = [10, 20, 30, 40, 50, 25]
    print(f"Inserting keys: {keys}")
    
    for key in keys:
        root = tree.insert(root, key)
        
    print(f"Pre-order Traversal: {tree.pre_order(root)}")
    print(f"In-order Traversal (should be sorted): {tree.in_order(root)}")
    
    # Root should be 20 or 30 due to self-balancing rotations
    print(f"Balanced Root Key: {root.key}")
