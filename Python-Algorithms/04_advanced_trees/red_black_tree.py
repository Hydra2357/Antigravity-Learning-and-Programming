"""
Red-Black Tree Implementation
A self-balancing binary search tree where each node has a color (Red or Black).
Guarantees O(log N) search, insertion, and deletion.
Properties:
1. Every node is either red or black.
2. The root is black.
3. Every leaf (NIL) is black.
4. If a node is red, both its children are black.
5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.
"""

RED = True
BLACK = False

class RBNode:
    def __init__(self, key, color=RED):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        # NIL node representing leaves
        self.NIL = RBNode(None, color=BLACK)
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
            
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
            
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
            
        x.right = y
        y.parent = x

    def insert(self, key):
        node = RBNode(key, color=RED)
        node.left = self.NIL
        node.right = self.NIL
        
        y = None
        x = self.root
        
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
                
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
            
        if node.parent is None:
            node.color = BLACK
            return
            
        if node.parent.parent is None:
            return
            
        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle node
                if u.color == RED:
                    # Case 1: Uncle is RED -> recolor parent, uncle, grandparent
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    # Case 2: Uncle is BLACK, k is left child -> Right rotate on parent
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    # Case 3: Uncle is BLACK, k is right child -> Left rotate on grandparent
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # Uncle node
                if u.color == RED:
                    # Case 1 (Mirror)
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    # Case 2 (Mirror)
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    # Case 3 (Mirror)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.right_rotate(k.parent.parent)
                    
            if k == self.root:
                break
        self.root.color = BLACK

    def in_order_traverse(self, node, acc=None):
        if acc is None:
            acc = []
        if node != self.NIL:
            self.in_order_traverse(node.left, acc)
            color_str = "RED" if node.color == RED else "BLACK"
            acc.append((node.key, color_str))
            self.in_order_traverse(node.right, acc)
        return acc

if __name__ == "__main__":
    print("=== Red-Black Tree Demo ===")
    rbt = RedBlackTree()
    
    insert_keys = [8, 18, 5, 15, 17, 25, 40, 80]
    print(f"Inserting keys: {insert_keys}")
    for k in insert_keys:
        rbt.insert(k)
        
    res = rbt.in_order_traverse(rbt.root)
    print("In-order Traversal (Key, Color):")
    for key, color in res:
        print(f"  - {key}: {color}")
        
    print(f"\nRoot Key: {rbt.root.key} (Color: {'RED' if rbt.root.color == RED else 'BLACK'})")
