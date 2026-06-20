"""
Fixed-Parameter Tractable (FPT) Algorithms
FPT algorithms solve NP-Hard problems efficiently when a certain parameter k is small.
The running time is of the form O(f(k) * N^c) where N is input size, c is a constant independent of k, and f is any function.

Problem: Vertex Cover (FPT Decision Version)
- Does there exist a vertex cover of size <= k?
- Instead of checking all subsets of size k (which takes O(N^k)), we use a bounded search tree.
- Time Complexity: O(2^k * (V + E))
"""

def fpt_vertex_cover(graph, k):
    """
    Determines if there is a vertex cover of size <= k.
    graph: dict where graph[u] is a set of neighbors.
    Returns: (bool, cover_set)
    """
    # Helper set of vertices in cover
    cover = set()
    
    def search(g, k_rem):
        # Base Case 1: If no edges remain, we have a valid cover
        has_edges = False
        for u in g:
            if g[u]:
                has_edges = True
                break
        if not has_edges:
            return True
            
        # Base Case 2: If we ran out of allowed cover size but edges remain
        if k_rem <= 0:
            return False
            
        # Pick an arbitrary edge (u, v)
        u = None
        v = None
        for node in g:
            if g[node]:
                u = node
                v = next(iter(g[node]))
                break
                
        # Branching step: Either u is in the cover, or v is in the cover
        
        # Branch 1: Include u in the cover
        # Remove u and all its incident edges
        g_u = remove_vertex(g, u)
        cover.add(u)
        if search(g_u, k_rem - 1):
            return True
        cover.remove(u)
        
        # Branch 2: Include v in the cover
        # Remove v and all its incident edges
        g_v = remove_vertex(g, v)
        cover.add(v)
        if search(g_v, k_rem - 1):
            return True
        cover.remove(v)
        
        return False

    # Perform search on a copy of the graph
    g_copy = {u: set(neighbors) for u, neighbors in graph.items()}
    result = search(g_copy, k)
    return result, (list(cover) if result else [])

def remove_vertex(g, vertex):
    """Returns a new graph with the vertex and its edges removed."""
    new_g = {u: set(neighbors) for u, neighbors in g.items() if u != vertex}
    for u in new_g:
        new_g[u].discard(vertex)
    return new_g

if __name__ == "__main__":
    print("=== Fixed-Parameter Tractable (FPT) Vertex Cover ===")
    
    # Graph:
    # 0 - 1 - 2 - 3 - 4
    #  \ /
    #   5
    graph = {
        0: {1, 5},
        1: {0, 2, 5},
        2: {1, 3},
        3: {2, 4},
        4: {3},
        5: {0, 1}
    }
    
    print(f"Graph: {graph}")
    
    # Test k = 2
    k = 2
    exists, cover = fpt_vertex_cover(graph, k)
    print(f"\nDoes a vertex cover of size <= {k} exist? {exists}")
    if exists:
        print(f"  Cover: {cover}")
        
    # Test k = 3
    k = 3
    exists, cover = fpt_vertex_cover(graph, k)
    print(f"\nDoes a vertex cover of size <= {k} exist? {exists} (Expected: True)")
    if exists:
        print(f"  Cover: {cover} (Expected to contain 1, 3, and 0 or 5)")
