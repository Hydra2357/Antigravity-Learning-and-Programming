"""
Dijkstra's Single-Source Shortest Path Algorithm
Finds shortest paths from a single source vertex to all other vertices in a weighted graph with non-negative edge weights.
Uses a priority queue (min-heap).
Time Complexity: O(E log V)
Space Complexity: O(V)
"""

import heapq

def dijkstra(graph, start):
    """
    Computes shortest distances and paths from 'start'.
    graph: dict where graph[u] is a list of tuples (neighbor_v, weight)
    Returns: distances dict, parents dict (for path reconstruction)
    """
    # Initialize distances to infinity, start node to 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Track parent node for path reconstruction
    parents = {node: None for node in graph}
    
    # Priority queue stores tuples: (distance, node)
    pq = [(0, start)]
    
    # Track visited/finalized nodes
    visited = set()
    
    while pq:
        current_distance, u = heapq.heappop(pq)
        
        # Nodes can be pushed to PQ multiple times, skip if already visited
        if u in visited:
            continue
        visited.add(u)
        
        for neighbor, weight in graph.get(u, []):
            distance = current_distance + weight
            
            # If a shorter path is found, update and push to PQ
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = u
                heapq.heappush(pq, (distance, neighbor))
                
    return distances, parents

def get_path(parents, start, target):
    """Reconstructs the shortest path from start to target."""
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
    print("=== Dijkstra's Algorithm Demo ===")
    
    # Weighted directed graph
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 3), ('D', 2), ('E', 3)],
        'C': [('B', 1), ('D', 4), ('E', 5)],
        'D': [],
        'E': [('D', 1)]
    }
    
    print(f"Graph: {graph}")
    distances, parents = dijkstra(graph, 'A')
    
    print("\nShortest distances from 'A':")
    for node, dist in distances.items():
        path = get_path(parents, 'A', node)
        print(f"  To {node}: distance = {dist}, path = {path}")
