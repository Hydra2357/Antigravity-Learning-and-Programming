"""
Depth-First Search (DFS) Implementation
Explores as deep as possible along each branch before backtracking.
Includes cycle detection for directed and undirected graphs.
Time Complexity: O(V + E)
Space Complexity: O(V) for recursion stack / visited.
"""

def dfs_recursive(graph, start, visited=None, traversal=None):
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []
        
    visited.add(start)
    traversal.append(start)
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal)
            
    return traversal

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    traversal = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            # Push neighbors in reverse order so they are processed in order
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return traversal

def has_cycle_directed(graph):
    """
    Checks if a directed graph contains a cycle using DFS (3-coloring: white, gray, black).
    0 = Unvisited (White)
    1 = Visiting / in recursion stack (Gray)
    2 = Fully visited (Black)
    """
    state = {v: 0 for v in graph}
    
    def dfs_visit(u):
        state[u] = 1  # Gray
        for v in graph.get(u, []):
            if state.get(v, 0) == 1:
                return True  # Found back-edge (cycle)
            elif state.get(v, 0) == 0:
                if dfs_visit(v):
                    return True
        state[u] = 2  # Black
        return False
        
    for node in graph:
        if state[node] == 0:
            if dfs_visit(node):
                return True
    return False

if __name__ == "__main__":
    print("=== Depth-First Search (DFS) Demo ===")
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    print(f"Graph: {graph}")
    print(f"DFS Recursive Traversal from 'A': {dfs_recursive(graph, 'A')}")
    print(f"DFS Iterative Traversal from 'A': {dfs_iterative(graph, 'A')}")
    
    # Cycle detection tests
    cyclic_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']  # Cycle here A->B->C->A
    }
    print(f"\nDirected Graph with cycle: {cyclic_graph}")
    print(f"Has cycle? {has_cycle_directed(cyclic_graph)}")
    
    print(f"Does original graph have cycle? {has_cycle_directed(graph)}")
