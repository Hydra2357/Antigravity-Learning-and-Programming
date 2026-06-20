"""
Topological Sort Implementation
Computes a linear ordering of vertices in a Directed Acyclic Graph (DAG)
such that for every directed edge u -> v, u comes before v.
Includes:
1. Kahn's Algorithm (BFS-based, uses indegrees). O(V + E) time, O(V) space.
2. DFS-based Topological Sort. O(V + E) time, O(V) space.
"""

from collections import deque

def topological_sort_kahns(graph):
    """
    Kahn's Algorithm for topological sorting.
    Also detects cycles (if graph has cycle, sorted list length < V).
    """
    # Calculate indegrees of all vertices
    indegree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] = indegree.get(v, 0) + 1
            
    # Queue for vertices with indegree 0
    queue = deque([u for u in graph if indegree[u] == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        
        for v in graph.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
                
    if len(topo_order) != len(graph):
        raise ValueError("Graph contains a cycle; topological sort not possible.")
        
    return topo_order

def topological_sort_dfs(graph):
    """
    DFS-based Topological Sort.
    """
    visited = set()
    stack = []
    
    # State tracking to detect cycles during DFS
    # 0 = unvisited, 1 = visiting, 2 = visited
    state = {u: 0 for u in graph}
    
    def dfs_visit(u):
        state[u] = 1  # visiting
        for v in graph.get(u, []):
            if state.get(v, 0) == 1:
                raise ValueError("Graph contains a cycle; topological sort not possible.")
            elif state.get(v, 0) == 0:
                dfs_visit(v)
        state[u] = 2  # visited
        stack.append(u)
        
    for u in graph:
        if state[u] == 0:
            dfs_visit(u)
            
    # Topological order is the reverse of the stack
    return stack[::-1]

if __name__ == "__main__":
    print("=== Topological Sort Demo ===")
    
    # Representing a DAG
    dag = {
        5: [2, 0],
        4: [0, 1],
        2: [3],
        3: [1],
        0: [],
        1: []
    }
    
    print(f"DAG: {dag}")
    print(f"Kahn's Sort: {topological_sort_kahns(dag)}")
    print(f"DFS-based Sort: {topological_sort_dfs(dag)}")
    
    # Cyclic Graph test
    cyclic = {
        0: [1],
        1: [2],
        2: [0]
    }
    print(f"\nCyclic Graph: {cyclic}")
    try:
        topological_sort_kahns(cyclic)
    except ValueError as e:
        print(f"Error caught: {e}")
