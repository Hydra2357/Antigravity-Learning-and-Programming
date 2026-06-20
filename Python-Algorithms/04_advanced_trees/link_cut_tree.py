"""
Link-Cut Tree Implementation
A dynamic graph data structure that maintains a forest of trees under edge insertions (link) and deletions (cut).
Uses Splay Trees to represent preferred paths (S-trees).
Time Complexity: O(log N) amortized per operation.
Space Complexity: O(N)
"""

class LCTNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.rev = False  # Reverse propagation lazy flag for path reversals

    def is_root(self):
        """Returns True if this node is the root of its auxiliary tree (Splay Tree)."""
        if self.parent is None:
            return True
        return self.parent.left != self and self.parent.right != self

class LinkCutTree:
    def push_down(self, x):
        """Pushes down lazy propagation flags (like path reversal)."""
        if x and x.rev:
            x.left, x.right = x.right, x.left
            if x.left:
                x.left.rev = not x.left.rev
            if x.right:
                x.right.rev = not x.right.rev
            x.rev = False

    def push_all(self, x):
        """Recursively pushes down all lazy flags from auxiliary tree root to node x."""
        if not x.is_root():
            self.push_all(x.parent)
        self.push_down(x)

    def rotate(self, x):
        y = x.parent
        z = y.parent
        
        # Determine left/right children
        is_left = (y.left == x)
        
        # Update connections
        if is_left:
            y.left = x.right
            if x.right:
                x.right.parent = y
            x.right = y
        else:
            y.right = x.left
            if x.left:
                x.left.parent = y
            x.left = y
            
        y.parent = x
        x.parent = z
        
        if z:
            if z.left == y:
                z.left = x
            elif z.right == y:
                z.right = x

    def splay(self, x):
        """Splays node x to the root of its auxiliary tree."""
        self.push_all(x)
        while not x.is_root():
            y = x.parent
            z = y.parent
            if not y.is_root():
                # Double rotation (Zig-Zig or Zig-Zag)
                if (y.left == x) == (z.left == y):
                    self.rotate(y)
                else:
                    self.rotate(x)
            self.rotate(x)

    def access(self, x):
        """
        Builds a preferred path from the root of the represented tree to node x.
        x becomes the root of its splay tree, and has no right child (no nodes deeper in path).
        """
        last = None
        curr = x
        while curr:
            self.splay(curr)
            curr.right = last  # Preferred child becomes last
            last = curr
            curr = curr.parent
        self.splay(x)
        return last

    def make_root(self, x):
        """Makes node x the root of its represented tree."""
        self.access(x)
        x.rev = not x.rev

    def link(self, x, y):
        """Adds an edge between x and y (makes x parent of y in represented forest)."""
        self.make_root(x)
        self.access(y)
        x.parent = y

    def cut(self, x, y):
        """Removes the edge between x and y."""
        self.make_root(x)
        self.access(y)
        if y.left == x and x.right is None:
            y.left = None
            x.parent = None

    def find_root(self, x):
        """Finds the root of the represented tree containing node x."""
        self.access(x)
        curr = x
        while curr.left:
            self.push_down(curr)
            curr = curr.left
        self.splay(curr)
        return curr

if __name__ == "__main__":
    print("=== Link-Cut Tree Demo ===")
    lct = LinkCutTree()
    
    # Create 5 nodes
    nodes = [LCTNode(i) for i in range(5)]
    
    # Nodes are initially disconnected trees
    print(f"Initially, root of node 1 is: Node {lct.find_root(nodes[1]).val}")
    print(f"Initially, root of node 3 is: Node {lct.find_root(nodes[3]).val}")
    
    # Link node 1 and node 2 (1-2)
    lct.link(nodes[1], nodes[2])
    print(f"Linked 1-2. Root of node 1 is: Node {lct.find_root(nodes[1]).val}")
    print(f"Root of node 2 is: Node {lct.find_root(nodes[2]).val}")
    
    # Link node 2 and node 3 (1-2-3)
    lct.link(nodes[2], nodes[3])
    print(f"Linked 2-3. Root of node 1 is: Node {lct.find_root(nodes[1]).val}")
    print(f"Root of node 3 is: Node {lct.find_root(nodes[3]).val}")
    
    # Cut node 2 and node 3
    lct.cut(nodes[2], nodes[3])
    print(f"Cut edge 2-3. Root of node 1 is: Node {lct.find_root(nodes[1]).val}")
    print(f"Root of node 3 is: Node {lct.find_root(nodes[3]).val}")
