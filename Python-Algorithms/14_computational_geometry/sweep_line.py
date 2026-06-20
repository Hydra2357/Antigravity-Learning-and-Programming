"""
Sweep Line Algorithm Demo - Closest Pair of Points
The Sweep Line paradigm sorts geometric objects by one coordinate (e.g., X-coordinate)
and processes them sequentially (sweeping a vertical line from left to right)
while maintaining an active set of candidates in a data structure ordered by another coordinate.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

import math
import bisect

def closest_pair_sweep_line(points):
    """
    Finds the closest pair of points and their distance using the Sweep Line technique.
    """
    if len(points) < 2:
        return float('inf'), None
        
    # Step 1: Sort points by X-coordinate
    pts_x = sorted(points, key=lambda p: p[0])
    
    # Active set of points, sorted by Y-coordinate.
    # In python, we can maintain this list sorted using bisect.
    active_y = []
    
    min_dist = float('inf')
    best_pair = None
    
    left_idx = 0  # Points to the leftmost point in the active window
    
    for i in range(len(pts_x)):
        curr = pts_x[i]
        
        # Step 2: Remove points from active set whose X-coordinate is further than min_dist
        while pts_x[left_idx][0] < curr[0] - min_dist:
            # Remove pts_x[left_idx] from active_y
            p_to_remove = pts_x[left_idx]
            # Since active_y is sorted by Y, we search by Y-coordinate to remove
            remove_idx = bisect.bisect_left(active_y, (p_to_remove[1], p_to_remove[0]))
            # Make sure we remove the correct point
            while remove_idx < len(active_y):
                if active_y[remove_idx][1] == p_to_remove[0] and active_y[remove_idx][0] == p_to_remove[1]:
                    active_y.pop(remove_idx)
                    break
                remove_idx += 1
            left_idx += 1
            
        # Step 3: Find candidate points in active set within [curr.y - min_dist, curr.y + min_dist]
        lower_y = curr[1] - min_dist
        upper_y = curr[1] + min_dist
        
        # Find range using binary search
        start_idx = bisect.bisect_left(active_y, (lower_y, -float('inf')))
        
        # Iterate through candidates
        for j in range(start_idx, len(active_y)):
            candidate = active_y[j]
            # If candidate's Y is beyond the window, we can stop
            if candidate[0] > upper_y:
                break
                
            # Compute distance between curr and candidate (represented as (y, x))
            dist = math.hypot(curr[0] - candidate[1], curr[1] - candidate[0])
            if dist < min_dist:
                min_dist = dist
                best_pair = (curr, (candidate[1], candidate[0]))
                
        # Step 4: Insert current point into active_y (stored as (y, x) for sorting by Y)
        bisect.insort(active_y, (curr[1], curr[0]))
        
    return min_dist, best_pair

if __name__ == "__main__":
    print("=== Sweep Line (Closest Pair of Points) Demo ===")
    
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(f"Points: {points}")
    
    dist, pair = closest_pair_sweep_line(points)
    print(f"Closest distance: {dist:.6f}")
    print(f"Closest pair:     {pair} (expected: (2,3) and (3,4) with distance 1.414)")
