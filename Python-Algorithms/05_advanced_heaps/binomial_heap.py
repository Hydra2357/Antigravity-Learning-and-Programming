"""
Binomial Heap Implementation
A collection of binomial trees.
Time Complexities:
    - Insert: O(1) amortized, O(log N) worst-case
    - Minimum: O(log N) (can be O(1) if tracked)
    - Extract Min: O(log N)
    - Union (Merge): O(log N)
    - Decrease Key: O(log N)
    - Delete: O(log N)
Space Complexity: O(N)
"""

class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.child = None
        self.sibling = None
        self.parent = None

class BinomialHeap:
    def __init__(self):
        self.head = None

    def merge_trees(self, y, z):
        """Merges two binomial trees of the same degree."""
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1

    def union(self, other_heap):
        """Unites this binomial heap with another."""
        new_head = self._merge_heads(self.head, other_heap.head)
        if not new_head:
            self.head = None
            return
            
        prev_x = None
        x = new_head
        next_x = x.sibling
        
        while next_x:
            # Case 1 & Case 2: degree[x] != degree[next_x] or there are 3 trees of same degree
            if (x.degree != next_x.degree) or (next_x.sibling and next_x.sibling.degree == x.degree):
                prev_x = x
                x = next_x
            # Case 3: key[x] <= key[next_x]
            elif x.key <= next_x.key:
                x.sibling = next_x.sibling
                self.merge_trees(next_x, x)
            # Case 4: key[next_x] < key[x]
            else:
                if not prev_x:
                    new_head = next_x
                else:
                    prev_x.sibling = next_x
                self.merge_trees(x, next_x)
                x = next_x
                
            next_x = x.sibling
            
        self.head = new_head

    def _merge_heads(self, h1, h2):
        """Helper to merge the root lists of h1 and h2 sorted by degree."""
        if not h1:
            return h2
        if not h2:
            return h1
            
        if h1.degree <= h2.degree:
            head = h1
            h1 = h1.sibling
        else:
            head = h2
            h2 = h2.sibling
            
        curr = head
        while h1 and h2:
            if h1.degree <= h2.degree:
                curr.sibling = h1
                h1 = h1.sibling
            else:
                curr.sibling = h2
                h2 = h2.sibling
            curr = curr.sibling
            
        curr.sibling = h1 if h1 else h2
        return head

    def insert(self, key):
        """Inserts a key into the heap."""
        temp_node = BinomialNode(key)
        temp_heap = BinomialHeap()
        temp_heap.head = temp_node
        self.union(temp_heap)
        return temp_node

    def get_min(self):
        """Returns the minimum node in the heap."""
        if not self.head:
            return None
        min_node = self.head
        curr = self.head.sibling
        while curr:
            if curr.key < min_node.key:
                min_node = curr
            curr = curr.sibling
        return min_node

    def extract_min(self):
        """Extracts the node with minimum key."""
        if not self.head:
            return None
            
        # Find minimum node
        min_node = self.head
        prev_min = None
        curr = self.head.sibling
        prev_curr = self.head
        
        while curr:
            if curr.key < min_node.key:
                min_node = curr
                prev_min = prev_curr
            prev_curr = curr
            curr = curr.sibling
            
        # Remove min_node from root list
        if not prev_min:
            self.head = min_node.sibling
        else:
            prev_min.sibling = min_node.sibling
            
        # Reverse the child list of min_node and create a new heap
        child_heap = BinomialHeap()
        curr_child = min_node.child
        prev_child = None
        
        while curr_child:
            next_child = curr_child.sibling
            curr_child.sibling = prev_child
            curr_child.parent = None
            prev_child = curr_child
            curr_child = next_child
            
        child_heap.head = prev_child
        
        # Union the original heap and the reversed child heap
        self.union(child_heap)
        return min_node

    def decrease_key(self, node, new_key):
        """Decreases the key of a node to new_key."""
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        node.key = new_key
        
        # Bubble up if necessary
        curr = node
        parent = curr.parent
        while parent and curr.key < parent.key:
            # Swap keys
            curr.key, parent.key = parent.key, curr.key
            # In a full pointer-based decrease-key, node identity changes or we update pointers.
            # Here we just swap values for simplicity.
            curr = parent
            parent = curr.parent

if __name__ == "__main__":
    print("=== Binomial Heap Demo ===")
    heap = BinomialHeap()
    
    # Insert elements
    insert_keys = [12, 7, 25, 15, 28, 33, 41, 1]
    print(f"Inserting: {insert_keys}")
    nodes = {}
    for k in insert_keys:
        nodes[k] = heap.insert(k)
        
    print(f"Minimum value: {heap.get_min().key}")
    
    # Decrease key of node with key 28 to 2
    print("Decreasing key 28 to 2...")
    heap.decrease_key(nodes[28], 2)
    print(f"New minimum value: {heap.get_min().key}")
    
    # Extract minimums
    print("\nExtracting all elements in order:")
    while heap.head:
        min_n = heap.extract_min()
        print(f"  Extracted: {min_n.key}")
