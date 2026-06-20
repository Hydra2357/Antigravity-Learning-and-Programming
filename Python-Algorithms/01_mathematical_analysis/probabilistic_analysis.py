"""
Probabilistic Analysis Demonstrations
This file contains two core examples:
1. The Birthday Paradox:
   - Simulates groups of N people to find the empirical probability of a shared birthday.
   - Compares it with the mathematical calculation: P(shared) = 1 - (365! / (365^N * (365-N)!))
2. The Hiring Problem (Secretary Problem):
   - Demonstrates the 1/e (~37%) rule for selecting the best secretary.
   - Runs simulations to show that checking and rejecting the first n/e candidates, 
     then selecting the first candidate better than all seen so far, yields the best candidate with probability ~1/e.
"""

import random
import math

def calculate_birthday_probability(n):
    """Calculates mathematical probability of at least two people sharing a birthday."""
    if n > 365:
        return 1.0
    prob_all_different = 1.0
    for i in range(n):
        prob_all_different *= (365 - i) / 365
    return 1 - prob_all_different

def simulate_birthday_paradox(n, trials=10000):
    """Simulates trials for N people to estimate shared birthday probability."""
    shared_count = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(n)]
        if len(birthdays) != len(set(birthdays)):
            shared_count += 1
    return shared_count / trials

def run_hiring_simulation(n, r, trials=10000):
    """
    Simulates the Hiring Problem.
    n: Total candidates.
    r: Reject the first r candidates, then pick the first one better than the best of the first r.
    Returns: The probability of hiring the absolute best candidate.
    """
    successes = 0
    for _ in range(trials):
        # Candidates are represented by their ranks: 1 (best) to n (worst)
        candidates = list(range(1, n + 1))
        random.shuffle(candidates)
        
        # Best rank of the first r candidates (we want the minimum number, since rank 1 is best)
        best_in_sample = min(candidates[:r]) if r > 0 else float('inf')
        
        hired = None
        for i in range(r, n):
            if candidates[i] < best_in_sample:
                hired = candidates[i]
                break
        
        # If we didn't pick anyone, we get the last candidate
        if hired is None:
            hired = candidates[-1]
            
        if hired == 1:
            successes += 1
            
    return successes / trials

if __name__ == "__main__":
    print("=== Birthday Paradox Simulation vs Theory ===")
    print(f"{'Group Size':<10} | {'Theoretical Prob':<18} | {'Simulated Prob (10k trials)':<28}")
    print("-" * 65)
    for size in [5, 10, 20, 23, 30, 50, 75]:
        theory = calculate_birthday_probability(size)
        sim = simulate_birthday_paradox(size)
        print(f"{size:<10d} | {theory:<18.4f} | {sim:<28.4f}")

    print("\n=== Hiring Problem (Secretary Problem) Simulation ===")
    n_candidates = 100
    print(f"Total Candidates: {n_candidates}")
    print(f"Rule: Reject the first R candidates, then pick the first one better than the best seen so far.")
    print("-" * 55)
    print(f"{'Reject R':<10} | {'Ratio R/N':<12} | {'Success Prob (Pick rank 1)'}")
    print("-" * 55)
    
    # We test different rejection thresholds R
    best_prob = 0
    best_r = 0
    for r in range(5, 75, 5):
        prob = run_hiring_simulation(n_candidates, r)
        ratio = r / n_candidates
        print(f"{r:<10d} | {ratio:<12.2f} | {prob:.4f}")
        if prob > best_prob:
            best_prob = prob
            best_r = r
            
    # The optimal mathematical cutoff is n / e
    optimal_cutoff = int(round(n_candidates / math.e))
    optimal_prob = run_hiring_simulation(n_candidates, optimal_cutoff)
    print("-" * 55)
    print(f"Empirical Best cutoff: R = {best_r} (Prob = {best_prob:.4f})")
    print(f"Theoretical Optimal cutoff: N/e = {optimal_cutoff} (Prob = {optimal_prob:.4f}, expected ~37%)")
