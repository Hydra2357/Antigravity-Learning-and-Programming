"""
Vertex Cover 2-Approximation Algorithm
Vertex Cover Problem: Find a minimum set of vertices such that every edge in the graph
is incident to at least one vertex in the set.
This problem is NP-Hard.
The 2-approximation algorithm works by repeatedly picking an arbitrary edge (u, v) in the graph,
adding both endpoints u and v to the vertex cover, and removing all edges incident to u or v.
Approximation Ratio: Guaranteed to be at most 2 times the size of the optimal vertex cover.
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

def vertex_cover_approx(num_vertices, edges):
    """
    edges: list of tuples (u, v) representing undirected edges.
    Returns: set of vertices in the cover.
    """
    cover = set()
    # Working copy of edges as a set of tuples (u, v) (standardize order to avoid duplicates)
    remaining_edges = {tuple(sorted(edge)) for edge in edges}
    
    while remaining_edges:
        # Pick an arbitrary edge
        u, v = remaining_edges.pop()
        
        # Add both endpoints to the cover
        cover.add(u)
        cover.add(v)
        
        # Remove all remaining edges incident to either u or v
        edges_to_remove = set()
        for edge in remaining_edges:
            if edge[0] == u or edge[1] == u or edge[0] == v or edge[1] == v:
                edges_to_remove.add(edge)
                
        remaining_edges = remaining_edges.difference(edges_to_remove)
        
    return cover

if __name__ == "__main__":
    print("=== Vertex Cover 2-Approximation Demo ===")
    
    # Graph structure:
    # 0 - 1 - 2 - 3 - 4 - 5
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5)
    ]
    
    print(f"Edges: {edges}")
    
    cover = vertex_cover_approx(6, edges)
    print(f"Approximated Vertex Cover (endpoints selection): {cover}")
    
    # Verify validity: Every edge must have at least one endpoint in cover
    valid = True
    for u, v in edges:
        if u not in cover and v not in cover:
            valid = False
            break
            
    print(f"Is the cover valid? {valid}")
