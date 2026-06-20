"""
Convex Hull Algorithms
Given a set of 2D points, finds the smallest convex polygon that contains all points.
Includes:
1. Graham Scan: O(N log N) time, O(N) space.
2. Jarvis March (Gift Wrapping): O(N * H) time where H is number of hull vertices, O(N) space.
"""

import math

def orientation(p, q, r):
    """
    Returns orientation of triplet (p, q, r):
    0 -> p, q, r are collinear
    1 -> Clockwise
    2 -> Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def dist_sq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

# --- 1. Graham Scan ---
def graham_scan(points):
    n = len(points)
    if n < 3:
        return points
        
    # Find the bottom-most point (and left-most in case of tie)
    p0 = min(points, key=lambda p: (p[1], p[0]))
    
    # Sort remaining points based on polar angle with p0.
    # In case of tie, sort by distance to p0.
    def polar_angle_sort_key(p):
        if p == p0:
            return (-math.pi, 0)
        angle = math.atan2(p[1] - p0[1], p[0] - p0[0])
        dist = dist_sq(p0, p)
        return (angle, dist)
        
    sorted_pts = sorted(points, key=polar_angle_sort_key)
    
    # Filter out points with same angle, keeping only the furthest one
    # (Optional helper, but standard Graham Scan handles this using orientation checks)
    hull = [sorted_pts[0], sorted_pts[1], sorted_pts[2]]
    
    for i in range(3, n):
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], sorted_pts[i]) != 2:
            hull.pop()
        hull.append(sorted_pts[i])
        
    return hull

# --- 2. Jarvis March (Gift Wrapping) ---
def jarvis_march(points):
    n = len(points)
    if n < 3:
        return points
        
    hull = []
    # Find the leftmost point
    l = min(range(n), key=lambda i: points[i][0])
    p = l
    
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            # If i is more counterclockwise than q, update q
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        # While we don't reach the first point
        if p == l:
            break
            
    return hull

if __name__ == "__main__":
    print("=== Convex Hull Demo ===")
    
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3), (1, 2)]
    print(f"Points: {points}")
    
    gs_hull = graham_scan(points)
    print(f"Convex Hull (Graham Scan):  {gs_hull}")
    
    jm_hull = jarvis_march(points)
    print(f"Convex Hull (Jarvis March): {jm_hull}")
