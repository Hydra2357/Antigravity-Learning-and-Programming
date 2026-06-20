"""
Bellman-Ford Single-Source Shortest Path Algorithm
Finds shortest paths from a single source vertex to all other vertices in a weighted graph (allows negative edge weights).
Detects negative weight cycles.
Time Complexity: O(V * E) where V is vertices, E is edges.
Space Complexity: O(V)
"""

def bellman_ford(vertices, edges, start):
    """
    Computes shortest distances from start.
    vertices: list of vertices.
    edges: list of tuples (u, v, weight).
    Returns: distances dict, parents dict, has_negative_cycle bool.
    """
    # Step 1: Initialize distances from start to all other vertices as infinity
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    parents = {v: None for v in vertices}
    
    # Step 2: Relax all edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                parents[v] = u
                
    # Step 3: Check for negative-weight cycles
    # If we can still relax an edge, then there is a negative cycle.
    has_negative_cycle = False
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            has_negative_cycle = True
            break
            
    return distances, parents, has_negative_cycle

def reconstruct_path(parents, start, target):
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        if curr == start:
            break
        curr = parents[curr]
    path.reverse()
    return path if path[0] == start else []

if __name__ == "__main__":
    print("=== Bellman-Ford Algorithm Demo ===")
    
    vertices = ['A', 'B', 'C', 'D', 'E']
    # Directed edges (u, v, weight)
    edges = [
        ('A', 'B', -1),
        ('A', 'C', 4),
        ('B', 'C', 3),
        ('B', 'D', 2),
        ('B', 'E', 2),
        ('D', 'B', 1),
        ('D', 'C', 5),
        ('E', 'D', -3)
    ]
    
    print("1. Testing graph with negative weight edges, no negative cycle:")
    distances, parents, has_neg_cycle = bellman_ford(vertices, edges, 'A')
    print(f"Has negative cycle? {has_neg_cycle}")
    print("Shortest distances:")
    for v, dist in distances.items():
        path = reconstruct_path(parents, 'A', v)
        print(f"  To {v}: distance = {dist:2d}, path = {path}")
        
    # Introduce a negative cycle: D -> B (-4) instead of D -> B (1)
    # The cycle B -> E (-3) -> D (1) -> B (-4) has total weight -6
    cyclic_edges = [
        ('A', 'B', -1),
        ('A', 'C', 4),
        ('B', 'C', 3),
        ('B', 'D', 2),
        ('B', 'E', 2),
        ('D', 'B', -4),  # Changed here to create negative cycle
        ('D', 'C', 5),
        ('E', 'D', -3)
    ]
    
    print("\n2. Testing graph WITH negative cycle:")
    _, _, has_neg_cycle = bellman_ford(vertices, cyclic_edges, 'A')
    print(f"Has negative cycle? {has_neg_cycle} (Expected: True)")
