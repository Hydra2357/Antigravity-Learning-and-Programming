"""
Graph Coloring Algorithms
Graph Coloring: Assign colors to vertices such that no two adjacent vertices share the same color.
Goal: Minimize the number of colors used (chromatic number).
Includes:
1. Welsh-Powell Algorithm (Greedy Heuristic):
   - Sorts vertices by degree in descending order.
   - Assigns the first available color to the first vertex, then iterates and assigns the same color to all non-adjacent vertices.
   - Repeats with new colors.
2. Backtracking Exact Coloring (NP-Complete decision problem):
   - Verifies if the graph is K-colorable and outputs the exact coloring.
"""

class GraphColoring:
    def __init__(self, num_vertices, edges):
        self.v = num_vertices
        self.edges = edges
        self.adj = {i: set() for i in range(num_vertices)}
        for u, v in edges:
            self.adj[u].add(v)
            self.adj[v].add(u)

    # --- 1. Welsh-Powell Greedy Heuristic ---
    def welsh_powell_coloring(self):
        """
        Greedy coloring using the Welsh-Powell degree ordering.
        Returns: dict mapping vertex -> color (0, 1, 2, ...)
        """
        # Sort vertices by degree in descending order
        sorted_vertices = sorted(range(self.v), key=lambda x: len(self.adj[x]), reverse=True)
        
        # Colors assigned: vertex -> color
        colors = {i: -1 for i in range(self.v)}
        
        current_color = 0
        while -1 in colors.values():
            # For each color, color the first uncolored vertex in sorted order,
            # and then color any subsequent uncolored vertex not adjacent to any vertex already colored with current_color.
            colored_in_this_phase = []
            
            for u in sorted_vertices:
                if colors[u] == -1:
                    # Check adjacency with already colored nodes in this phase
                    adjacent_to_phase_nodes = False
                    for val in colored_in_this_phase:
                        if u in self.adj[val]:
                            adjacent_to_phase_nodes = True
                            break
                            
                    if not adjacent_to_phase_nodes:
                        colors[u] = current_color
                        colored_in_this_phase.append(u)
                        
            current_color += 1
            
        return colors

    # --- 2. Backtracking Exact Coloring ---
    def solve_exact_coloring(self):
        """
        Finds the chromatic number of the graph by trying K = 1, 2, ...
        Returns: chromatic number, and dict mapping vertex -> color
        """
        for k in range(1, self.v + 1):
            color_assignment = [-1] * self.v
            if self._is_k_colorable(0, color_assignment, k):
                # Map array index to dict
                result_map = {i: color_assignment[i] for i in range(self.v)}
                return k, result_map
        return self.v, {i: i for i in range(self.v)}

    def _is_k_colorable(self, u, colors, k):
        if u == self.v:
            return True
            
        for color in range(k):
            if self._is_safe(u, colors, color):
                colors[u] = color
                if self._is_k_colorable(u + 1, colors, k):
                    return True
                colors[u] = -1
                
        return False

    def _is_safe(self, u, colors, color):
        for neighbor in self.adj[u]:
            if colors[neighbor] == color:
                return False
        return True

if __name__ == "__main__":
    print("=== Graph Coloring Algorithms Demo ===")
    
    # 5-vertex graph: Cycle C5 (chromatic number is 3)
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 0)
    ]
    num_vertices = 5
    
    gc = GraphColoring(num_vertices, edges)
    
    print(f"Graph Edges: {edges}")
    
    # 1. Welsh-Powell
    wp_colors = gc.welsh_powell_coloring()
    num_wp_colors = len(set(wp_colors.values()))
    print(f"\nWelsh-Powell Greedy Coloring: {wp_colors}")
    print(f"  Colors used: {num_wp_colors}")
    
    # 2. Exact Backtracking
    chromatic_num, exact_colors = gc.solve_exact_coloring()
    print(f"\nExact Coloring (Backtracking): {exact_colors}")
    print(f"  Chromatic Number: {chromatic_num} (Expected: 3)")
