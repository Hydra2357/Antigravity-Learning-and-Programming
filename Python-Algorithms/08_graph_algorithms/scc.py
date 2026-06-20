"""
Strongly Connected Components (SCC) Algorithms
Computes all maximal strongly connected subgraphs in a directed graph.
Includes:
1. Tarjan's Algorithm: Uses a single DFS pass, tracking low-link values and node stacks. O(V + E) time, O(V) space.
2. Kosaraju's Algorithm: Uses two DFS passes (original graph and transposed graph). O(V + E) time, O(V) space.
"""

def tarjans_scc(graph):
    """
    Finds Strongly Connected Components using Tarjan's Algorithm.
    """
    index = 0
    indices = {}
    lowlink = {}
    stack = []
    on_stack = set()
    sccs = []
    
    def strongconnect(u):
        nonlocal index
        indices[u] = index
        lowlink[u] = index
        index += 1
        stack.append(u)
        on_stack.add(u)
        
        for v in graph.get(u, []):
            if v not in indices:
                # v has not been visited; recurse
                strongconnect(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif v in on_stack:
                # v is in the stack, so it's in the current SCC
                lowlink[u] = min(lowlink[u], indices[v])
                
        # If u is a root node, pop the stack and generate an SCC
        if lowlink[u] == indices[u]:
            scc = []
            while True:
                v = stack.pop()
                on_stack.remove(v)
                scc.append(v)
                if v == u:
                    break
            sccs.append(scc)
            
    for node in graph:
        if node not in indices:
            strongconnect(node)
            
    return sccs

def kosarajus_scc(graph):
    """
    Finds Strongly Connected Components using Kosaraju's Algorithm.
    """
    # Step 1: Fill vertices in stack according to their finishing times in DFS
    visited = set()
    stack = []
    
    def dfs_first_pass(u):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs_first_pass(v)
        stack.append(u)
        
    for node in graph:
        if node not in visited:
            dfs_first_pass(node)
            
    # Step 2: Get transposed graph (reverse all edges)
    transposed = {u: [] for u in graph}
    for u in graph:
        for v in graph[u]:
            if v not in transposed:
                transposed[v] = []
            transposed[v].append(u)
            
    # Step 3: Process all vertices in order defined by stack
    visited.clear()
    sccs = []
    
    def dfs_second_pass(u, current_scc):
        visited.add(u)
        current_scc.append(u)
        for v in transposed.get(u, []):
            if v not in visited:
                dfs_second_pass(v, current_scc)
                
    while stack:
        u = stack.pop()
        if u not in visited:
            scc = []
            dfs_second_pass(u, scc)
            sccs.append(scc)
            
    return sccs

if __name__ == "__main__":
    print("=== Strongly Connected Components Demo ===")
    
    # Graph with 3 SCCs: {0, 1, 2}, {3}, {4}
    graph = {
        0: [2, 3],
        1: [0],
        2: [1],
        3: [4],
        4: []
    }
    
    print(f"Graph: {graph}")
    print(f"Tarjan's SCCs:   {tarjans_scc(graph)}")
    print(f"Kosaraju's SCCs: {kosarajus_scc(graph)}")
