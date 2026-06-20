"""
Fibonacci Heap Implementation
A mergeable heap structure.
Amortized Time Complexities:
    - Insert: O(1)
    - Minimum: O(1)
    - Union (Merge): O(1)
    - Extract Min: O(log N)
    - Decrease Key: O(1)
    - Delete: O(log N)
Space Complexity: O(N)
"""

import math

class FibNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.n = 0

    def insert(self, key):
        """Inserts a new key. O(1) amortized."""
        node = FibNode(key)
        if self.min_node is None:
            self.min_node = node
        else:
            # Insert node into root list
            self._add_to_root_list(node)
            if node.key < self.min_node.key:
                self.min_node = node
        self.n += 1
        return node

    def get_min(self):
        """Returns min key node. O(1) amortized."""
        return self.min_node

    def union(self, other_heap):
        """Merges two Fibonacci Heaps. O(1) amortized."""
        if not other_heap.min_node:
            return
        if not self.min_node:
            self.min_node = other_heap.min_node
            self.n = other_heap.n
            return
            
        # Cat and merge the root lists
        l1 = self.min_node.left
        r2 = other_heap.min_node.right
        
        self.min_node.left = other_heap.min_node
        other_heap.min_node.right = self.min_node
        
        l1.right = r2
        r2.left = l1
        
        if other_heap.min_node.key < self.min_node.key:
            self.min_node = other_heap.min_node
        self.n += other_heap.n

    def extract_min(self):
        """Extracts the minimum node. O(log N) amortized."""
        z = self.min_node
        if z is not None:
            # Add all children of z to the root list
            if z.child is not None:
                children = self._get_nodes_in_list(z.child)
                for child in children:
                    self._add_to_root_list(child)
                    child.parent = None
            
            # Remove z from root list
            self._remove_from_root_list(z)
            
            if z == z.right:
                self.min_node = None
            else:
                self.min_node = z.right
                self.consolidate()
            self.n -= 1
        return z

    def decrease_key(self, x, k):
        """Decreases key of x to k. O(1) amortized."""
        if k > x.key:
            raise ValueError("New key is greater than current key")
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self.cut(x, y)
            self.cascading_cut(y)
        if x.key < self.min_node.key:
            self.min_node = x

    def cut(self, x, y):
        """Cuts the link between child x and parent y, making x a root."""
        # Remove x from child list of y
        if x == x.right:
            y.child = None
        else:
            x.left.right = x.right
            x.right.left = x.left
            if y.child == x:
                y.child = x.right
        y.degree -= 1
        # Add x to root list
        self._add_to_root_list(x)
        x.parent = None
        x.mark = False

    def cascading_cut(self, y):
        """Performs cascading cuts on ancestor y."""
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)

    def consolidate(self):
        """Consolidates roots of equal degree. Runs during extract_min."""
        max_deg = int(math.log2(self.n)) + 2 if self.n > 0 else 2
        A = [None] * max_deg
        
        roots = self._get_nodes_in_list(self.min_node)
        for w in roots:
            x = w
            d = x.degree
            while d < len(A) and A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self.fib_link(y, x)
                A[d] = None
                d += 1
            if d < len(A):
                A[d] = x
            
        self.min_node = None
        for i in range(len(A)):
            if A[i] is not None:
                if self.min_node is None:
                    self.min_node = A[i]
                    A[i].left = A[i]
                    A[i].right = A[i]
                else:
                    self._add_to_root_list(A[i])
                    if A[i].key < self.min_node.key:
                        self.min_node = A[i]

    def fib_link(self, y, x):
        """Links root y as a child of root x."""
        # Remove y from root list
        y.left.right = y.right
        y.right.left = y.left
        # Make y child of x
        y.parent = x
        if x.child is None:
            x.child = y
            y.left = y
            y.right = y
        else:
            y.right = x.child
            y.left = x.child.left
            x.child.left.right = y
            x.child.left = y
        x.degree += 1
        y.mark = False

    def _add_to_root_list(self, node):
        node.parent = None
        node.right = self.min_node
        node.left = self.min_node.left
        self.min_node.left.right = node
        self.min_node.left = node

    def _remove_from_root_list(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def _get_nodes_in_list(self, start):
        nodes = []
        if not start:
            return nodes
        curr = start
        while True:
            nodes.append(curr)
            curr = curr.right
            if curr == start:
                break
        return nodes

if __name__ == "__main__":
    print("=== Fibonacci Heap Demo ===")
    heap = FibonacciHeap()
    
    insert_keys = [8, 18, 5, 15, 17, 25, 40, 80]
    print(f"Inserting keys: {insert_keys}")
    nodes = {}
    for k in insert_keys:
        nodes[k] = heap.insert(k)
        
    print(f"Minimum: {heap.get_min().key}")
    
    print("Decreasing key 80 to 2...")
    heap.decrease_key(nodes[80], 2)
    print(f"New Minimum: {heap.get_min().key}")
    
    print("\nExtracting all elements:")
    while heap.n > 0:
        min_n = heap.extract_min()
        print(f"  Extracted: {min_n.key}")
