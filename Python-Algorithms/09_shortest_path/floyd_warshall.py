"""
Floyd-Warshall All-Pairs Shortest Path Algorithm
Dynamic Programming algorithm to solve the all-pairs shortest path problem in a weighted graph.
Allows negative edge weights (but no negative weight cycles).
Time Complexity: O(V^3) where V is the number of vertices.
Space Complexity: O(V^2) for the distance matrix.
"""

def floyd_warshall(n, adj_matrix):
    """
    Computes all-pairs shortest paths.
    adj_matrix: 2D list where adj_matrix[i][j] is the weight of edge i -> j.
                If no edge exists, weight should be float('inf').
                adj_matrix[i][i] should be 0.
    Returns: 2D list of shortest distances, and next_vertex matrix for path reconstruction.
    """
    # Initialize distances and path reconstruction matrix
    dist = [[float('inf')] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            dist[i][j] = adj_matrix[i][j]
            if adj_matrix[i][j] != float('inf') and i != j:
                next_node[i][j] = j
                
    # Floyd-Warshall DP updates
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        dist[i][j] = new_dist
                        next_node[i][j] = next_node[i][k]
                        
    # Check for negative self-loops (indicates negative cycle)
    for i in range(n):
        if dist[i][i] < 0:
            raise ValueError("Graph contains a negative weight cycle!")
            
    return dist, next_node

def reconstruct_path(i, j, next_node):
    """Reconstructs shortest path from i to j using next_node matrix."""
    if next_node[i][j] is None:
        return []
    path = [i]
    while i != j:
        i = next_node[i][j]
        if i is None:
            return []
        path.append(i)
    return path

if __name__ == "__main__":
    print("=== Floyd-Warshall Algorithm Demo ===")
    
    # 4 vertices graph (0 to 3)
    n = 4
    INF = float('inf')
    
    # Adjacency matrix representation
    adj = [
        [0,   3,   INF, 7],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1],
        [2,   INF, INF, 0]
    ]
    
    print("Input adjacency matrix (INF means no edge):")
    for r in adj:
        print(f"  {r}")
        
    distances, next_node = floyd_warshall(n, adj)
    
    print("\nAll-Pairs Shortest Distances:")
    for i in range(n):
        row_str = [f"{d:3.1f}" if d != INF else "INF" for d in distances[i]]
        print(f"  Row {i}: {row_str}")
        
    print("\nReconstructed Shortest Paths:")
    for i in range(n):
        for j in range(n):
            if i != j:
                path = reconstruct_path(i, j, next_node)
                print(f"  Shortest path from {i} to {j}: {path} (Distance: {distances[i][j]})")
