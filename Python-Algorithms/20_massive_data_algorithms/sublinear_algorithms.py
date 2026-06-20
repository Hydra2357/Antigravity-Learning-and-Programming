"""
Massive Data Algorithms - Sublinear Algorithms and Property Testing
Sublinear algorithms process massive datasets in time or space that is strictly less than the size of the input (e.g. O(log N) or O(sqrt(N))).
This script implements:
1. Sublinear Sortedness Tester (Property Testing):
   - Determines if an array of size N is sorted, or if it is "epsilon-far" from sorted (must delete > epsilon * N elements to make it sorted).
   - Uses randomized binary search checks.
   - Time Complexity: O((1/epsilon) * log N) queries.
2. Sublinear Connected Components Estimator (Chazelle's paradigm):
   - Estimates the number of connected components in a graph in sublinear time using neighborhood sizing.
   - Time Complexity: O(1/epsilon^2) node neighborhood exploration steps.
"""

import random

# --- 1. Sublinear Sortedness Property Tester ---
def is_sorted_sublinear(arr, epsilon=0.1, confidence_trials=20):
    """
    Sublinear Sortedness Property Tester.
    - If arr is sorted, returns True.
    - If arr is epsilon-far from sorted, returns False with probability >= 2/3.
    Algorithm:
    - Pick a random index i.
    - Perform a binary search on the array looking for arr[i].
    - If binary search fails or encounters an inversion, we found a witness of unsortedness.
    - Repeat O(1/epsilon) times.
    """
    n = len(arr)
    if n <= 1:
        return True
        
    for _ in range(confidence_trials):
        # Pick a random index i
        i = random.randint(0, n - 1)
        val = arr[i]
        
        # Perform binary search looking for arr[i]
        low = 0
        high = n - 1
        found = False
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check for local inversion
            if mid < n - 1 and arr[mid] > arr[mid + 1]:
                return False  # Witness of unsortedness
            if mid > 0 and arr[mid - 1] > arr[mid]:
                return False  # Witness of unsortedness
                
            if arr[mid] == val:
                if mid == i:
                    found = True
                # Break to save time, or continue.
                # In standard sublinear sortedness testing, we just check if binary search paths are consistent.
                break
            elif arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1
                
        # If binary search fails to locate the index i properly due to inconsistencies
        if not found:
            return False  # Witness of unsortedness
            
    return True  # Probably sorted

# --- 2. Sublinear Connected Components Estimator ---
def estimate_connected_components_sublinear(graph, max_degree, epsilon=0.2):
    """
    Estimates the number of connected components C in a graph of size N.
    Based on the formula: C = sum_{u in V} (1 / size of component containing u)
    Instead of summing over all u, we sample a random set of vertices S,
    estimate the component size for each, and scale up.
    If a component is larger than a threshold, we cap it to save time (sublinear exploration).
    """
    n = len(graph)
    # Sample size needed for epsilon approximation
    k = int(2 / (epsilon ** 2))
    k = min(k, n)
    
    samples = random.sample(list(graph.keys()), k)
    
    sum_inverse_sizes = 0.0
    threshold = int(2.0 / epsilon)
    
    for u in samples:
        # Explore BFS neighborhood of u up to threshold
        visited = {u}
        queue = [u]
        
        while queue and len(visited) < threshold:
            curr = queue.pop(0)
            for neighbor in graph.get(curr, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    if len(visited) >= threshold:
                        break
                        
        component_size = len(visited)
        sum_inverse_sizes += 1.0 / component_size
        
    # Scale sample average to estimate total components count
    estimated_c = (n / k) * sum_inverse_sizes
    return round(estimated_c)

if __name__ == "__main__":
    print("=== Sublinear & Property Testing Demo ===")
    
    # 1. Sortedness Tester Test
    print("\n1. Sortedness Property Testing:")
    sorted_list = list(range(1, 10001))
    
    # Create list that is far from sorted (e.g. 20% unsorted)
    unsorted_list = list(range(1, 10001))
    for idx in range(0, 10000, 5):
        # swap elements to make it unsorted
        unsorted_list[idx], unsorted_list[idx + 1] = unsorted_list[idx + 1], unsorted_list[idx]
        
    print(f"  Testing sorted list of size {len(sorted_list)}...")
    print(f"    Tester returns: {is_sorted_sublinear(sorted_list)} (expected: True)")
    
    print(f"  Testing 20% unsorted list of size {len(unsorted_list)}...")
    print(f"    Tester returns: {is_sorted_sublinear(unsorted_list)} (expected: False)")
    
    # 2. Connected Components Estimator
    print("\n2. Connected Components Estimator:")
    # Graph with 4 distinct connected components
    # 0-1-2, 3-4, 5-6-7-8, 9
    graph = {
        0: [1, 2], 1: [0, 2], 2: [0, 1],
        3: [4], 4: [3],
        5: [6], 6: [5, 7], 7: [6, 8], 8: [7],
        9: []
    }
    
    actual_c = 4
    estimated_c = estimate_connected_components_sublinear(graph, max_degree=3, epsilon=0.1)
    print(f"  Actual components count:    {actual_c}")
    print(f"  Sublinear Estimated count:  {estimated_c}")
