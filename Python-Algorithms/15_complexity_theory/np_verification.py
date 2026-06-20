"""
Complexity Theory Concepts: P vs NP
This file demonstrates the computational distinction between:
1. Verification (NP): Checking if a given certificate (solution) is valid. This can be done in polynomial time.
2. Solving (NP-Hard): Finding a valid solution from scratch. For NP-Complete/NP-Hard problems,
   no polynomial-time algorithm is known, so we resort to exponential-time search (e.g., O(2^N)).

Problem: Subset Sum (NP-Complete)
- Given a set of integers and a target sum, is there a subset that sums to the target?
"""

import time

# --- 1. Verification (Polynomial Time - O(N)) ---
def verify_subset_sum(subset, target):
    """
    NP Certificate Verifier.
    Given a candidate subset (the certificate) and the target,
    verifies if the subset is valid (i.e. elements sum to target).
    Time Complexity: O(N) where N is the size of the subset.
    """
    # Simply sum the elements and check if they equal target
    return sum(subset) == target

# --- 2. Solving (Exponential Time - O(2^N)) ---
def solve_subset_sum_exact(nums, target):
    """
    NP-Hard Solver.
    Finds a subset of nums that sums to target.
    Time Complexity: O(2^N) in the worst case (searching all subsets).
    """
    solution = []
    
    def backtrack(idx, current_sum, current_subset):
        if current_sum == target:
            solution.append(list(current_subset))
            return True
        if idx >= len(nums) or current_sum > target: # Assuming positive numbers for simple pruning
            return False
            
        # Case 1: Include nums[idx]
        current_subset.append(nums[idx])
        if backtrack(idx + 1, current_sum + nums[idx], current_subset):
            return True
        current_subset.pop()
        
        # Case 2: Exclude nums[idx]
        if backtrack(idx + 1, current_sum, current_subset):
            return True
            
        return False

    backtrack(0, 0, [])
    return solution[0] if solution else None

if __name__ == "__main__":
    print("=== Complexity Theory: P vs NP (Subset Sum) ===")
    
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    print(f"\nSet: {nums} | Target Sum: {target}")
    
    # 1. Solving (Hard)
    print("\n--- Phase 1: Solving (NP-Hard Search) ---")
    start = time.perf_counter()
    certificate = solve_subset_sum_exact(nums, target)
    solve_duration = time.perf_counter() - start
    print(f"  Solver output (Certificate): {certificate}")
    print(f"  Solver runtime:              {solve_duration:.6f} seconds")
    
    # 2. Verifying (Easy)
    print("\n--- Phase 2: Verification (NP Poly-Time Check) ---")
    start = time.perf_counter()
    is_valid = verify_subset_sum(certificate, target) if certificate else False
    verify_duration = time.perf_counter() - start
    print(f"  Verifier output:             {is_valid}")
    print(f"  Verifier runtime:            {verify_duration:.6f} seconds")
    
    print(f"\nRatio of Solve Time to Verify Time: {solve_duration / verify_duration:.2f}x")
