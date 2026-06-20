"""
Divide and Conquer Closest Pair of Points Algorithm
Finds the two closest points in a 2D plane.
Time Complexity: O(N log N) using sorting.
Space Complexity: O(N) recursion stack and buffer.
"""

import math

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def brute_force(points):
    min_d = float('inf')
    best_pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_d:
                min_d = d
                best_pair = (points[i], points[j])
    return min_d, best_pair

def closest_pair_divide_and_conquer(points):
    """
    Main driver function.
    """
    if len(points) < 2:
        return float('inf'), None
        
    # Sort points by X-coordinate
    pts_x = sorted(points, key=lambda p: p[0])
    # Sort points by Y-coordinate
    pts_y = sorted(points, key=lambda p: p[1])
    
    return _closest_pair_rec(pts_x, pts_y)

def _closest_pair_rec(pts_x, pts_y):
    n = len(pts_x)
    if n <= 3:
        return brute_force(pts_x)
        
    mid = n // 2
    mid_point = pts_x[mid]
    
    # Divide pts_y into left and right halves based on X coordinate
    # (keeps them sorted by Y)
    pts_y_left = []
    pts_y_right = []
    for p in pts_y:
        # To handle duplicate X-coordinates correctly, we partition by index boundary or midpoint X
        if p[0] < mid_point[0]:
            pts_y_left.append(p)
        else:
            pts_y_right.append(p)
            
    # If division isn't balanced due to vertical line ties, resolve:
    if len(pts_y_left) == 0 or len(pts_y_right) == 0:
        pts_y_left = pts_y[:mid]
        pts_y_right = pts_y[mid:]
        
    dl, pair_l = _closest_pair_rec(pts_x[:mid], pts_y_left)
    dr, pair_r = _closest_pair_rec(pts_x[mid:], pts_y_right)
    
    d = dl
    best_pair = pair_l
    if dr < dl:
        d = dr
        best_pair = pair_r
        
    # Find points inside strip of width 2d
    strip = [p for p in pts_y if abs(p[0] - mid_point[0]) < d]
    
    # Check strip points
    min_strip_d = d
    best_strip_pair = None
    
    for i in range(len(strip)):
        # Inner loop runs at most 7 times due to geometric bounds
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_strip_d:
                break
            dist = distance(strip[i], strip[j])
            if dist < min_strip_d:
                min_strip_d = dist
                best_strip_pair = (strip[i], strip[j])
                
    if best_strip_pair is not None:
        return min_strip_d, best_strip_pair
    return d, best_pair

if __name__ == "__main__":
    print("=== Divide & Conquer Closest Pair of Points ===")
    
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(f"Points: {points}")
    
    dist, pair = closest_pair_divide_and_conquer(points)
    print(f"Closest distance: {dist:.6f}")
    print(f"Closest pair:     {pair}")
