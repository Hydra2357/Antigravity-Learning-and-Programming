"""
Breadth-First Search (BFS) Implementation
Explores vertices layer by layer starting from a source vertex.
Used for finding the shortest path in an unweighted graph.
Time Complexity: O(V + E) where V is vertices, E is edges.
Space Complexity: O(V) for queue and visited set.
"""

from collections import deque

def bfs(graph, start):
    """
    Performs standard BFS traversal.
    graph: dict where graph[u] is a list of neighbors of u.
    Returns: Order of visited vertices.
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    traversal_order = []
    
    while queue:
        vertex = queue.popleft()
        traversal_order.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

def bfs_shortest_path(graph, start, goal):
    """
    Finds the shortest path from start to goal in an unweighted graph using BFS.
    Returns: List of vertices representing the path, or None if no path exists.
    """
    if start == goal:
        return [start]
        
    visited = set()
    queue = deque([[start]])
    visited.add(start)
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                if neighbor == goal:
                    return new_path
                visited.add(neighbor)
                queue.append(new_path)
                
    return None

if __name__ == "__main__":
    print("=== Breadth-First Search (BFS) Demo ===")
    
    # Adjacency list representation of a graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print(f"Graph: {graph}")
    print(f"BFS Traversal starting from 'A': {bfs(graph, 'A')}")
    
    path = bfs_shortest_path(graph, 'A', 'F')
    print(f"Shortest path from 'A' to 'F': {path}")
