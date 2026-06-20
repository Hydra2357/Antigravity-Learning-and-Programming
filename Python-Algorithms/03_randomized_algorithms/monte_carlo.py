"""
Monte Carlo Algorithm Demo - Estimating Pi
A Monte Carlo algorithm has a deterministic runtime, but its output is correct
only with a certain probability (or within a statistical margin of error).
This demo estimates the value of Pi by checking the fraction of randomly placed points
within a unit square that fall inside a quadrant of a unit circle.
"""

import random

def estimate_pi(n_samples):
    """
    Estimates Pi using Monte Carlo simulation.
    Area of quarter circle of radius 1 is pi / 4.
    Area of square of side 1 is 1.
    Ratio of points inside circle to total points is (pi / 4) / 1 = pi / 4.
    So, Pi = 4 * (inside_circle_count / total_count).
    """
    inside_circle = 0
    
    for _ in range(n_samples):
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)
        
        # Check if point (x, y) is inside the unit circle: x^2 + y^2 <= 1
        if x*x + y*y <= 1.0:
            inside_circle += 1
            
    pi_estimate = 4 * (inside_circle / n_samples)
    return pi_estimate

if __name__ == "__main__":
    print("=== Monte Carlo Simulation: Estimating Pi ===")
    print(f"{'Samples (N)':<12} | {'Estimated Pi':<14} | {'Error Amount':<12} | {'Error %':<8}")
    print("-" * 55)
    
    actual_pi = 3.141592653589793
    for samples in [100, 1000, 10000, 100000, 1000000]:
        pi_est = estimate_pi(samples)
        error = abs(pi_est - actual_pi)
        error_pct = (error / actual_pi) * 100
        print(f"{samples:<12d} | {pi_est:<14.6f} | {error:<12.6f} | {error_pct:.4f}%")
