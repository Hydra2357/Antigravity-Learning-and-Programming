"""
Recurrence Relations Solver and Demonstrator
This script:
1. Implements a Master Theorem solver that parses:
   T(n) = a * T(n/b) + O(n^d * log^k n)
2. Implements recursive relations (like Fibonacci and Merge Sort recurrence)
   to demonstrate empirical step counts matching theoretical recurrences.
"""

import math

def solve_master_theorem(a, b, d, k=0):
    """
    Solves T(n) = a * T(n/b) + O(n^d * log^k n)
    Returns a string representation of the Big-O complexity.
    """
    if a < 1 or b <= 1:
        raise ValueError("Invalid parameters: 'a' must be >= 1 and 'b' must be > 1")
    
    # Calculate log_b(a)
    log_b_a = math.log(a) / math.log(b)
    
    # Compare log_b(a) and d
    # Using epsilon comparison for floating-point accuracy
    epsilon = 1e-9
    
    if abs(log_b_a - d) < epsilon:
        # Case 2: log_b(a) == d
        return f"O(n^{d:.3f} * log^{k+1} n)"
    elif log_b_a > d:
        # Case 1: log_b(a) > d
        return f"O(n^{log_b_a:.3f})"
    else:
        # Case 3: log_b(a) < d
        return f"O(n^{d:.3f} * log^{k} n)"

# Global step counters for empirical analysis
fib_steps = 0
merge_recurrence_steps = 0

def fibonacci_recursive(n):
    global fib_steps
    fib_steps += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def merge_sort_recurrence_sim(n):
    """
    Simulates the recurrence relation of Merge Sort:
    T(n) = 2 * T(n/2) + O(n)
    """
    global merge_recurrence_steps
    merge_recurrence_steps += n  # O(n) work done at the current level
    if n <= 1:
        return
    merge_sort_recurrence_sim(n // 2)
    merge_sort_recurrence_sim(n - n // 2)

if __name__ == "__main__":
    print("=== Master Theorem Solver Examples ===")
    # 1. Merge Sort: T(n) = 2*T(n/2) + O(n^1) -> a=2, b=2, d=1
    print(f"Merge Sort: T(n) = 2*T(n/2) + O(n) => {solve_master_theorem(a=2, b=2, d=1)}")
    
    # 2. Binary Search: T(n) = 1*T(n/2) + O(1) -> a=1, b=2, d=0
    print(f"Binary Search: T(n) = T(n/2) + O(1) => {solve_master_theorem(a=1, b=2, d=0)}")
    
    # 3. Strassen's Matrix Mult: T(n) = 7*T(n/2) + O(n^2) -> a=7, b=2, d=2
    print(f"Strassen's: T(n) = 7*T(n/2) + O(n^2) => {solve_master_theorem(a=7, b=2, d=2)}")
    
    # 4. Karatsuba Mult: T(n) = 3*T(n/2) + O(n^1) -> a=3, b=2, d=1
    print(f"Karatsuba: T(n) = 3*T(n/2) + O(n) => {solve_master_theorem(a=3, b=2, d=1)}")

    print("\n=== Empirical Recurrence Relation Analysis ===")
    
    print("\n1. Fibonacci Recurrence: T(n) = T(n-1) + T(n-2) + O(1)")
    for n in [5, 10, 15, 20]:
        fib_steps = 0
        val = fibonacci_recursive(n)
        ratio = fib_steps / (1.61803398875 ** n)
        print(f"N = {n:2d} | Result = {val:5d} | Total calls = {fib_steps:6d} | ratio T(n)/1.618^n = {ratio:.4f}")

    print("\n2. Merge Sort Recurrence Simulation: T(n) = 2*T(n/2) + O(n)")
    for n in [64, 128, 256, 512, 1024]:
        merge_recurrence_steps = 0
        merge_sort_recurrence_sim(n)
        theoretical = n * math.log2(n)
        ratio = merge_recurrence_steps / theoretical if theoretical > 0 else 0
        print(f"N = {n:4d} | Work done = {merge_recurrence_steps:5d} | Theoretical (N log N) = {theoretical:6.1f} | Ratio = {ratio:.4f}")
