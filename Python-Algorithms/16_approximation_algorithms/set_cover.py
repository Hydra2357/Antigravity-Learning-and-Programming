"""
Greedy Set Cover Approximation Algorithm
Set Cover Problem: Given a universe U of elements and a collection S of subsets of U,
find the minimum number of subsets whose union is equal to U.
This problem is NP-Hard.
The greedy approximation algorithm selects, at each step, the subset that covers the largest number of uncovered elements.
Approximation Ratio: ln(H(size of U)) <= ln(N) + 1 approximation.
Time Complexity: O(N * M) where N is number of elements, M is number of subsets.
Space Complexity: O(N)
"""

def set_cover_greedy(universe, subsets):
    """
    subsets: dict where keys are subset names and values are sets of elements.
    Returns: List of subset names selected, and the set of elements covered.
    """
    uncovered = set(universe)
    selected_subsets = []
    
    while uncovered:
        # Find the subset that covers the maximum number of uncovered elements
        best_subset = None
        best_covered = set()
        
        for name, elements in subsets.items():
            covered = elements.intersection(uncovered)
            if len(covered) > len(best_covered):
                best_subset = name
                best_covered = covered
                
        if best_subset is None:
            # Universe cannot be fully covered by the given subsets
            break
            
        selected_subsets.append(best_subset)
        uncovered = uncovered.difference(best_covered)
        
    return selected_subsets

if __name__ == "__main__":
    print("=== Greedy Set Cover Approximation Demo ===")
    
    universe = {1, 2, 3, 4, 5}
    subsets = {
        'S1': {1, 2, 3},
        'S2': {2, 4},
        'S3': {3, 4},
        'S4': {4, 5},
        'S5': {5}
    }
    
    print(f"Universe: {universe}")
    print(f"Subsets:  {subsets}")
    
    selected = set_cover_greedy(universe, subsets)
    print(f"\nSelected Subsets: {selected}")
    
    # Calculate union of selected subsets
    union_elements = set()
    for s in selected:
        union_elements = union_elements.union(subsets[s])
    print(f"Covered Elements: {union_elements}")
